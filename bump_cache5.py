with open('features.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('css/features-stack.css?v=6"', 'css/features-stack.css?v=7"')

with open('features.html', 'w', encoding='utf-8') as f:
    f.write(content)
