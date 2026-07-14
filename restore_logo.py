import os

# Old img-based logo
old_logo = '''<a href="index.html" class="nav-logo">
      <img src="assets/images/tasq_logo.svg" alt="TASQ Logo" class="nav-logo-img">
    </a>'''

# New HTML/CSS logo (uses Baloo 2 web font already loaded on page)
new_logo = '''<a href="index.html" class="nav-logo">
      <span class="logo-wrap">
        <span class="logo-wordmark"><span class="logo-tas">TAS</span><span class="logo-q">Q</span></span>
        <span class="logo-tagline">All in One Marketing CRM</span>
      </span>
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
