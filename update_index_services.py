import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove features-preview section
pattern_features = r'<!-- FEATURES PREVIEW -->\s*<section class="features-preview" id="features">.*?</section>'
content = re.sub(pattern_features, '', content, flags=re.DOTALL)

# 2. Update services section images
service_replacements = {
    '<div class="service-card-img">🏆</div>': '<div class="service-card-img"><img src="assets/images/crm_dashboard.jpg" alt="CRM" style="width:100%;height:100%;object-fit:cover;"></div>',
    '<div class="service-card-img">⚡</div>': '<div class="service-card-img"><img src="assets/images/marketing_dashboard.jpg" alt="Marketing" style="width:100%;height:100%;object-fit:cover;"></div>',
    '<div class="service-card-img">🤖</div>': '<div class="service-card-img"><img src="assets/images/ai_bot_dashboard.jpg" alt="AI Bot" style="width:100%;height:100%;object-fit:cover;"></div>',
    '<div class="service-card-img">🎯</div>': '<div class="service-card-img"><img src="assets/images/funnel_dashboard.jpg" alt="Funnel Builder" style="width:100%;height:100%;object-fit:cover;"></div>',
    '<div class="service-card-img">📊</div>': '<div class="service-card-img"><img src="assets/images/crm_dashboard.jpg" alt="Analytics" style="width:100%;height:100%;object-fit:cover;filter:hue-rotate(80deg);"></div>',
    '<div class="service-card-img">🔗</div>': '<div class="service-card-img"><img src="assets/images/social_dashboard.jpg" alt="Integrations" style="width:100%;height:100%;object-fit:cover;filter:hue-rotate(270deg);"></div>'
}

for old, new in service_replacements.items():
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
