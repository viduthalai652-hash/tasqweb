import os

logo_html = '''<a href="index.html" class="nav-logo">
      <img src="assets/images/logo.jpg" alt="TASQ Logo" class="nav-logo-img">
    </a>'''

html_files = ['index.html', 'features.html', 'pricing.html', 'contact.html']

for fname in html_files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # insert right after <div class="nav-container">
    if '<div class="nav-container">' in content:
        updated = content.replace('<div class="nav-container">', f'<div class="nav-container">\n    {logo_html}')
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"  Updated: {fname}")
    else:
        print(f"  WARNING: nav-container not found in {fname}")

print("Done!")
