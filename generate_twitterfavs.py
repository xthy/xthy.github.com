import re
import os

source_file = '/Users/thy/Documents/xthy.github.com/twitter_likes_archivlyx.md'
target_dir = '/Users/thy/Documents/xthy.github.com/_posts/'

with open(source_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Split blocks by '---'
# The first few might be header stuff
blocks = text.split('\n---\n')

years_data = {
    2020: [],
    2021: [],
    2022: [],
    2023: [],
    2024: [],
    2025: []
}

def parse_date(date_str):
    date_str = date_str.lower().strip()
    if 'month' in date_str:
        return 2025
    elif 'a year ago' in date_str or '1 year' in date_str:
        return 2024
    elif '2 years' in date_str:
        return 2023
    elif '3 years' in date_str:
        return 2022
    elif '4 years' in date_str:
        return 2021
    elif '5 years' in date_str:
        return 2020
    return None

import urllib.parse
# Regex to find urls. We want to find http or https
url_regex = re.compile(r'(https?://[^\s]+)')

for block in blocks:
    if not block.strip():
        continue
    
    # Check if it's a post block
    uname_match = re.search(r'## \d+\. @([a-zA-Z0-9_]+)', block)
    if not uname_match:
        continue
    username = uname_match.group(1)
    
    date_match = re.search(r'\*\*날짜:\*\* (.*)', block)
    if not date_match:
        continue
    date_str = date_match.group(1).strip()
    
    year = parse_date(date_str)
    if year not in years_data:
        continue
        
    # Extract content
    # content is usually between the date line and the link line or end of block
    content_lines = []
    lines = block.split('\n')
    capture = False
    for line in lines:
        if line.startswith('**날짜:**'):
            capture = True
            continue
        if line.startswith('**링크:**'):
            capture = False
            break
        if capture:
            content_lines.append(line)
            
    content = '\n'.join(content_lines).strip()
    
    # We want to format the URLs in the content
    # "https://t.co/..." -> "[https://t.co/...](https://t.co/...){:target="_blank"}"
    def replace_url(match):
        u = match.group(1)
        # some tweets end with "..." attached to url, handle safely. 
        # But actually let's just use the url directly.
        return f'[{u}]({u}){{:target="_blank"}}'
    
    # wait, if it's already markdown formatted, we might double format it.
    # The raw markdown seems to just have plaintext URLs.
    content = url_regex.sub(replace_url, content)
    
    # some lines might be empty, that's fine.
    
    formatted_post = ""
    if content:
        formatted_post += content + "\n"
    formatted_post += f"<br>User Name:  {username} <br><br>\n"
    
    years_data[year].append(formatted_post)

for year, posts in years_data.items():
    filename = os.path.join(target_dir, f"{year}-12-31-Twitterfavs.md")
    content_str = f"""---
layout: post
title: "Twitter Favorites {year}"
date:   {year+1}-01-01 00:00:00
category: Log
---

"""
    content_str += "\n".join(posts)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content_str)
        
print("Done creating files.")
