import re

with open('css/components.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Restore original pricing-card-header
original_header = '''.pricing-card-header {
  padding: 2rem;
  text-align: center;
  border-bottom: 1px solid rgba(0,0,0,0.08);
  background: var(--color-white-warm);
}'''

# Replace whatever the current header is
css_content = re.sub(r'\.pricing-card-header\s*\{[^}]*\}(\s*/\*.*?\*/)?(\s*\.pricing-card-header::before\s*\{[^}]*\})?', original_header, css_content, count=1, flags=re.DOTALL)

# Remove the title/desc z-index I added previously
css_content = re.sub(r'\.pricing-card-title,\s*\.pricing-card-desc\s*\{[^}]*\}', '', css_content, count=1)

# Add pricing-card-img
img_css = '''
.pricing-card-img {
  width: 100%;
  height: 170px;
  background: linear-gradient(135deg, rgba(255,106,0,0.08), rgba(255,140,26,0.04));
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.pricing-card-img::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--gradient-orange);
  opacity: 0;
  transition: opacity var(--transition-slow);
}

.pricing-card:hover .pricing-card-img::after {
  opacity: 0.15;
}
'''
if '.pricing-card-img {' not in css_content:
    css_content += img_css

with open('css/components.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated components.css")
