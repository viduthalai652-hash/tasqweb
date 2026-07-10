import io

# Fix broken characters in features.html
with io.open('features.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Replace '???' in buttons with '→'
# Wait, actually let's just replace '???' if it exists
content = content.replace('???', '&#8594;')
# Also remove the hardcoded style="background:#8b5cf6..." because we already added it to features-stack.css
import re
content = re.sub(r'style="background:#8b5cf6;color:white;box-shadow:[^"]*"', 'class="btn btn-primary"', content)
# Wait, the python script generated 'class="btn" style="..."' so we want to change that back to 'class="btn btn-primary"'
content = content.replace('class="btn" class="btn btn-primary"', 'class="btn btn-primary"')

with io.open('features.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Same for index.html
with io.open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('???', '&#8594;')
content = re.sub(r'style="background:#8b5cf6;color:white;box-shadow:[^"]*"', 'class="btn btn-primary"', content)
content = content.replace('class="btn" class="btn btn-primary"', 'class="btn btn-primary"')

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed arrows and styles")
