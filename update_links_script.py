import re

service_keys = [
    ("Instagram Automation Packs", "instagram"),
    ("WhatsApp Lead Automation", "whatsapp"),
    ("Google My Business Automation", "gmb"),
    ("Appointment Booking System", "appointment"),
    ("Social Media Auto Posting", "social"),
    ("CRM Setup (Basic)", "crm"),
    ("Invoice & Payment Automation", "invoice")
]

# Update update_features_showcase.py and re-run it
with open('update_card_backgrounds.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace href="contact.html" with href="pricing.html?service={service['key']}" in the generator script
# First add 'key' to service objects
code_new = code.replace('"name": "Instagram Automation Packs",', '"key": "instagram",\n        "name": "Instagram Automation Packs",')
code_new = code_new.replace('"name": "WhatsApp Lead Automation",', '"key": "whatsapp",\n        "name": "WhatsApp Lead Automation",')
code_new = code_new.replace('"name": "Google My Business Automation",', '"key": "gmb",\n        "name": "Google My Business Automation",')
code_new = code_new.replace('"name": "Appointment Booking System",', '"key": "appointment",\n        "name": "Appointment Booking System",')
code_new = code_new.replace('"name": "Social Media Auto Posting",', '"key": "social",\n        "name": "Social Media Auto Posting",')
code_new = code_new.replace('"name": "CRM Setup (Basic)",', '"key": "crm",\n        "name": "CRM Setup (Basic)",')
code_new = code_new.replace('"name": "Invoice & Payment Automation",', '"key": "invoice",\n        "name": "Invoice & Payment Automation",')

code_new = code_new.replace('href="contact.html"', 'href="pricing.html?service={service[\'key\']}"')

with open('update_card_backgrounds.py', 'w', encoding='utf-8') as f:
    f.write(code_new)

print("Updated update_card_backgrounds.py script")
