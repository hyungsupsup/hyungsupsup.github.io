
import os
import re
import glob

# 1. Update Posts
posts_dir = os.path.join(os.getcwd(), '_posts')
files = glob.glob(os.path.join(posts_dir, '*.md'))

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(file_path)
    
    # Update categories to skills (except the welcome post)
    if 'welcome-paper-reviews' not in filename:
        if re.search(r'^categories:', content, re.MULTILINE):
            content = re.sub(r'^categories:.*$', 'categories: skills', content, flags=re.MULTILINE)
        else:
            content = re.sub(r'(date:.*$)', r'\1\ncategories: skills', content, flags=re.MULTILINE)
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Rename welcome post
old_name = os.path.join(posts_dir, '2026-01-15-welcome-paper-reviews.md')
new_name = os.path.join(posts_dir, '2024-01-15-welcome-paper-reviews.md')

if os.path.exists(old_name):
    try:
        os.rename(old_name, new_name)
    except FileExistsError:
        pass # Already renamed
    
    # Update date inside
    with open(new_name, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'date: 2026-.*$', 'date: 2024-01-15 00:00:00', content, flags=re.MULTILINE)
    with open(new_name, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update _config.yml (Disable imagemagick)
config_path = os.path.join(os.getcwd(), '_config.yml')
with open(config_path, 'r', encoding='utf-8') as f:
    config_content = f.read()

# Replace enabled: true with enabled: false specifically for imagemagick block
# We look for "imagemagick:\n  enabled: true"
config_content = config_content.replace(
    'imagemagick:\n  enabled: true', 
    'imagemagick:\n  enabled: false'
)

with open(config_path, 'w', encoding='utf-8') as f:
    f.write(config_content)
print("Updated completed.")
