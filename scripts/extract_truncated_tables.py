#!/usr/bin/env python3
"""
Extract truncated table rows from Tailwind CSS documentation.

This script extracts table rows starting from a specified row number (default: 11)
from Markdown documentation files and consolidates them into a single reference document.
"""

import argparse
import re
from pathlib import Path
from typing import List, Tuple, Optional


def extract_tables_from_markdown(content: str, start_row: int = 11) -> List[Tuple[str, List[str]]]:
    """
    Extract tables from markdown content and return rows from start_row onwards.
    
    Args:
        content: Markdown content
        start_row: Row number to start extraction from (1-indexed)
        
    Returns:
        List of tuples (section_name, truncated_rows)
    """
    tables = []
    lines = content.split('\n')
    
    current_section = None
    in_table = False
    table_rows = []
    table_start_line = 0
    
    for i, line in enumerate(lines):
        # Track current section
        if line.startswith('## '):
            current_section = line[3:].strip()
        
        # Detect table start
        if not in_table and '|' in line and i + 1 < len(lines) and '| ---' in lines[i + 1]:
            in_table = True
            table_start_line = i
            table_rows = [line]  # Include header
            continue
        
        # Process table rows
        if in_table:
            if line.strip().startswith('|'):
                table_rows.append(line)
            else:
                # Table ended, process it
                if len(table_rows) > start_row + 1:  # +1 for header, +1 for separator
                    # Get rows from start_row onwards (accounting for header and separator)
                    truncated_rows = [table_rows[0], table_rows[1]] + table_rows[start_row + 1:]
                    if len(truncated_rows) > 2:  # Has content beyond header
                        tables.append((current_section or "Unknown", truncated_rows))
                
                in_table = False
                table_rows = []
    
    # Handle table at end of file
    if in_table and len(table_rows) > start_row + 1:
        truncated_rows = [table_rows[0], table_rows[1]] + table_rows[start_row + 1:]
        if len(truncated_rows) > 2:
            tables.append((current_section or "Unknown", truncated_rows))
    
    return tables


def process_documentation_files(docs_dir: Path, start_row: int = 11, include_files: Optional[List[str]] = None) -> dict:
    """
    Process Markdown files in the documentation directory.
    
    Args:
        docs_dir: Path to documentation directory
        start_row: Row number to start extraction from
        include_files: List of file names to include (without .md extension). If None, process all files.
        
    Returns:
        Dictionary mapping file paths to extracted tables
    """
    results = {}
    
    # Find markdown files
    if include_files:
        # Only process specified files
        md_files = []
        for filename in include_files:
            file_path = docs_dir / f"{filename}.md"
            if file_path.exists():
                md_files.append(file_path)
            else:
                print(f"Warning: File not found: {file_path}")
    else:
        # Process all markdown files
        md_files = list(docs_dir.rglob("*.md"))
    
    for md_file in sorted(md_files):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tables = extract_tables_from_markdown(content, start_row)
        if tables:
            # Use relative path for cleaner output
            rel_path = md_file.relative_to(docs_dir)
            results[str(rel_path)] = tables
    
    return results


def generate_reference_document(results: dict, start_row: int) -> str:
    """
    Generate a consolidated reference document from extracted tables.
    
    Args:
        results: Dictionary mapping file paths to extracted tables
        start_row: The row number used for extraction
        
    Returns:
        Markdown content for reference document
    """
    lines = []
    lines.append(f"# Truncated Table Rows Reference (Row {start_row}+)")
    lines.append("")
    lines.append(f"This document contains table rows starting from row {start_row} that were truncated in the initial implementation.")
    lines.append("")
    lines.append("## Table of Contents")
    lines.append("")
    
    # Generate TOC
    for file_path in sorted(results.keys()):
        file_name = Path(file_path).stem.replace('_', ' ').title()
        anchor = file_path.replace('/', '-').replace('.md', '').replace('_', '-').lower()
        lines.append(f"- [{file_name}](#{anchor})")
    
    lines.append("")
    
    # Generate content sections
    for file_path, tables in results.items():
        file_name = Path(file_path).stem.replace('_', ' ').title()
        anchor_id = file_path.replace('/', '-').replace('.md', '').replace('_', '-')
        lines.append(f"## {file_name}")
        lines.append("")
        lines.append(f"Source: `{file_path}`")
        lines.append("")
        
        for section_name, rows in tables:
            lines.append(f"### {section_name}")
            lines.append("")
            lines.extend(rows)
            lines.append("")
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Extract truncated table rows from Tailwind CSS documentation'
    )
    parser.add_argument(
        '--docs-dir',
        type=Path,
        default=Path('claude-docs/tailwind/utility_classes'),
        help='Path to documentation directory (default: claude-docs/tailwind/utility_classes)'
    )
    parser.add_argument(
        '--start-row',
        type=int,
        default=11,
        help='Row number to start extraction from (default: 11)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('truncated_tables_reference.md'),
        help='Output file path (default: truncated_tables_reference.md)'
    )
    parser.add_argument(
        '--include',
        nargs='+',
        help='Specific files to include (without .md extension). E.g., --include layout sizing spacing flexbox_and_grid'
    )
    
    args = parser.parse_args()
    
    # Resolve paths relative to script location
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    docs_dir = project_root / args.docs_dir
    output_path = project_root / args.output
    
    if not docs_dir.exists():
        print(f"Error: Documentation directory not found: {docs_dir}")
        return 1
    
    print(f"Processing documentation files in: {docs_dir}")
    if args.include:
        print(f"Including only: {', '.join(args.include)}")
    print(f"Extracting rows from row {args.start_row} onwards...")
    
    # Process files
    results = process_documentation_files(docs_dir, args.start_row, args.include)
    
    if not results:
        print("No truncated tables found.")
        return 0
    
    # Generate reference document
    reference_content = generate_reference_document(results, args.start_row)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(reference_content)
    
    print(f"\nExtracted truncated tables from {len(results)} files:")
    total_tables = sum(len(tables) for tables in results.values())
    print(f"Total sections with truncated tables: {total_tables}")
    print(f"\nReference document written to: {output_path}")
    
    return 0


if __name__ == '__main__':
    exit(main())