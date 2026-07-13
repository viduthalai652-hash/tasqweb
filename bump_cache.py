import re

for fname in ['index.html', 'features.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Bump home.css cache
    content = content.replace('css/home.css"', 'css/home.css?v=2"')
    
    # Bump features-stack.css cache
    content = content.replace('css/features-stack.css?v=3"', 'css/features-stack.css?v=4"')
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
