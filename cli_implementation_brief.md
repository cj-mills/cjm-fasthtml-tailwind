# CLI Explorer Implementation for cjm-fasthtml-tailwind

I need your help implementing a CLI tool for the `cjm-fasthtml-tailwind` library. This tool will allow coding assistants like Claude Code to autonomously explore the library's API and learn how to use it.

## Project Context

The `cjm-fasthtml-tailwind` library provides a fully Python-abstracted Tailwind CSS v4 utility class builder for FastHTML projects. The project structure is:

```
cjm-fasthtml-tailwind/
├── nbs/
│   ├── core/
│   │   ├── base.ipynb       # Base classes, types, and protocols
│   │   ├── resources.ipynb  # CDN resources and headers
│   │   └── testing.ipynb    # Test page creation utilities
│   ├── builders/
│   │   └── scales.ipynb     # Numeric and named scale builders
│   ├── utilities/
│   │   ├── flexbox_and_grid.ipynb  # Flexbox and CSS Grid utilities
│   │   ├── layout.ipynb            # Display, position, overflow utilities
│   │   ├── sizing.ipynb            # Width, height, min/max sizing utilities
│   │   └── spacing.ipynb           # Padding and margin utilities
│   └── cli/
│       └── explorer.ipynb   # CLI tool (TO BE IMPLEMENTED)
```

## Key Requirements

1. **Zero hardcoded library information** - All information must be dynamically discovered from the Python modules
2. **Automatic adaptation** - Must handle new modules/utilities without modification
3. **Test functions as examples** - Use existing `test_<module>_<feature>_examples()` functions as ground-truth usage examples
4. **Intuitive navigation** - Help coding assistants quickly find what they need

## Test Function Convention

Each utility module contains test functions following this naming pattern:
- `test_<module>_<feature>_examples()`

Examples:
- `test_spacing_basic_examples()`
- `test_sizing_width_examples()`
- `test_layout_display_examples()`
- `test_flexbox_and_grid_basis_examples()`

These functions contain assertions that serve as usage examples:
```python
def test_spacing_basic_examples():
    """Test basic padding utilities with various scale values."""
    assert str(p(0)) == "p-0"
    assert str(p(4)) == "p-4"
    assert str(p.px) == "p-px"
```

## Implementation Task

Create `nbs/cli/explorer.ipynb` that implements a CLI tool with these commands:

### Core Commands Structure
```
cjm-fasthtml-tailwind
├── list                    # List available resources
│   ├── modules            # Show all modules with descriptions
│   ├── utilities          # Show all utility factories by category
│   └── examples           # Show all test example functions
│
├── explore <module>        # Deep dive into a specific module
│   ├── --utilities        # Show module's utilities with details
│   ├── --examples         # Show module's test examples
│   └── --all             # Show everything about the module
│
├── utility <name>          # Get details about a specific utility
│   ├── --values          # Show all valid values
│   ├── --examples        # Show usage from test functions
│   └── --related         # Show related utilities
│
├── search <keyword>        # Search across everything
│   └── --type [utility|function|example|all]
│
├── show-example <module> [<feature>]  # Display test function source
│
└── import-guide           # Show how to import and use the library
```

## Discovery Implementation Approach

1. **Module Discovery**: Dynamically find all modules in the package
2. **Utility Discovery**: Find all factory instances (ScaledFactory, DirectionalScaledFactory, SimpleFactory)
3. **Test Discovery**: Find all test functions and extract their assertions
4. **Configuration Extraction**: Extract scale configurations from utilities

## Example Output Format

```
$ cjm-fasthtml-tailwind utility p

📦 Utility: p (padding)
Module: cjm_fasthtml_tailwind.utilities.spacing
Type: DirectionalScaledFactory

✨ Creates padding utilities with directional support

🎯 Basic Usage:
  p(4)      → "p-4"      # All sides
  p.x(8)    → "px-8"     # Horizontal
  p.t(2)    → "pt-2"     # Top only

📐 Valid Values:
  • Numeric: 0-96, decimals (0.5, 1.5, 2.5, 3.5)
  • Special: px, auto
  • Arbitrary: "10px", "2.5rem", "--custom-spacing"

📍 Related:
  • m (margin) - Same scale, supports negative
  • space - For spacing between children

💡 See examples: cjm-fasthtml-tailwind show-example spacing basic
```

## Starting Point

Begin by:
1. Setting up the notebook with proper exports (`#| default_exp cli.explorer`)
2. Implementing the core discovery functions
3. Building the CLI command structure using argparse
4. Adding helpful output formatting

The implementation should follow nbdev conventions and include test cells to verify functionality.

Ready to start implementing?