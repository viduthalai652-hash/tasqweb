import re

# Read features.html
with open('features.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the CSS link
if 'css/features-stack.css' not in content:
    content = content.replace('<link rel="stylesheet" href="css/features.css">', '<link rel="stylesheet" href="css/features.css">\n  <link rel="stylesheet" href="css/features-stack.css">')

# Read generated features-stack
with open('features_stack.html', 'r', encoding='utf-8') as f:
    stack_content = f.read()

# Replace the .features-grid with the new stack
pattern = r'<div class="features-grid">.*?</div>\s+</div>\s+</section>'
replacement = stack_content + '\n  </div>\n</section>'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('features.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated features.html")
