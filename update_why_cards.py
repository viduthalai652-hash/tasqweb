import re

with open('features.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'<div class="why-card reveal reveal-delay-1">', '<div class="why-card why-card-bg reveal reveal-delay-1" style="background-image: url(\'assets/images/crm_dashboard.jpg\');">'),
    (r'<div class="why-card reveal reveal-delay-2">', '<div class="why-card why-card-bg reveal reveal-delay-2" style="background-image: url(\'assets/images/ai_bot_dashboard.jpg\');">'),
    (r'<div class="why-card reveal reveal-delay-3">', '<div class="why-card why-card-bg reveal reveal-delay-3" style="background-image: url(\'assets/images/social_dashboard.jpg\');">'),
    (r'<div class="why-card reveal reveal-delay-4">', '<div class="why-card why-card-bg reveal reveal-delay-4" style="background-image: url(\'assets/images/marketing_dashboard.jpg\');">'),
    (r'<div class="why-card reveal reveal-delay-5">', '<div class="why-card why-card-bg reveal reveal-delay-5" style="background-image: url(\'assets/images/funnel_dashboard.jpg\');">'),
    (r'<div class="why-card reveal reveal-delay-6">', '<div class="why-card why-card-bg reveal reveal-delay-6" style="background-image: url(\'assets/images/crm_dashboard.jpg\');">')
]

for old, new in replacements:
    content = content.replace(old, new)

with open('features.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated features.html with background images")
