import re

with open('features.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make overview benefits column layout to support images on top
overview_replacements = {
    '<span class="overview-benefit-icon">📈</span>': '<div style="width:100%;height:140px;border-radius:var(--radius-md);overflow:hidden;margin-bottom:1rem;"><img src="assets/images/crm_dashboard.jpg" style="width:100%;height:100%;object-fit:cover;"></div>',
    '<span class="overview-benefit-icon">🤖</span>': '<div style="width:100%;height:140px;border-radius:var(--radius-md);overflow:hidden;margin-bottom:1rem;"><img src="assets/images/ai_bot_dashboard.jpg" style="width:100%;height:100%;object-fit:cover;"></div>',
    '<span class="overview-benefit-icon">🏢</span>': '<div style="width:100%;height:140px;border-radius:var(--radius-md);overflow:hidden;margin-bottom:1rem;"><img src="assets/images/funnel_dashboard.jpg" style="width:100%;height:100%;object-fit:cover;"></div>',
    '<span class="overview-benefit-icon">👥</span>': '<div style="width:100%;height:140px;border-radius:var(--radius-md);overflow:hidden;margin-bottom:1rem;"><img src="assets/images/social_dashboard.jpg" style="width:100%;height:100%;object-fit:cover;"></div>',
    '<span class="overview-benefit-icon">📊</span>': '<div style="width:100%;height:140px;border-radius:var(--radius-md);overflow:hidden;margin-bottom:1rem;"><img src="assets/images/crm_dashboard.jpg" style="width:100%;height:100%;object-fit:cover;filter:hue-rotate(80deg);"></div>',
    '<span class="overview-benefit-icon">🔗</span>': '<div style="width:100%;height:140px;border-radius:var(--radius-md);overflow:hidden;margin-bottom:1rem;"><img src="assets/images/social_dashboard.jpg" style="width:100%;height:100%;object-fit:cover;filter:hue-rotate(270deg);"></div>'
}

for old, new in overview_replacements.items():
    content = content.replace(old, new)

# Change .overview-benefit inline style to flex-direction column if needed, but it's easier to just use CSS or inject style
content = content.replace('class="overview-benefit reveal', 'class="overview-benefit reveal" style="flex-direction:column; gap:0; padding:1rem;"')
content = content.replace('<div class="overview-benefit reveal" style="flex-direction:column; gap:0; padding:1rem;" reveal-delay', '<div class="overview-benefit reveal reveal-delay') # Fix potential double spacing
content = re.sub(r'class="overview-benefit reveal reveal-delay-(\d+)"', r'class="overview-benefit reveal reveal-delay-\1" style="flex-direction:column; gap:0; padding:1rem;"', content)


with open('features.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated features.html")
