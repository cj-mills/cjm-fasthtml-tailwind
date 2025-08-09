#!/usr/bin/env python3
"""
Script to recursively search for .ipynb notebooks in the nbs/ directory
and replace '_practical_examples' with '_fasthtml_examples'.
Ignores .ipynb_checkpoints folders.
"""

import json
import os
from pathlib import Path


def process_notebook(notebook_path):
    """
    Process a single notebook file to replace '_practical_examples' with '_fasthtml_examples'.
    
    Args:
        notebook_path: Path to the notebook file
        
    Returns:
        True if replacements were made, False otherwise
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_data = json.load(f)
        
        modified = False
        replacement_count = 0
        
        # Process cells in the notebook
        if 'cells' in notebook_data:
            for cell in notebook_data['cells']:
                if 'source' in cell:
                    # Handle source as a list of strings
                    if isinstance(cell['source'], list):
                        new_source = []
                        for line in cell['source']:
                            if '_practical_examples' in line:
                                new_line = line.replace('_practical_examples', '_fasthtml_examples')
                                new_source.append(new_line)
                                modified = True
                                replacement_count += line.count('_practical_examples')
                            else:
                                new_source.append(line)
                        cell['source'] = new_source
                    # Handle source as a single string
                    elif isinstance(cell['source'], str):
                        if '_practical_examples' in cell['source']:
                            cell['source'] = cell['source'].replace('_practical_examples', '_fasthtml_examples')
                            modified = True
                            replacement_count += cell['source'].count('_practical_examples')
        
        # Write back if modified
        if modified:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(notebook_data, f, indent=1, ensure_ascii=False)
            print(f"✓ {notebook_path}: Replaced {replacement_count} occurrence(s)")
            return True
        else:
            print(f"  {notebook_path}: No replacements needed")
            return False
            
    except Exception as e:
        print(f"✗ Error processing {notebook_path}: {e}")
        return False


def find_notebooks(directory):
    """
    Recursively find all .ipynb files in the specified directory,
    excluding .ipynb_checkpoints folders.
    
    Args:
        directory: Root directory to search
        
    Returns:
        List of Path objects for notebook files
    """
    notebooks = []
    
    for root, dirs, files in os.walk(directory):
        # Remove .ipynb_checkpoints from dirs to prevent walking into them
        if '.ipynb_checkpoints' in dirs:
            dirs.remove('.ipynb_checkpoints')
        
        # Find all .ipynb files in current directory
        for file in files:
            if file.endswith('.ipynb'):
                notebooks.append(Path(root) / file)
    
    return notebooks


def main():
    """Main function to execute the replacement process."""
    # Set the target directory
    nbs_dir = Path('nbs')
    
    if not nbs_dir.exists():
        print(f"Error: Directory '{nbs_dir}' does not exist")
        return 1
    
    print(f"Searching for notebooks in '{nbs_dir}'...")
    
    # Find all notebooks
    notebooks = find_notebooks(nbs_dir)
    
    if not notebooks:
        print("No notebook files found")
        return 0
    
    print(f"Found {len(notebooks)} notebook(s)\n")
    print("Processing notebooks...")
    print("-" * 50)
    
    # Process each notebook
    total_modified = 0
    for notebook_path in sorted(notebooks):
        if process_notebook(notebook_path):
            total_modified += 1
    
    print("-" * 50)
    print(f"\nSummary: Modified {total_modified} out of {len(notebooks)} notebook(s)")
    
    return 0


if __name__ == "__main__":
    exit(main())