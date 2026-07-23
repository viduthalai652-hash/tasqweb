import os

# 1. Fix literal \n in index.html and features.html safely
for filename in ['index.html', 'features.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace literal \n with an actual newline
    content = content.replace('\\n', '\n')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update CSS for background images on cards
with open('css/components.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add a style for the pricing-card-header to support background images
# We'll use CSS inline styles on the HTML for the specific image, but we need the header to be relative and have a dark/light overlay.
header_css = '''.pricing-card-header {
  padding: 2rem;
  text-align: center;
  border-bottom: 1px solid rgba(0,0,0,0.08);
  background: var(--color-white-warm);
  position: relative;
  overflow: hidden;
}

/* Optional overlay if we use background images directly on the header */
.pricing-card-header::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(to bottom, rgba(255,255,255,0.7), rgba(255,255,255,0.95));
  z-index: 1;
}

.pricing-card-title, .pricing-card-desc {
  position: relative;
  z-index: 2;
}
'''
if '.pricing-card-header {' in css_content:
    # Very crude replacement
    import re
    css_content = re.sub(r'\.pricing-card-header\s*\{[^}]*\}', header_css, css_content, count=1)
    # Ensure z-index on title/desc is added
    if '.pricing-card-title, .pricing-card-desc {' not in css_content:
        css_content += '\n.pricing-card-title, .pricing-card-desc {\n  position: relative;\n  z-index: 2;\n}\n'
    
    with open('css/components.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

# 3. Also the background image for the Our Services section
with open('css/home.css', 'r', encoding='utf-8') as f:
    home_css = f.read()

new_services = '''.services-section {
  padding: var(--space-24) 0;
  background: linear-gradient(rgba(10, 20, 35, 0.8), rgba(10, 20, 35, 0.9)), url('../assets/images/hero_dashboard.jpg') center/cover no-repeat fixed;
  position: relative;
}

.services-section .section-label {
  color: var(--color-orange);
}

.services-section .section-heading,
.services-section .section-subheading {
  color: white;
}
'''

if '.services-section {' in home_css:
    home_css = re.sub(r'\.services-section\s*\{[^}]*\}', new_services, home_css, count=1)
    with open('css/home.css', 'w', encoding='utf-8') as f:
        f.write(home_css)

print("Fixed newlines and updated CSS for backgrounds.")
