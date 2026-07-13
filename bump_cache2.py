with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('css/home.css?v=2"', 'css/home.css?v=3"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
