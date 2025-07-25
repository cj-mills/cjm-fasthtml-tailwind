#!/usr/bin/env python3
"""
Script to extract Tailwind CSS class documentation from the official Tailwind CSS website
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin
from pathlib import Path
from tqdm import tqdm
from nbdev.config import get_config
import argparse


def extract_navigation_links(url="https://tailwindcss.com/docs/installation/using-vite"):
    """Extract navigation links from the Tailwind CSS documentation sidebar"""
    
    try:
        # Fetch the page
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the navigation panel
        nav_panel = soup.find('nav', class_='flex flex-col gap-8')
        
        if not nav_panel:
            print("Could not find the navigation panel")
            return []
        
        # Extract all links with their hierarchy
        navigation_structure = []
        
        # Process each section in the navigation
        sections = nav_panel.find_all('div', recursive=False)
        
        for section in sections:
            # Try to find section title
            section_title_elem = section.find(['h2', 'h3', 'h4', 'h5', 'button'])
            section_title = section_title_elem.get_text(strip=True) if section_title_elem else "Untitled Section"
            
            # Find all links in this section
            links = section.find_all('a')
            
            if links:
                section_data = {
                    'title': section_title,
                    'links': []
                }
                
                for link in links:
                    href = link.get('href')
                    link_text = link.get_text(strip=True)
                    
                    if href and link_text:
                        # Make absolute URL
                        absolute_url = urljoin(url, href)
                        
                        # Only include tailwindcss.com links
                        if 'tailwindcss.com' in absolute_url:
                            section_data['links'].append({
                                'text': link_text,
                                'url': absolute_url
                            })
                
                if section_data['links']:
                    navigation_structure.append(section_data)
        
        return navigation_structure
        
    except Exception as e:
        print(f"Error extracting navigation links: {e}")
        return []


def save_navigation_to_markdown(navigation_structure, output_file="claude-docs/tailwind/navigation_links.md"):
    """Save the extracted navigation structure to a Markdown file"""
    
    # Ensure output directory exists
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Tailwind CSS Documentation Navigation Links\n\n")
        f.write(f"Extracted from https://tailwindcss.com/docs/installation/using-vite\n\n")
        
        for section in navigation_structure:
            f.write(f"## {section['title']}\n\n")
            
            for link in section['links']:
                f.write(f"- [{link['text']}]({link['url']})\n")
            
            f.write("\n")
    
    print(f"Navigation links saved to {output_file}")
    print(f"Total sections: {len(navigation_structure)}")
    print(f"Total links: {sum(len(section['links']) for section in navigation_structure)}")


def html_table_to_markdown(table):
    """Convert HTML table to Markdown format"""
    rows = []
    
    # Extract headers
    headers = []
    header_row = table.find('thead')
    if header_row:
        for th in header_row.find_all('th'):
            headers.append(th.get_text(strip=True))
    else:
        # Try to find headers in first row
        first_row = table.find('tr')
        if first_row:
            for th in first_row.find_all(['th', 'td']):
                headers.append(th.get_text(strip=True))
    
    # For Tailwind tables, they use a grid structure
    if not headers:
        # Extract from grid structure
        cells = table.find_all(['div', 'td', 'th'])
        if len(cells) >= 2:
            headers = ['Class', 'Properties']
    
    if not headers:
        return None
    
    # Create header row
    rows.append('| ' + ' | '.join(headers) + ' |')
    rows.append('|' + '|'.join([' --- ' for _ in headers]) + '|')
    
    # Extract data rows
    # Find all tbody elements, including hidden ones
    tbodies = table.find_all('tbody')
    data_rows = []
    
    if tbodies:
        # Process all tbody elements
        for tbody in tbodies:
            tbody_rows = tbody.find_all('tr')
            data_rows.extend(tbody_rows)
    else:
        # Handle grid-based table structure
        all_cells = table.find_all('div', recursive=True)
        # Group cells in pairs (class name, properties)
        for i in range(0, len(all_cells), 2):
            if i + 1 < len(all_cells):
                data_rows.append([all_cells[i], all_cells[i + 1]])
    
    for row in data_rows:
        cells = []
        if isinstance(row, list):
            # Handle paired divs
            for cell in row:
                # Check if this cell contains a div with whitespace-pre class (multi-line content)
                whitespace_div = cell.find('div', class_='*:whitespace-pre!')
                
                if whitespace_div:
                    # This is a multi-line code block, preserve line breaks
                    text = whitespace_div.get_text(separator='\n').strip()
                    text = text.replace('\n', '<br>')
                else:
                    # Regular cell - use empty separator to avoid extra spaces
                    text = cell.get_text(separator='').strip()
                
                text = text.replace('|', '\\|')
                cells.append(text)
        else:
            # Handle traditional table rows
            for td in row.find_all(['td', 'th']):
                # Check if this cell contains a div with whitespace-pre class (multi-line content)
                whitespace_div = td.find('div', class_='*:whitespace-pre!')
                
                if whitespace_div:
                    # This is a multi-line code block, preserve line breaks
                    text = whitespace_div.get_text(separator='\n').strip()
                    text = text.replace('\n', '<br>')
                else:
                    # Regular cell - use empty separator to avoid extra spaces
                    text = td.get_text(separator='').strip()
                
                text = text.replace('|', '\\|')
                cells.append(text)
        
        if cells:
            rows.append('| ' + ' | '.join(cells) + ' |')
    
    return '\n'.join(rows) if len(rows) > 2 else None


def extract_page_content(url):
    """Extract title, description, and table from a Tailwind documentation page"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title_elem = soup.find('h1', {'data-title': 'true'})
        title = title_elem.get_text(strip=True) if title_elem else None
        
        # Extract description
        desc_elem = soup.find('p', {'data-description': 'true'})
        description = desc_elem.get_text(strip=True) if desc_elem else None
        
        # Extract table
        table_markdown = None
        table = soup.find('table', class_=re.compile(r'grid'))
        if table:
            table_markdown = html_table_to_markdown(table)
        
        return {
            'title': title,
            'description': description,
            'table': table_markdown,
            'url': url
        }
        
    except Exception as e:
        print(f"Error extracting content from {url}: {e}")
        return None


def extract_sections_from_layout_onwards(navigation_structure):
    """Extract only sections from Layout onwards"""
    
    # Sections to skip
    skip_sections = ['Getting started', 'Core concepts', 'Base styles']
    
    # Filter sections
    filtered_sections = []
    for section in navigation_structure:
        if section['title'] not in skip_sections:
            filtered_sections.append(section)
    
    return filtered_sections


def save_tailwind_classes_to_separate_files(classes_data, output_dir="claude-docs/tailwind/utility_classes"):
    """Save extracted Tailwind classes to separate Markdown files for each section"""
    
    # Create output directory if it doesn't exist
    cfg = get_config()
    project_dir = cfg.config_path
    output_path = project_dir/output_dir
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Group classes by section
    sections_data = {}
    for item in classes_data:
        section = item['section']
        if section not in sections_data:
            sections_data[section] = []
        sections_data[section].append(item['data'])
    
    # Save each section to a separate file
    saved_files = []
    for section, items in sections_data.items():
        # Create safe filename
        safe_filename = section.lower().replace(' ', '_').replace('&', 'and').replace('/', '_')
        file_path = output_path / f"{safe_filename}.md"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {section}\n\n")
            f.write(f"This document contains Tailwind CSS classes for {section}.\n\n")
            
            # Write content for each item in the section
            for data in items:
                if data:
                    if data['title']:
                        f.write(f"## {data['title']}\n\n")
                    
                    if data['description']:
                        f.write(f"{data['description']}\n\n")
                    
                    if data['table']:
                        f.write("### Classes\n\n")
                        f.write(data['table'])
                        f.write("\n\n")
                    
                    f.write(f"[Documentation]({data['url']})\n\n")
                    f.write("---\n\n")
        
        saved_files.append(file_path)
    
    # Create index file
    index_path = output_path / "README.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Tailwind CSS Utility Classes Documentation\n\n")
        f.write(f"This directory contains extracted Tailwind CSS classes organized by section.\n\n")
        f.write("## Sections\n\n")
        
        for section in sorted(sections_data.keys()):
            safe_filename = section.lower().replace(' ', '_').replace('&', 'and').replace('/', '_')
            f.write(f"- [{section}](./{safe_filename}.md)\n")
    
    print(f"Tailwind classes saved to {len(saved_files)} files in {output_dir}/")
    print(f"Index file created at {index_path}")


def save_tailwind_classes_to_markdown(classes_data, output_file="claude-docs/tailwind/tailwind_classes.md"):
    """Save extracted Tailwind classes to a Markdown file"""
    
    # Create output directory if it doesn't exist
    cfg = get_config()
    project_dir = cfg.config_path
    # Ensure output directory exists
    output_path = project_dir/output_file
    output_dir = output_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Tailwind CSS Classes Documentation\n\n")
        f.write(f"Extracted {len(classes_data)} class groups from tailwindcss.com\n\n")
        
        # Generate table of contents for H2 sections
        f.write("## Table of Contents\n\n")
        sections = []
        current_section = None
        
        # Collect unique sections
        for item in classes_data:
            if item['section'] != current_section:
                current_section = item['section']
                sections.append(current_section)
        
        # Write TOC links
        for section in sections:
            # Create anchor link (lowercase, replace spaces with hyphens)
            anchor = section.lower().replace(' ', '-').replace('&', '').replace('  ', ' ').strip()
            f.write(f"- [{section}](#{anchor})\n")
        
        f.write("\n---\n\n")
        
        # Write the actual content
        current_section = None
        
        for item in classes_data:
            # Write section header if it changed
            if item['section'] != current_section:
                current_section = item['section']
                f.write(f"## {current_section}\n\n")
            
            # Write class documentation
            if item['data']:
                data = item['data']
                if data['title']:
                    f.write(f"### {data['title']}\n\n")
                
                if data['description']:
                    f.write(f"{data['description']}\n\n")
                
                if data['table']:
                    f.write("#### Classes\n\n")
                    f.write(data['table'])
                    f.write("\n\n")
                
                f.write(f"[Documentation]({data['url']})\n\n")
                f.write("---\n\n")
    
    print(f"Tailwind classes saved to {output_file}")


def main():
    """Main function to extract Tailwind CSS classes documentation"""
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract Tailwind CSS class documentation')
    parser.add_argument(
        '--separate-files', 
        action='store_true',
        help='Save each section in a separate Markdown file instead of one combined file'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='claude-docs/tailwind/utility_classes',
        help='Output directory for separate files (default: claude-docs/tailwind/utility_classes)'
    )
    parser.add_argument(
        '--output-file',
        type=str,
        default='claude-docs/tailwind/tailwind_classes.md',
        help='Output file for combined mode (default: claude-docs/tailwind/tailwind_classes.md)'
    )
    
    args = parser.parse_args()
    
    print("Extracting Tailwind CSS documentation...")
    
    try:
        # Extract navigation structure
        navigation_structure = extract_navigation_links()
        
        if not navigation_structure:
            print("No navigation links found.")
            return
        
        # Filter to get only Layout section and below
        filtered_sections = extract_sections_from_layout_onwards(navigation_structure)
        
        print(f"Found {len(filtered_sections)} sections to process")
        
        # Extract content from each page
        all_classes_data = []
        
        for section in filtered_sections:
            print(f"\nProcessing section: {section['title']}")
            
            for link in tqdm(section['links'], desc=f"Extracting from {section['title']}", unit=" page"):
                # Add delay to be respectful to the server
                time.sleep(0.5)
                
                # Extract page content
                page_data = extract_page_content(link['url'])
                
                if page_data:
                    all_classes_data.append({
                        'section': section['title'],
                        'data': page_data
                    })
                    
                    # Show progress
                    if page_data['title'] and page_data['table']:
                        tqdm.write(f"  ✓ {page_data['title']}: Found table")
                    elif page_data['title']:
                        tqdm.write(f"  ✓ {page_data['title']}: No table found")
        
        # Save all extracted data
        if all_classes_data:
            if args.separate_files:
                save_tailwind_classes_to_separate_files(all_classes_data, args.output_dir)
            else:
                save_tailwind_classes_to_markdown(all_classes_data, args.output_file)
            
            # Print summary
            tables_found = sum(1 for item in all_classes_data if item['data'] and item['data']['table'])
            print(f"\nSummary:")
            print(f"- Total pages processed: {len(all_classes_data)}")
            print(f"- Pages with tables: {tables_found}")
        else:
            print("No data extracted.")
            
    except requests.RequestException as e:
        print(f"Error fetching pages: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()