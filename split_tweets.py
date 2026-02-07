import os
import re

def process_twitter_likes():
    input_file = '/Users/thy/Documents/xthy.github.com/twitter_likes_archivlyx.md'
    output_dir = '/Users/thy/Documents/xthy.github.com/_posts'
    
    if not os.path.exists(input_file):
        print("Input file not found")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by '---' separator
    posts = content.split('---')
    
    # Year mapping based on "X years ago" from Feb 2026
    # 5 years ago -> 2021
    # 4 years ago -> 2022
    # 3 years ago -> 2023
    # 2 years ago -> 2024
    # a year ago / 1 year ago -> 2025
    
    year_data = {
        2021: [],
        2022: [],
        2023: [],
        2024: [],
        2025: []
    }

    for post in posts:
        # Extract ID and Name: ## 1. @id (name)
        header_match = re.search(r'## \d+\. @(\w+) \((.*?)\)', post)
        if not header_match:
            continue
            
        user_id = header_match.group(1)
        user_name = header_match.group(2)
        
        # Extract Date: **날짜:** ...
        date_match = re.search(r'\*\*날짜:\*\* (.*)', post)
        if not date_match:
            continue
            
        date_str = date_match.group(1).strip()
        
        target_year = None
        if '5 years ago' in date_str: target_year = 2021
        elif '4 years ago' in date_str: target_year = 2022
        elif '3 years ago' in date_str: target_year = 2023
        elif '2 years ago' in date_str: target_year = 2024
        elif 'a year ago' in date_str or '1 year ago' in date_str: target_year = 2025
        
        if not target_year:
            continue
            
        # Extract content: between date and '---' or end of post
        # The structure is:
        # ## ...
        # **날짜:** ...
        # [CONTENT]
        # **링크:** ... (optional)
        
        # Find start of content (after the date line)
        content_lines = post.split('\n')
        start_idx = -1
        for i, line in enumerate(content_lines):
            if '**날짜:**' in line:
                start_idx = i + 1
                break
        
        if start_idx == -1:
            continue
            
        body = '\n'.join(content_lines[start_idx:]).strip()
        # Remove "링크: ..." if present
        body = re.sub(r'\*\*링크:\*\* .*', '', body).strip()
        
        formatted_post = f"{body}\n<br>User Name:  {user_id}\n<br>DateTime: {target_year-2000}-12-31 00:00:00 <br><br>"
        year_data[target_year].append(formatted_post)

    for year, logs in year_data.items():
        if not logs:
            continue
            
        filename = f"{year}-12-31-Twitterfavs.md"
        filepath = os.path.join(output_dir, filename)
        
        # YAML Frontmatter
        # For 2021-12-31, the date in frontmatter can be slightly ahead like in the example
        # Example 2020 file has: date: 2021-02-14 01:20:30
        # We'll use [Year+1]-01-01 for consistency
        yaml_date = f"{year+1}-01-01 00:00:00"
        
        file_content = f"""---
layout: post
title: "Twitter Favorites {year}"
date:   {yaml_date}
category: Log
---

"""
        # Join logs in reverse order (assuming original was newest first, and we want newest at top)
        file_content += '\n\n'.join(logs)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content)
        print(f"Created {filepath} with {len(logs)} posts.")

if __name__ == "__main__":
    process_twitter_likes()
