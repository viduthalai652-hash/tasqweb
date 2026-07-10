import re
import os

def remove_shapes(content):
    content = re.sub(r'<div class="particles-container">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="floating-shapes">.*?</div>', '', content, flags=re.DOTALL)
    # Contact hero doesn't have floating-shapes but has particles-container
    return content

# 1. index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()
idx = remove_shapes(idx)
idx = re.sub(r'<!-- ACHIEVEMENTS -->.*?<section class="achievements-section" id="achievements">.*?</section>', '', idx, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# 2. features.html
with open('features.html', 'r', encoding='utf-8') as f:
    feat = f.read()
feat = remove_shapes(feat)
feat = re.sub(r'<!-- Overview -->.*?<section class="overview-section">.*?</section>', '', feat, flags=re.DOTALL)
with open('features.html', 'w', encoding='utf-8') as f:
    f.write(feat)

# 3. pricing.html
with open('pricing.html', 'r', encoding='utf-8') as f:
    price = f.read()
price = remove_shapes(price)
with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(price)

# 4. contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    contact = f.read()
contact = remove_shapes(contact)

map_html = """
        <div class="contact-map" style="margin-top:2rem; border-radius:var(--radius-lg); overflow:hidden; border:1px solid rgba(255,106,0,0.1);">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.0673418501257!2d-122.3956891!3d37.7932646!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858066f1228e93%3A0x6e76cf0ba749b563!2sFerry%20Building!5e0!3m2!1sen!2sus!4v1700000000000!5m2!1sen!2sus" width="100%" height="250" style="border:0; display:block;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
"""
contact = contact.replace('</div>\n      \n      <!-- Contact Form -->', map_html + '\n      <!-- Contact Form -->')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact)

# 5. css/contact.css
with open('css/contact.css', 'r', encoding='utf-8') as f:
    contact_css = f.read()

contact_css = contact_css.replace('background: var(--color-black);', 'background: var(--color-white);')
contact_css = contact_css.replace('color: white;\n  letter-spacing', 'color: var(--color-black);\n  letter-spacing')
contact_css = contact_css.replace('color: rgba(255,255,255,0.7);', 'color: #555;')
contact_css = contact_css.replace('grid-template-columns: 1fr 1.6fr;', 'grid-template-columns: 1fr 1fr;')

with open('css/contact.css', 'w', encoding='utf-8') as f:
    f.write(contact_css)

print("Cleanup complete.")
