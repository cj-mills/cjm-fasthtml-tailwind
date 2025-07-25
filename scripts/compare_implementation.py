#!/usr/bin/env python3
"""
Compare implemented Python modules against Tailwind CSS documentation.

This script analyzes the generated Python modules and compares them against
the Markdown documentation to identify missing implementations.
"""

import argparse
import ast
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
import importlib.util


def extract_classes_from_markdown(content: str) -> Dict[str, List[str]]:
    """
    Extract all CSS classes from markdown tables.
    
    Args:
        content: Markdown content
        
    Returns:
        Dictionary mapping section names to list of CSS classes
    """
    classes = {}
    lines = content.split('\n')
    
    current_section = None
    in_table = False
    in_classes_section = False
    
    for i, line in enumerate(lines):
        # Track current section
        if line.startswith('## '):
            current_section = line[3:].strip()
            in_classes_section = False
        
        # Check if we're in a Classes subsection
        if line.strip() == '### Classes':
            in_classes_section = True
            continue
        
        # Detect table start (only in Classes sections)
        if in_classes_section and not in_table and '|' in line and i + 1 < len(lines) and '| ---' in lines[i + 1]:
            in_table = True
            continue
        
        # Process table rows
        if in_table:
            if line.strip().startswith('|') and '| ---' not in line:
                # Extract the class name from the first column
                parts = line.split('|')
                if len(parts) >= 3:  # Has at least class and style columns
                    class_name = parts[1].strip()
                    if class_name and class_name != 'Class':  # Skip header
                        if current_section not in classes:
                            classes[current_section] = []
                        classes[current_section].append(class_name)
            elif not line.strip().startswith('|'):
                # Table ended
                in_table = False
    
    return classes


def parse_class_patterns(class_names: List[str]) -> Dict[str, Set[str]]:
    """
    Parse class patterns into categories.
    
    Args:
        class_names: List of CSS class names
        
    Returns:
        Dictionary categorizing classes
    """
    patterns = {
        'static': set(),      # Static classes like 'block', 'hidden'
        'numeric': set(),     # Classes with <number> placeholder
        'fraction': set(),    # Classes with <fraction> placeholder
        'arbitrary': set(),   # Classes with [<value>] placeholder
        'custom_prop': set(), # Classes with (<custom-property>) placeholder
        'special': set(),     # Classes with other patterns
    }
    
    for class_name in class_names:
        if '<number>' in class_name:
            # Extract base pattern
            base = re.sub(r'-?<number>', '', class_name)
            patterns['numeric'].add(base)
        elif '<fraction>' in class_name:
            base = re.sub(r'<fraction>', '', class_name)
            patterns['fraction'].add(base)
        elif '[<value>]' in class_name:
            base = class_name.replace('[<value>]', '')
            patterns['arbitrary'].add(base)
        elif '(<custom-property>)' in class_name:
            base = class_name.replace('(<custom-property>)', '')
            patterns['custom_prop'].add(base)
        elif any(placeholder in class_name for placeholder in ['<', '>']):
            patterns['special'].add(class_name)
        else:
            patterns['static'].add(class_name)
    
    return patterns


def analyze_python_module(module_path: Path) -> Dict[str, Set[str]]:
    """
    Analyze a Python module to extract implemented utilities.
    
    Args:
        module_path: Path to Python module
        
    Returns:
        Dictionary of implemented utilities
    """
    implemented = {
        'variables': set(),      # Variable assignments
        'functions': set(),      # Function definitions
        'classes': set(),        # Class definitions
        'factories': set(),      # Factory instances
        'string_literals': set() # String literals that look like CSS classes
    }
    
    try:
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            # Variable assignments
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        implemented['variables'].add(target.id)
            
            # Function definitions
            elif isinstance(node, ast.FunctionDef):
                implemented['functions'].add(node.name)
            
            # Class definitions
            elif isinstance(node, ast.ClassDef):
                implemented['classes'].add(node.name)
            
            # String literals that look like CSS classes
            elif isinstance(node, ast.Constant) and isinstance(node.value, str):
                value = node.value
                if re.match(r'^[a-z\-]+$', value) and '-' in value:
                    implemented['string_literals'].add(value)
        
        # Look for factory patterns
        for line in content.split('\n'):
            # Match patterns like: w = ScaledFactory("w", SIZE_CONFIG)
            factory_match = re.match(r'(\w+)\s*=\s*\w*Factory\(["\'](\w+)["\']', line)
            if factory_match:
                var_name, prefix = factory_match.groups()
                implemented['factories'].add(f"{var_name} ({prefix})")
        
    except Exception as e:
        print(f"Error analyzing {module_path}: {e}")
    
    return implemented


def compare_implementations(
    doc_classes: Dict[str, List[str]], 
    module_info: Dict[str, Dict[str, Set[str]]]
) -> Dict[str, Dict[str, List[str]]]:
    """
    Compare documentation classes against implemented modules.
    
    Args:
        doc_classes: Classes from documentation
        module_info: Information from Python modules
        
    Returns:
        Dictionary of missing implementations by category
    """
    missing = {}
    
    for section, classes in doc_classes.items():
        patterns = parse_class_patterns(classes)
        missing[section] = {
            'static': [],
            'patterns': [],
            'special': []
        }
        
        # Check static classes
        all_implemented = set()
        for info in module_info.values():
            all_implemented.update(info['variables'])
            all_implemented.update(info['string_literals'])
        
        # Also check for underscored versions (e.g., _2xl -> 2xl)
        implemented_normalized = set()
        for impl in all_implemented:
            implemented_normalized.add(impl)
            if impl.startswith('_') and len(impl) > 1:
                implemented_normalized.add(impl[1:])
        
        for static_class in patterns['static']:
            # Normalize class name
            normalized = static_class.replace('-', '_')
            
            # Check various forms
            if not any(form in implemented_normalized for form in [
                static_class,           # Original form
                normalized,             # Underscored form
                static_class.replace('-', ''),  # No separator
            ]):
                missing[section]['static'].append(static_class)
        
        # Check for pattern support (numeric, fraction, etc.)
        factory_prefixes = set()
        for info in module_info.values():
            for factory in info['factories']:
                if '(' in factory:
                    prefix = factory.split('(')[1].rstrip(')')
                    factory_prefixes.add(prefix)
        
        # Check if patterns are supported by factories
        for pattern_type, bases in [
            ('numeric', patterns['numeric']),
            ('fraction', patterns['fraction']),
            ('arbitrary', patterns['arbitrary']),
            ('custom_prop', patterns['custom_prop'])
        ]:
            for base in bases:
                # Extract the prefix from the base
                if base.startswith('-'):
                    prefix = base[1:].rstrip('-')
                else:
                    prefix = base.rstrip('-')
                
                if prefix and prefix not in factory_prefixes:
                    missing[section]['patterns'].append(f"{base}<{pattern_type}>")
        
        # Special patterns need manual review
        missing[section]['special'] = list(patterns['special'])
    
    return missing


def generate_comparison_report(
    missing: Dict[str, Dict[str, List[str]]], 
    module_info: Dict[str, Dict[str, Set[str]]]
) -> str:
    """
    Generate a comparison report.
    
    Args:
        missing: Missing implementations
        module_info: Module information
        
    Returns:
        Markdown report
    """
    lines = []
    lines.append("# Implementation Comparison Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    
    # Count totals
    total_missing_static = sum(len(m['static']) for m in missing.values())
    total_missing_patterns = sum(len(m['patterns']) for m in missing.values())
    total_missing_special = sum(len(m['special']) for m in missing.values())
    
    lines.append(f"- Missing static classes: {total_missing_static}")
    lines.append(f"- Missing pattern implementations: {total_missing_patterns}")
    lines.append(f"- Special patterns needing review: {total_missing_special}")
    lines.append("")
    
    # Implemented summary
    lines.append("## Implemented Elements")
    lines.append("")
    for module_name, info in module_info.items():
        lines.append(f"### {module_name}")
        lines.append(f"- Variables: {len(info['variables'])}")
        lines.append(f"- Functions: {len(info['functions'])}")
        lines.append(f"- Classes: {len(info['classes'])}")
        lines.append(f"- Factories: {len(info['factories'])}")
        if info['factories']:
            for factory in sorted(info['factories']):
                lines.append(f"  - {factory}")
        lines.append("")
    
    # Missing implementations
    lines.append("## Missing Implementations by Section")
    lines.append("")
    
    for section, miss_info in sorted(missing.items()):
        if any(miss_info.values()):  # Only show sections with missing items
            lines.append(f"### {section}")
            lines.append("")
            
            if miss_info['static']:
                lines.append("**Missing static classes:**")
                for cls in sorted(miss_info['static']):
                    lines.append(f"- `{cls}`")
                lines.append("")
            
            if miss_info['patterns']:
                lines.append("**Missing pattern support:**")
                for pattern in sorted(set(miss_info['patterns'])):
                    lines.append(f"- `{pattern}`")
                lines.append("")
            
            if miss_info['special']:
                lines.append("**Special patterns to review:**")
                for pattern in sorted(miss_info['special']):
                    lines.append(f"- `{pattern}`")
                lines.append("")
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Compare Python implementation against Tailwind documentation'
    )
    parser.add_argument(
        '--docs-dir',
        type=Path,
        default=Path('claude-docs/tailwind/utility_classes'),
        help='Path to documentation directory'
    )
    parser.add_argument(
        '--module-dir',
        type=Path,
        default=Path('cjm_fasthtml_tailwind'),
        help='Path to Python module directory'
    )
    parser.add_argument(
        '--include',
        nargs='+',
        help='Specific documentation files to include (without .md extension)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('implementation_comparison.md'),
        help='Output file path'
    )
    
    args = parser.parse_args()
    
    # Resolve paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    docs_dir = project_root / args.docs_dir
    module_dir = project_root / args.module_dir
    output_path = project_root / args.output
    
    if not docs_dir.exists():
        print(f"Error: Documentation directory not found: {docs_dir}")
        return 1
    
    if not module_dir.exists():
        print(f"Error: Module directory not found: {module_dir}")
        return 1
    
    print(f"Analyzing documentation in: {docs_dir}")
    print(f"Analyzing Python modules in: {module_dir}")
    
    # Extract classes from documentation
    all_doc_classes = {}
    
    if args.include:
        doc_files = [docs_dir / f"{name}.md" for name in args.include]
    else:
        doc_files = list(docs_dir.glob("*.md"))
    
    for doc_file in doc_files:
        if doc_file.exists():
            with open(doc_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            classes = extract_classes_from_markdown(content)
            # Prefix with filename for clarity
            file_prefix = doc_file.stem
            for section, class_list in classes.items():
                key = f"{file_prefix} - {section}"
                all_doc_classes[key] = class_list
            
            print(f"  Extracted {sum(len(c) for c in classes.values())} classes from {doc_file.name}")
    
    # Analyze Python modules
    module_info = {}
    
    # Map documentation files to expected Python modules
    module_mapping = {
        'layout': ['utilities/layout.py'],
        'sizing': ['utilities/sizing.py'],
        'spacing': ['utilities/spacing.py'],
        'flexbox_and_grid': ['utilities/flexbox_grid.py', 'utilities/flexbox.py', 'utilities/grid.py']
    }
    
    # First check for existing modules based on documentation files
    if args.include:
        for doc_name in args.include:
            possible_modules = module_mapping.get(doc_name, [f"utilities/{doc_name}.py"])
            for module_name in possible_modules:
                module_path = module_dir / module_name
                if module_path.exists():
                    module_info[module_name] = analyze_python_module(module_path)
                    print(f"  Analyzed {module_path}")
    
    # Also analyze all Python files in the module directory
    for py_file in module_dir.rglob("*.py"):
        if py_file.name != "__init__.py" and py_file.relative_to(module_dir).as_posix() not in module_info:
            rel_path = py_file.relative_to(module_dir).as_posix()
            module_info[rel_path] = analyze_python_module(py_file)
    
    # Compare implementations
    missing = compare_implementations(all_doc_classes, module_info)
    
    # Generate report
    report = generate_comparison_report(missing, module_info)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nComparison report written to: {output_path}")
    
    return 0


if __name__ == '__main__':
    exit(main())