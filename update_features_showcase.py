import re

services_data = [
    {
        "badge": "INSTAGRAM AUTOMATION",
        "name": "Instagram Automation Packs",
        "title": "Automate Engagement & <span>Lead Generation</span>",
        "img": "social_dashboard.jpg",
        "desc": "Automate Instagram engagement by instantly responding to comments, sending direct messages, and nurturing leads through automated follow-up conversations.",
        "plan1": {"name": "Professional Plan", "price": "₹6,000 / 6 Months"},
        "plan2": {"name": "Premium Plan", "price": "₹10,000 / 1 Year"},
        "features": [
            "Comment to DM Automation",
            "Keyword-Based Auto Reply",
            "Automatic Follow-up Messages",
            "Lead Collection through Instagram",
            "Automated Customer Engagement",
            "Promotion & Offer Messaging"
        ]
    },
    {
        "badge": "WHATSAPP AUTOMATION",
        "name": "WhatsApp Lead Automation",
        "title": "Capture & Qualify <span>Leads Instantly</span>",
        "img": "crm_dashboard.jpg",
        "desc": "Automate WhatsApp conversations to capture leads, send instant replies, and follow up with potential customers automatically.",
        "plan1": {"name": "Professional Plan", "price": "₹20,000 / 6 Months"},
        "plan2": {"name": "Premium Plan", "price": "₹35,000 / 1 Year"},
        "features": [
            "Instant Auto Reply",
            "Lead Capture Automation",
            "Automated Follow-up Sequence",
            "Customer Engagement",
            "Faster Lead Qualification",
            "Improved Conversion Process"
        ]
    },
    {
        "badge": "GMB AUTOMATION",
        "name": "Google My Business Automation",
        "title": "Automate Reviews & <span>Local Reputation</span>",
        "img": "marketing_dashboard.jpg",
        "desc": "Increase your business visibility by automating review requests and responding to customer reviews using AI-powered automation.",
        "plan1": {"name": "Professional Plan", "price": "₹5,000 / 6 Months"},
        "plan2": {"name": "Premium Plan", "price": "₹8,000 / 1 Year"},
        "features": [
            "Automated Review Requests",
            "AI Review Replies",
            "Local Business Optimization",
            "Customer Trust Building",
            "Reputation Improvement"
        ]
    },
    {
        "badge": "APPOINTMENT SCHEDULING",
        "name": "Appointment Booking System",
        "title": "Seamless Bookings & <span>Automated Reminders</span>",
        "img": "funnel_dashboard.jpg",
        "desc": "Manage appointments with automated scheduling, reminders, and rescheduling workflows for a smooth customer booking experience.",
        "plan1": {"name": "Professional Plan", "price": "₹8,000 / 6 Months"},
        "plan2": {"name": "Premium Plan", "price": "₹14,000 / 1 Year"},
        "features": [
            "Calendar Setup",
            "Appointment Scheduling",
            "Reminder Automation",
            "Reschedule Workflow",
            "Booking Management",
            "Reduced No-Shows"
        ]
    },
    {
        "badge": "SOCIAL MEDIA POSTING",
        "name": "Social Media Auto Posting",
        "title": "Multi-Platform Content <span>Auto-Publishing</span>",
        "img": "social_dashboard.jpg",
        "desc": "Schedule and publish content across multiple social media platforms automatically with AI-assisted captions and ready-to-use templates.",
        "plan1": {"name": "Professional Plan", "price": "₹6,000 / 6 Months"},
        "plan2": {"name": "Premium Plan", "price": "₹10,000 / 1 Year"},
        "features": [
            "Scheduled Posting",
            "Caption Setup",
            "Multi-Platform Publishing",
            "AI-Generated Captions",
            "Built-in Post Templates",
            "Consistent Content Delivery"
        ]
    },
    {
        "badge": "CRM & PIPELINE",
        "name": "CRM Setup (Basic)",
        "title": "Organize Leads & <span>Track Conversions</span>",
        "img": "crm_dashboard.jpg",
        "desc": "Organize customer information and manage leads with a structured CRM setup for better tracking and sales management.",
        "plan1": {"name": "Professional Plan", "price": "₹6,000 / 6 Months"},
        "plan2": {"name": "Premium Plan", "price": "₹10,000 / 1 Year"},
        "features": [
            "Pipeline Setup",
            "Lead Stage Configuration",
            "Lead Tagging System",
            "Lead Segmentation",
            "Customer Tracking",
            "Better Lead Management"
        ]
    },
    {
        "badge": "INVOICE & PAYMENTS",
        "name": "Invoice & Payment Automation",
        "title": "Automate Invoicing & <span>Payment Reminders</span>",
        "img": "hero_dashboard.jpg",
        "desc": "Automate invoice creation, invoice delivery, and payment reminders to simplify billing and improve payment collection.",
        "plan1": {"name": "Professional Plan", "price": "₹5,000 / 6 Months"},
        "plan2": {"name": "Premium Plan", "price": "₹8,000 / 1 Year"},
        "features": [
            "Custom Branded Invoice Setup",
            "Invoice Delivery via WhatsApp",
            "Invoice Delivery via Email",
            "Automated Payment Reminders",
            "Professional Billing Workflow",
            "Simplified Payment Management"
        ]
    }
]

html_cards = []
for i, service in enumerate(services_data):
    reverse_class = " reverse" if i % 2 == 1 else ""
    
    bullets_html = "\n".join([
        f'            <div class="feature-bullet-item"><div class="feature-bullet-icon">✓</div><span>{f}</span></div>'
        for f in service["features"]
    ])
    
    card_html = f'''    <!-- Showcase Card {i+1}: {service["name"]} -->
    <div class="feature-showcase-card{reverse_class} reveal reveal-delay-{(i%3)+1}">
      <div class="feature-showcase-grid">
        <div class="feature-showcase-content">
          <div class="feature-pill-badge">{service["badge"]}</div>
          <h2 class="feature-showcase-title">{service["title"]}</h2>
          <p class="feature-showcase-desc">{service["desc"]}</p>
          
          <div class="feature-bullets-grid">
{bullets_html}
          </div>
          
          <div class="feature-pricing-box">
            <div class="feature-price-plan">
              <div class="feature-plan-lbl">{service["plan1"]["name"]}</div>
              <div class="feature-plan-val">{service["plan1"]["price"]}</div>
            </div>
            <div class="feature-price-plan">
              <div class="feature-plan-lbl">{service["plan2"]["name"]}</div>
              <div class="feature-plan-val">{service["plan2"]["price"]}</div>
            </div>
          </div>
          
          <a href="contact.html" class="btn btn-primary btn-ripple">Get Started <span class="btn-arrow">→</span></a>
        </div>
        <div class="feature-dashboard-preview">
          <img src="assets/images/{service["img"]}" alt="{service["name"]} Dashboard Preview">
        </div>
      </div>
    </div>'''
    html_cards.append(card_html)

full_section_html = '''<section class="section" id="all-features">
  <div class="container">
    <div class="feature-showcase-container">
''' + "\n".join(html_cards) + '''
    </div>
  </div>
</section>
'''

with open('features.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- SERVICES & PRICING -->'
end_marker = '<!-- Why Choose TASQ -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + '<!-- SERVICES & PRICING -->\n' + full_section_html + '\n' + content[end_idx:]
    with open('features.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated features.html with showcase cards successfully.")
else:
    print("Could not find markers in features.html")
