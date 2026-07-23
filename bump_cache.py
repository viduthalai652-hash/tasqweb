import re

files = ['index.html', 'features.html', 'pricing.html']
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Bump base.css cache string
    content = re.sub(r'base\.css\?v=\d+', 'base.css?v=20', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Cache versions bumped.")
