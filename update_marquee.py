import re

services_data = [
    {
        "name": "Instagram Automation Packs",
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
        "name": "WhatsApp Lead Automation",
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
        "name": "Google My Business Automation",
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
        "name": "Appointment Booking System",
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
        "name": "Social Media Auto Posting",
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
        "name": "CRM Setup (Basic)",
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
        "name": "Invoice & Payment Automation",
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

html_cards = ""
for service in services_data:
    features_list_html = '\\n'.join([f'            <li><span class="check">✔</span> {f}</li>' for f in service['features']])
    
    card_html = f'''      <div class="pricing-card" style="box-shadow: none; border-color: rgba(0,0,0,0.1);">
        <div class="pricing-card-header">
          <h3 class="pricing-card-title">{service["name"]}</h3>
          <p class="pricing-card-desc" style="display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">{service["desc"]}</p>
        </div>
        <div class="pricing-card-plans">
          <div class="pricing-plan">
            <div class="plan-name">{service["plan1"]["name"]}</div>
            <div class="plan-price">{service["plan1"]["price"]}</div>
          </div>
          <div class="pricing-plan">
            <div class="plan-name">{service["plan2"]["name"]}</div>
            <div class="plan-price">{service["plan2"]["price"]}</div>
          </div>
        </div>
        <div class="pricing-card-features">
          <ul>
{features_list_html}
          </ul>
        </div>
        <div class="pricing-card-footer">
          <a href="contact.html" class="btn btn-secondary btn-block btn-ripple">Get Started</a>
        </div>
      </div>'''
    html_cards += card_html + '\\n'

marquee_inner = html_cards + '\\n        <!-- Duplicate for infinite scroll loop -->\\n' + html_cards

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the contents of <div class="services-marquee-track"> ... </div>
start_tag = '<div class="services-marquee-track">'
end_tag = '</div>\n    </div>\n  </div>\n</section>'

start_idx = content.find(start_tag)
if start_idx != -1:
    end_idx = content.find(end_tag, start_idx)
    if end_idx != -1:
        new_content = content[:start_idx + len(start_tag)] + '\\n' + marquee_inner + '      ' + content[end_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated index.html marquee successfully.")
    else:
        print("Could not find end tag.")
else:
    print("Could not find start tag.")
