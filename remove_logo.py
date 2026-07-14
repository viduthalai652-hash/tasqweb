import os
import re

html_files = ['index.html', 'features.html', 'pricing.html', 'contact.html']

for fname in html_files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # The regex targets the entire <a class="nav-logo">...</a> block
    # Note: re.DOTALL ensures '.' matches newlines as well
    updated = re.sub(r'<a href="index\.html" class="nav-logo".*?</a>', '', content, flags=re.DOTALL)
    
    if updated == content:
        print(f"  WARNING: nav-logo not found in {fname}")
    else:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"  Updated: {fname}")

print("Done!")
