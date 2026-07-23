import re

with open('css/pricing.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .pricing-hero
css = re.sub(r'\.pricing-hero \{\s*background: #[0-9A-Fa-f]+;', '.pricing-hero {\n  background: var(--color-white-warm);', css)
css = re.sub(r'\.pricing-hero h1 \{\s*(.*?)\s*color: white;', r'.pricing-hero h1 {\n  \1\n  color: var(--color-black);', css, flags=re.DOTALL)
css = re.sub(r'\.pricing-hero-desc \{\s*(.*?)\s*color: rgba\(255, 255, 255, 0\.7\);', r'.pricing-hero-desc {\n  \1\n  color: #555;', css, flags=re.DOTALL)

# Update service tabs for light background
css = re.sub(r'\.service-tab-bar \{\s*(.*?)\s*background: rgba\(255, 255, 255, 0\.04\);\s*(.*?)\s*border: 1px solid rgba\(255, 255, 255, 0\.08\);', 
             r'.service-tab-bar {\n  \1\n  background: white;\n  \2\n  border: 1px solid rgba(0,0,0,0.08);', css, flags=re.DOTALL)
css = re.sub(r'\.service-tab-btn \{\s*(.*?)\s*color: rgba\(255, 255, 255, 0\.7\);', r'.service-tab-btn {\n  \1\n  color: #555;', css, flags=re.DOTALL)
css = re.sub(r'\.service-tab-btn:hover \{\s*color: white;\s*background: rgba\(255, 255, 255, 0\.08\);', 
             r'.service-tab-btn:hover {\n  color: var(--color-black);\n  background: rgba(0,0,0,0.04);', css)

# Update pricing section background
css = re.sub(r'\.pricing-section \{\s*(.*?)\s*background: #[0-9A-Fa-f]+;', r'.pricing-section {\n  \1\n  background: var(--color-white-warm);', css, flags=re.DOTALL)

# Update pricing overview section
css = re.sub(r'\.pricing-overview-section \{\s*(.*?)\s*background: #[0-9A-Fa-f]+;\s*(.*?)\s*border-top: 1px solid rgba\(255, 255, 255, 0\.05\);', 
             r'.pricing-overview-section {\n  \1\n  background: var(--color-white);\n  \2\n  border-top: 1px solid rgba(0,0,0,0.08);', css, flags=re.DOTALL)
css = re.sub(r'\.pricing-overview-title \{\s*(.*?)\s*color: white;', r'.pricing-overview-title {\n  \1\n  color: var(--color-black);', css, flags=re.DOTALL)

css = re.sub(r'\.pricing-table-wrapper \{\s*(.*?)\s*border: 1px solid rgba\(255, 255, 255, 0\.08\);\s*(.*?)\s*background: #[0-9A-Fa-f]+;', 
             r'.pricing-table-wrapper {\n  \1\n  border: 1px solid rgba(0,0,0,0.08);\n  \2\n  background: white;', css, flags=re.DOTALL)

css = re.sub(r'\.pricing-table th, \.pricing-table td \{\s*(.*?)\s*border-bottom: 1px solid rgba\(255, 255, 255, 0\.06\);\s*(.*?)\s*color: rgba\(255, 255, 255, 0\.85\);', 
             r'.pricing-table th, .pricing-table td {\n  \1\n  border-bottom: 1px solid rgba(0,0,0,0.06);\n  \2\n  color: #444;', css, flags=re.DOTALL)

css = re.sub(r'\.pricing-table th \{\s*(.*?)\s*background: rgba\(255, 255, 255, 0\.03\);', r'.pricing-table th {\n  \1\n  background: rgba(0,0,0,0.02);', css, flags=re.DOTALL)

css = re.sub(r'\.pricing-table td\.service-name-cell \{\s*(.*?)\s*color: white;', r'.pricing-table td.service-name-cell {\n  \1\n  color: var(--color-black);', css, flags=re.DOTALL)

with open('css/pricing.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/pricing.css successfully.")
