import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace contact.html links inside pricing-card-footer with pricing.html?service=...
service_mapping = [
    ("Instagram Automation Packs", "instagram"),
    ("WhatsApp Lead Automation", "whatsapp"),
    ("Google My Business Automation", "gmb"),
    ("Appointment Booking System", "appointment"),
    ("Social Media Auto Posting", "social"),
    ("CRM Setup (Basic)", "crm"),
    ("Invoice & Payment Automation", "invoice")
]

for name, key in service_mapping:
    # Pattern matching card with specific title
    pattern = rf'(<h3 class="pricing-card-title">{re.escape(name)}</h3>[\s\S]*?<div class="pricing-card-footer">\s*<a href=")contact\.html(")'
    content = re.sub(pattern, rf'\1pricing.html?service={key}\2', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html marquee links successfully")
