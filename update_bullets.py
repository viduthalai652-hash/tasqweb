import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the span with emojis
content = re.sub(r'<span class="about-bullet-icon">.*?</span>', '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed emojis from index.html")

# Now update home.css to make the bullet point a circle
with open('css/home.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    '''.about-bullet::before {
  content: '';
  width: 20px;
  height: 20px;
  background: var(--gradient-orange);
  border-radius: var(--radius-sm);''',
    '''.about-bullet::before {
  content: '';
  width: 12px;
  height: 12px;
  background: var(--gradient-orange);
  border-radius: 50%;'''
)

# Remove .about-bullet-icon styles as they are no longer needed
css = re.sub(r'\.about-bullet-icon\s*\{[^}]*\}', '', css)

with open('css/home.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated home.css bullet point styles")
