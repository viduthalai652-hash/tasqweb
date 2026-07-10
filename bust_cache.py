import io

def bust_cache(filepath):
    with io.open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add cache buster query param to features-stack.css
    content = content.replace('css/features-stack.css"', 'css/features-stack.css?v=2"')
    
    with io.open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

bust_cache('index.html')
bust_cache('features.html')

print("Busted CSS cache")
