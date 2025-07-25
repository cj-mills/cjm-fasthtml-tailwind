#!/usr/bin/env python3
"""
Script to extract Core concepts content from Tailwind CSS documentation
"""

import requests
from bs4 import BeautifulSoup, NavigableString
import re
import time
from urllib.parse import urljoin
from pathlib import Path
from tqdm import tqdm
from nbdev.config import get_config


def extract_navigation_links(url="https://tailwindcss.com/docs/installation/using-vite", target_section="Core concepts"):
    """Extract navigation links from a specific section of the Tailwind CSS documentation sidebar"""
    
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
        
        # Extract links from the target section
        navigation_links = []
        
        # Process each section in the navigation
        sections = nav_panel.find_all('div', recursive=False)
        
        for section in sections:
            # Try to find section title
            section_title_elem = section.find(['h2', 'h3', 'h4', 'h5', 'button'])
            section_title = section_title_elem.get_text(strip=True) if section_title_elem else "Untitled Section"
            
            # Check if this is our target section
            if section_title == target_section:
                # Find all links in this section
                links = section.find_all('a')
                
                for link in links:
                    href = link.get('href')
                    link_text = link.get_text(strip=True)
                    
                    if href and link_text:
                        # Make absolute URL
                        absolute_url = urljoin(url, href)
                        
                        # Only include tailwindcss.com links
                        if 'tailwindcss.com' in absolute_url:
                            navigation_links.append({
                                'text': link_text,
                                'url': absolute_url,
                                'filename': create_filename(link_text)
                            })
                break
        
        return navigation_links
        
    except Exception as e:
        print(f"Error extracting navigation links: {e}")
        return []


def create_filename(title):
    """Create a valid filename from a page title"""
    # Convert to lowercase and replace spaces/special chars with hyphens
    filename = title.lower()
    filename = re.sub(r'[^\w\s-]', '', filename)
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.strip('-') + '.md'


def format_html_code(code):
    """Format HTML code with proper indentation and newlines"""
    # Simple HTML formatter for common patterns
    # Add newlines after opening tags and before closing tags
    code = re.sub(r'>\s*<', '>\n<', code)
    
    # Split into lines and indent
    lines = code.split('\n')
    formatted_lines = []
    indent_level = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Decrease indent for closing tags
        if line.startswith('</') or line == '/>':
            indent_level = max(0, indent_level - 1)
        
        # Add the line with current indentation
        formatted_lines.append('  ' * indent_level + line)
        
        # Increase indent for opening tags (not self-closing)
        if line.startswith('<') and not line.startswith('</') and not line.endswith('/>') and not line.startswith('<!--'):
            # Check if it's a self-closing tag like <br> or <img>
            tag_name = re.match(r'<(\w+)', line)
            if tag_name:
                tag = tag_name.group(1).lower()
                if tag not in ['br', 'img', 'input', 'meta', 'link', 'hr']:
                    indent_level += 1
    
    return '\n'.join(formatted_lines)


def format_css_code(code):
    """Format CSS code with proper indentation and newlines"""
    # Add newlines after { and before }
    code = re.sub(r'\s*{\s*', ' {\n  ', code)
    code = re.sub(r';\s*', ';\n  ', code)
    code = re.sub(r'\s*}\s*', '\n}\n', code)
    
    # Clean up extra spaces and newlines
    code = re.sub(r'\n\s*\n', '\n', code)
    code = re.sub(r'  \n}', '\n}', code)
    
    return code.strip()


def element_to_markdown(element, depth=0, context=None):
    """Convert a BeautifulSoup element to Markdown format
    
    Args:
        element: BeautifulSoup element to convert
        depth: Current nesting depth (for lists)
        context: Additional context (e.g., detected language for code blocks)
    """
    
    if isinstance(element, NavigableString):
        text = str(element)
        # Clean up whitespace but preserve single spaces
        if text.strip():
            return text
        elif text == ' ':
            return ' '
        else:
            return ''
    
    tag_name = element.name
    
    # Headers
    if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag_name[1])
        text = ''
        
        # Check if the header contains an anchor with the actual text
        anchor = element.find('a')
        if anchor and anchor.get_text(strip=True):
            # Get text from the anchor, excluding any nested anchor links
            text = anchor.get_text(strip=True)
            # Remove the # symbol if it's part of an anchor link
            if text.startswith('#'):
                text = text[1:].strip()
        else:
            # Extract text without anchor links
            text_parts = []
            for child in element.children:
                if isinstance(child, NavigableString):
                    text_parts.append(str(child).strip())
                elif child.name != 'a' or 'anchor' not in child.get('class', []):
                    text_parts.append(child.get_text(strip=True))
            text = ' '.join(text_parts).strip()
        
        # Only return header if we have actual text
        if text:
            return '\n\n' + '#' * level + ' ' + text + '\n\n'
        else:
            return ''
    
    # Paragraphs
    elif tag_name == 'p':
        content = ''.join(element_to_markdown(child, depth, context) for child in element.children)
        return '\n\n' + content + '\n\n'
    
    # Links
    elif tag_name == 'a':
        text = element.get_text(strip=True)
        href = element.get('href', '')
        if href and not href.startswith('#'):
            # Make absolute URL if relative
            if href.startswith('/'):
                href = 'https://tailwindcss.com' + href
            return f'[{text}]({href})'
        return text
    
    # Figure elements (often contain code examples)
    elif tag_name == 'figure':
        # Check if this figure contains a code block
        pre_elem = element.find('pre')
        if pre_elem:
            # Extract just the code from the figure
            # Figure elements typically contain HTML examples
            return element_to_markdown(pre_elem, depth, context={'language': 'html'})
        # Otherwise process normally
        content = ''.join(element_to_markdown(child, depth, context) for child in element.children)
        return content
    
    # Code blocks
    elif tag_name == 'pre':
        code_elem = element.find('code')
        if code_elem:
            # Extract language from class
            classes = code_elem.get('class', [])
            lang = ''
            for cls in classes:
                if cls.startswith('language-'):
                    lang = cls.replace('language-', '')
                    break
            
            # If no language found and we have context, use it
            if not lang and context and 'language' in context:
                lang = context['language']
            
            # Get the code text and preserve formatting
            # Use a more robust method to preserve the original formatting
            # Extract the raw string content from the code element
            code = ''
            
            # Try to get the string representation directly
            if hasattr(code_elem, 'strings'):
                code = ''.join(code_elem.strings)
            else:
                # Fallback to manual extraction
                for child in code_elem.descendants:
                    if isinstance(child, NavigableString):
                        code += str(child)
            
            # Auto-detect language if not specified
            if not lang:
                # Check if it looks like HTML
                if re.search(r'<[a-zA-Z][\s\S]*>', code):
                    lang = 'html'
                # Check if it looks like CSS
                elif re.search(r'[.#]?[\w-]+\s*{[\s\S]*}', code) or '@' in code and '{' in code:
                    lang = 'css'
                # Check if it looks like JavaScript
                elif any(keyword in code for keyword in ['function', 'const', 'let', 'var', 'import', 'export', '=>']):
                    lang = 'javascript'
            
            # Format the code based on language
            if lang in ['html', 'xml'] or (context and context.get('language') == 'html'):
                # Format HTML code - add newlines and indentation
                code = format_html_code(code)
            elif lang == 'css':
                # Format CSS code
                code = format_css_code(code)
            else:
                # Clean up the code indentation for other languages
                lines = code.split('\n')
                # Find minimum indentation (excluding empty lines)
                min_indent = float('inf')
                for line in lines:
                    if line.strip():
                        indent = len(line) - len(line.lstrip())
                        min_indent = min(min_indent, indent)
                
                # Remove minimum indentation from all lines
                if min_indent < float('inf'):
                    cleaned_lines = []
                    for line in lines:
                        if line.strip():
                            cleaned_lines.append(line[min_indent:])
                        else:
                            cleaned_lines.append('')
                    code = '\n'.join(cleaned_lines)
            
            return f'\n\n```{lang}\n{code}\n```\n\n'
        return f'\n\n```\n{element.get_text()}\n```\n\n'
    
    # Inline code
    elif tag_name == 'code':
        # Check if parent is pre (already handled)
        if element.parent and element.parent.name == 'pre':
            return element.get_text()
        return f'`{element.get_text()}`'
    
    # Bold/Strong
    elif tag_name in ['strong', 'b']:
        content = ''.join(element_to_markdown(child, depth) for child in element.children)
        return f'**{content}**'
    
    # Italic/Emphasis
    elif tag_name in ['em', 'i']:
        content = ''.join(element_to_markdown(child, depth) for child in element.children)
        return f'*{content}*'
    
    # Lists
    elif tag_name == 'ul':
        items = []
        for li in element.find_all('li', recursive=False):
            content = ''.join(element_to_markdown(child, depth + 1) for child in li.children).strip()
            items.append(f'{"  " * depth}- {content}')
        return '\n\n' + '\n'.join(items) + '\n\n'
    
    elif tag_name == 'ol':
        items = []
        for i, li in enumerate(element.find_all('li', recursive=False), 1):
            content = ''.join(element_to_markdown(child, depth + 1) for child in li.children).strip()
            items.append(f'{"  " * depth}{i}. {content}')
        return '\n\n' + '\n'.join(items) + '\n\n'
    
    # Blockquotes
    elif tag_name == 'blockquote':
        content = ''.join(element_to_markdown(child, depth) for child in element.children)
        lines = content.strip().split('\n')
        quoted_lines = ['> ' + line if line else '>' for line in lines]
        return '\n\n' + '\n'.join(quoted_lines) + '\n\n'
    
    # Tables
    elif tag_name == 'table':
        rows = []
        
        # Extract headers
        thead = element.find('thead')
        if thead:
            headers = []
            for th in thead.find_all('th'):
                headers.append(th.get_text(strip=True))
            if headers:
                rows.append('| ' + ' | '.join(headers) + ' |')
                rows.append('|' + '|'.join([' --- ' for _ in headers]) + '|')
        
        # Extract body
        tbody = element.find('tbody')
        if tbody:
            for tr in tbody.find_all('tr'):
                cells = []
                for td in tr.find_all(['td', 'th']):
                    cell_content = ''.join(element_to_markdown(child, depth, context) for child in td.children).strip()
                    cells.append(cell_content)
                if cells:
                    rows.append('| ' + ' | '.join(cells) + ' |')
        
        return '\n\n' + '\n'.join(rows) + '\n\n' if rows else ''
    
    # Horizontal rule
    elif tag_name == 'hr':
        return '\n\n---\n\n'
    
    # Line breaks
    elif tag_name == 'br':
        return '  \n'
    
    # Images
    elif tag_name == 'img':
        alt = element.get('alt', '')
        src = element.get('src', '')
        if src:
            # Make absolute URL if relative
            if src.startswith('/'):
                src = 'https://tailwindcss.com' + src
            return f'![{alt}]({src})'
        return ''
    
    # Divs and other containers - just process children
    elif tag_name in ['div', 'section', 'article', 'main', 'aside', 'nav', 'span']:
        # Skip certain divs (like code highlight overlays)
        if element.get('class'):
            classes = element.get('class', [])
            if any('highlight' in cls for cls in classes):
                return ''
            
            # TODO: Convert grid elements to markdown tables in the future
            # For now, skip interactive grid elements (like color palettes)
            if any('grid' in cls for cls in classes) and element.find_all(['button', 'input']):
                return '\n\n[Interactive color palette not shown]\n\n'
        
        # Check if this is a language hint before a code block
        # (e.g., a div/span containing just "HTML", "CSS", etc. before a pre element)
        text_content = element.get_text(strip=True)
        if text_content and text_content.upper() in ['HTML', 'CSS', 'JS', 'JAVASCRIPT', 'JSX', 'BASH', 'SHELL', 'JSON', 'YAML', 'XML']:
            next_sibling = element.find_next_sibling()
            if next_sibling and (next_sibling.name == 'pre' or (next_sibling.name == 'figure' and next_sibling.find('pre'))):
                # Skip this element as it's just a language label
                # But pass the language info to the next element
                lang_map = {
                    'HTML': 'html',
                    'CSS': 'css',
                    'JS': 'javascript',
                    'JAVASCRIPT': 'javascript',
                    'JSX': 'jsx',
                    'BASH': 'bash',
                    'SHELL': 'bash',
                    'JSON': 'json',
                    'YAML': 'yaml',
                    'XML': 'xml'
                }
                detected_lang = lang_map.get(text_content.upper(), text_content.lower())
                if next_sibling.name == 'pre':
                    return element_to_markdown(next_sibling, depth, context={'language': detected_lang})
                elif next_sibling.name == 'figure':
                    return element_to_markdown(next_sibling, depth, context={'language': detected_lang})
                return ''
        
        content = ''.join(element_to_markdown(child, depth, context) for child in element.children)
        return content
    
    # Default: just get text content
    else:
        content = ''.join(element_to_markdown(child, depth, context) for child in element.children)
        return content


def extract_page_content(url):
    """Extract content from a Tailwind CSS documentation page"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the main content div
        content_div = soup.find('div', class_='px-4 pt-10 pb-24 sm:px-6 xl:pr-0')
        
        if not content_div:
            # Try alternative selectors
            content_div = soup.find('div', class_=re.compile(r'px-4.*pt-10.*pb-24'))
        
        if not content_div:
            print(f"Could not find content div for {url}")
            return None
        
        # Convert to markdown
        markdown_content = element_to_markdown(content_div)
        
        # Clean up excessive newlines
        markdown_content = re.sub(r'\n{4,}', '\n\n\n', markdown_content)
        markdown_content = re.sub(r'^\n+', '', markdown_content)
        markdown_content = re.sub(r'\n+$', '\n', markdown_content)
        
        return markdown_content
        
    except Exception as e:
        print(f"Error extracting content from {url}: {e}")
        return None


def save_to_markdown(content, filename, output_dir="claude-docs/tailwind/core_concepts"):
    """Save content to a Markdown file"""

    # Create output directory if it doesn't exist
    cfg = get_config()
    project_dir = cfg.config_path
    # Ensure output directory exists
    output_dir = project_dir/output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save file
    file_path = output_dir / filename
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path


def main():
    """Main function to extract Tailwind CSS Core concepts documentation"""
    
    print("Extracting Tailwind CSS Core concepts documentation...")
    
    try:
        # Extract navigation links for Core concepts section
        links = extract_navigation_links(target_section="Core concepts")
        
        if not links:
            print("No Core concepts links found.")
            return
        
        print(f"Found {len(links)} Core concepts pages")
        
        # Extract content from each page
        successful = 0
        
        for link in tqdm(links, desc="Extracting pages", unit=" page"):
            # Add delay to be respectful to the server
            time.sleep(0.5)
            
            # Extract page content
            content = extract_page_content(link['url'])
            
            if content:
                # Save to file
                file_path = save_to_markdown(content, link['filename'])
                successful += 1
                tqdm.write(f"  ✓ {link['text']} -> {link['filename']}")
            else:
                tqdm.write(f"  ✗ {link['text']} - Failed to extract content")
        
        print(f"\nSummary:")
        print(f"- Total pages: {len(links)}")
        print(f"- Successfully extracted: {successful}")
        print(f"- Failed: {len(links) - successful}")
        
    except requests.RequestException as e:
        print(f"Error fetching pages: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()