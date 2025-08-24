import json
import sys
import os
import re

# README: call from terminal in directory. Pass file in same dir as argument.
# Usage: python md_to_json.py input.md output.json

def parse_table(lines, start_index):
    """Parse a Markdown table into headers, rows, and alignments."""
    headers = [h.strip() for h in lines[start_index].split("|")[1:-1]]
    alignments = []
    rows = []
    
    # Parse alignment row
    if start_index + 1 < len(lines) and lines[start_index + 1].strip().startswith("|"):
        align_row = lines[start_index + 1].split("|")[1:-1]
        for align in align_row:
            align = align.strip()
            if align.startswith(":") and align.endswith(":"):
                alignments.append("center")
            elif align.endswith(":"):
                alignments.append("right")
            else:
                alignments.append("left")
    else:
        alignments = ["left"] * len(headers)
    
    # Parse data rows
    i = start_index + 2
    while i < len(lines) and lines[i].strip().startswith("|"):
        row_data = [d.strip() for d in lines[i].split("|")[1:-1]]
        row_dict = {}
        for j in range(min(len(headers), len(row_data))):
            # Convert prices (e.g., "$1600" to 1600)
            if row_data[j].startswith("$") and row_data[j].lstrip("$").replace(".", "").isdigit():
                row_dict[headers[j]] = float(row_data[j].lstrip("$"))
            else:
                row_dict[headers[j]] = row_data[j]
        rows.append(row_dict)
        i += 1
    
    return {
        "headers": headers,
        "rows": rows,
        "alignments": alignments
    }, i

def clean_empty_fields(data):
    """Remove empty fields from JSON to streamline output."""
    if isinstance(data, dict):
        cleaned = {}
        for key, value in data.items():
            if key == "subsections" and not value:
                continue
            if key in ("items", "links", "tables", "content_blocks") and not value:
                continue
            if key == "text" and value == "":
                continue
            cleaned[key] = clean_empty_fields(value)
            if cleaned[key] or cleaned[key] == {}:
                cleaned[key] = cleaned[key]
        return cleaned
    elif isinstance(data, list):
        return [clean_empty_fields(item) for item in data if item or item == {}]
    return data

def parse_markdown_to_json(md_file):
    if not os.path.exists(md_file):
        raise FileNotFoundError(f"{md_file} does not exist")

    with open(md_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Initialize JSON structure
    result = {"content": {}}
    current_section = result["content"]
    current_key = None
    current_subsection = None
    subsection_stack = []

    # Parse Markdown lines
    lines = text.splitlines()
    i = 0
    heading_counters = {}  # Track heading names for unique keys
    current_level = 0  # Track the current heading level
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("# "):
            # Top-level heading (level 1)
            current_key = line[2:].strip()
            current_section[current_key] = {"content_blocks": [], "items": [], "links": [], "subsections": {}}
            current_subsection = None
            subsection_stack = []
            heading_counters = {}
            current_level = 1
        elif line.startswith("## "):
            # Subsection (level 2)
            if current_key:
                sub_key = line[3:].strip()
                current_section[current_key]["subsections"][sub_key] = {"content_blocks": [], "items": [], "links": [], "subsections": {}}
                current_subsection = current_section[current_key]["subsections"][sub_key]
                subsection_stack = [current_subsection]
                heading_counters = {}
                current_level = 2
            else:
                print(f"Warning: Subsection '{line}' ignored (no parent heading)")
        elif re.match(r"^#{3,6}\s", line):
            # Inline headings (level 3-6)
            if current_key:
                level = len(re.match(r"^#+", line).group(0))
                sub_key = line.lstrip("# ").strip()
                # Determine the parent based on the current level
                if level > current_level:
                    parent = subsection_stack[-1] if subsection_stack else current_section[current_key]
                else:
                    # Go up to the parent at the level below the current heading
                    parent_level = level - 1
                    if parent_level <= 1:
                        parent = current_section[current_key]
                        subsection_stack = []
                    else:
                        subsection_stack = subsection_stack[:parent_level-1]
                        parent = subsection_stack[-1] if subsection_stack else current_section[current_key]
                # Ensure unique key for same-level headings
                heading_counters[sub_key] = heading_counters.get(sub_key, 0) + 1
                unique_sub_key = f"{sub_key}_{heading_counters[sub_key]}" if heading_counters[sub_key] > 1 else sub_key
                parent["subsections"][unique_sub_key] = {"content_blocks": [], "items": [], "links": [], "subsections": {}}
                current_subsection = parent["subsections"][unique_sub_key]
                # Update the stack to reflect the current level
                if level <= len(subsection_stack):
                    subsection_stack = subsection_stack[:level-1] + [current_subsection]
                else:
                    subsection_stack.append(current_subsection)
                current_level = level
            else:
                print(f"Warning: Inline heading '{line}' ignored (no parent heading)")
        elif line.startswith("|"):
            # Table
            try:
                table_data, new_i = parse_table(lines, i)
                if current_subsection:
                    current_subsection["content_blocks"].append({"type": "table", "data": table_data})
                elif current_key:
                    current_section[current_key]["content_blocks"].append({"type": "table", "data": table_data})
                else:
                    print(f"Warning: Table at line {i+1} ignored (no heading)")
                i = new_i - 1
            except Exception as e:
                print(f"Warning: Failed to parse table at line {i+1}: {e}")
        elif line.startswith("- "):
            # List item
            if current_subsection:
                current_subsection["items"].append(line[2:].strip())
            elif current_key:
                current_section[current_key]["items"].append(line[2:].strip())
            else:
                print(f"Warning: List item '{line}' ignored (no heading)")
        elif line and re.match(r"\[.*?\]\(.*?\)", line):
            # Inline link
            link_match = re.match(r"\[(.*?)\]\((.*?)\)", line)
            link_data = {"text": link_match.group(1), "url": link_match.group(2)}
            if current_subsection:
                current_subsection["links"].append(link_data)
            elif current_key:
                current_section[current_key]["links"].append(link_data)
            else:
                print(f"Warning: Link '{line}' ignored (no heading)")
        elif line:
            # Paragraph
            if current_subsection:
                current_subsection["content_blocks"].append({"type": "text", "data": line})
            elif current_key:
                current_section[current_key]["content_blocks"].append({"type": "text", "data": line})
            else:
                print(f"Warning: Paragraph '{line}' ignored (no heading)")
        i += 1

    # Clean empty fields
    return clean_empty_fields(result)

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.md"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.json"
    
    try:
        json_data = parse_markdown_to_json(input_file)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2)
        print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error: {e}")