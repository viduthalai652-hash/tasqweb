import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the CSS link
if 'css/features-stack.css' not in content:
    content = content.replace('<link rel="stylesheet" href="css/home.css">', '<link rel="stylesheet" href="css/home.css">\n  <link rel="stylesheet" href="css/features-stack.css">')

# Extract the first 6 features from features_stack.html
with open('features_stack.html', 'r', encoding='utf-8') as f:
    stack_content = f.read()

# Split the stack content by '<div class="feature-stack-block reveal">'
blocks = stack_content.split('<div class="feature-stack-block reveal">')
# First item is '<div class="features-stack">\n      '
new_stack_content = blocks[0] + '<div class="feature-stack-block reveal">'.join(blocks[1:7]) + '\n</div>\n'

# Replace the .features-preview-grid with the new stack
pattern = r'<div class="features-preview-grid">.*?</div>\s+<div class="features-preview-cta reveal">'
replacement = new_stack_content + '    <div class="features-preview-cta reveal">'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
