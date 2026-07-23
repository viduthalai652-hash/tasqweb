import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('body style="background:#080A14;"', 'body')
content = re.sub(r'pricing\.css\?v=\d+', 'pricing.css?v=17', content)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)
