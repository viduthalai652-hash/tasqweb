import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the cards
match = re.search(r'<div class="services-grid">(.*?)</div>\s*</div>\s*</section>', content, re.DOTALL)
if match:
    cards_html = match.group(1).strip()
    
    # We want to remove the 'reveal' classes from cards in the marquee since they will scroll in immediately.
    # We'll just leave the class as "service-card".
    clean_cards_html = re.sub(r'reveal reveal-delay-\d+', '', cards_html).replace('class="service-card "', 'class="service-card"')

    marquee_html = f'''<div class="services-marquee-wrapper reveal">
      <div class="services-marquee-track">
        {clean_cards_html}
        <!-- Duplicate for infinite scroll loop -->
        {clean_cards_html}
      </div>
    </div>'''

    new_content = content[:match.start()] + marquee_html + '\n  </div>\n</section>' + content[match.end():]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated index.html to use marquee wrapper!")
else:
    print("Could not find services-grid block.")
