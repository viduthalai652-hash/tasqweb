import os

# New img-based logo pointing to logo.png
new_logo = '''<a href="index.html" class="nav-logo">
      <img src="assets/images/logo.png" alt="TASQ Logo" class="nav-logo-img">
    </a>'''

# The inline SVG logo currently in the files
old_logo = '''<a href="index.html" class="nav-logo" style="text-decoration:none;display:flex;align-items:center;">
      <svg viewBox="0 0 310 68" height="52" width="auto" xmlns="http://www.w3.org/2000/svg" style="display:block;overflow:visible;">
        <defs>
          <linearGradient id="qGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFB300"/>
            <stop offset="100%" stop-color="#FF5200"/>
          </linearGradient>
        </defs>
        <text x="0" y="48"
          font-family="'Baloo 2', 'Nunito', 'Arial Rounded MT Bold', Arial, sans-serif"
          font-weight="800" font-size="54" fill="#2B1200" letter-spacing="-2">TAS</text>
        <text x="187" y="48"
          font-family="'Baloo 2', 'Nunito', 'Arial Rounded MT Bold', Arial, sans-serif"
          font-weight="800" font-size="54" fill="url(#qGradient)" letter-spacing="-2">Q</text>
        <text x="1" y="64"
          font-family="'Nunito', Arial, sans-serif"
          font-weight="600" font-size="11.5" fill="#1B3A6E" letter-spacing="0.8">All in One Marketing CRM</text>
      </svg>
    </a>'''

html_files = ['index.html', 'features.html', 'pricing.html', 'contact.html']

for fname in html_files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    updated = content.replace(old_logo, new_logo)
    
    if updated == content:
        print(f"  WARNING: logo pattern not found in {fname}")
    else:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"  Updated: {fname}")

print("Done!")
