import glob
import re

new_footer_links = '''<div class="footer-links">
        <div class="footer-col">
          <h4>Services</h4>
          <a href="features.html">Instagram Automation</a>
          <a href="features.html">WhatsApp Leads</a>
          <a href="features.html">GMB Automation</a>
          <a href="features.html">Appointments</a>
        </div>
        <div class="footer-col">
          <h4>More Services</h4>
          <a href="features.html">Social Media Posting</a>
          <a href="features.html">CRM Setup</a>
          <a href="features.html">Invoice Automation</a>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <a href="features.html">Features & Services</a>
          <a href="pricing.html">Pricing</a>
          <a href="contact.html">Contact</a>
        </div>
      </div>'''

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the block from <div class="footer-links"> to its closing </div>
    # A bit tricky with regex, we can find <div class="footer-links"> and the next </div> that matches its level.
    # But we can just use a simple string replacement if we extract it first.
    
    match = re.search(r'<div class="footer-links">.*?</div>\s*</div>\s*</div>\s*<div class="footer-bottom">', content, re.DOTALL)
    if match:
        old_links = re.search(r'<div class="footer-links">.*?(?=</div>\s*</div>\s*<div class="footer-bottom">)', content, re.DOTALL)
        if old_links:
            # We need to be careful not to consume the closing tags of the footer-top
            # Actually, the footer structure is:
            # <div class="footer-top">
            #   <div class="footer-brand">...</div>
            #   <div class="footer-links">...</div>
            # </div>
            # <div class="footer-bottom">...</div>
            #
            # Let's replace the whole footer-links block
            start_tag = '<div class="footer-links">'
            start_idx = content.find(start_tag)
            
            if start_idx != -1:
                # Find the footer-bottom to bound the search
                bottom_idx = content.find('<div class="footer-bottom">', start_idx)
                if bottom_idx != -1:
                    # We want to replace everything from <div class="footer-links"> up to the </div> that closes it (which is right before </div> closing footer-top)
                    # Let's just use regex to replace between <div class="footer-links"> and the </div> immediately preceding <div class="footer-bottom">
                    
                    # A safer way is to just replace the whole footer-top
                    pass

    # Let's just do a manual replace using the exact known string from index.html (with some whitespace tolerance)
    # Actually, all files probably have the exact same footer structure right now. Let's just replace the exact string if we can.
    
    # Better approach:
    content = re.sub(r'<div class="footer-links">[\s\S]*?(?=</div>\s*</div>\s*<div class="footer-bottom">)', new_footer_links, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated footer in {filepath}")
