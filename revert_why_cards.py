import re

with open('features.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove why-card-bg class and the inline style attribute
content = re.sub(r'why-card-bg\s+', '', content)
content = re.sub(r'\s*style="background-image:\s*url\([^)]+\);"', '', content)

with open('features.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted Why TASQ cards to plain background")
