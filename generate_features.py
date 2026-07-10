import json

features = [
    {
        "id": "crm",
        "icon": "🎯",
        "label": "CRM",
        "title": "Manage customer relationships and close deals faster.",
        "desc": "Track leads, organize contacts, and manage your entire sales pipeline from one centralized dashboard. Build stronger relationships with full customer history.",
        "checks": ["Contact Management", "Sales Pipeline Tracking", "Lead Scoring", "Deal Analytics"],
        "url": "crm.html",
        "img": "crm_dashboard.jpg",
        "filter": ""
    },
    {
        "id": "funnel",
        "icon": "🎪",
        "label": "Funnel Builder",
        "title": "Build beautiful funnels that convert visitors into buyers.",
        "desc": "Create high-converting sales funnels and landing pages without writing a single line of code. Launch, test, and optimize your campaigns in minutes.",
        "checks": ["Drag-and-Drop Builder", "Conversion Optimization", "Funnel Analytics", "A/B Split Testing"],
        "url": "funnel-builder.html",
        "img": "funnel_dashboard.jpg",
        "filter": ""
    },
    {
        "id": "social",
        "icon": "📱",
        "label": "Social Media",
        "title": "Automate your social presence across all major platforms.",
        "desc": "Plan, schedule, and publish content to Facebook, Instagram, LinkedIn, and X from one intelligent dashboard. Grow your audience effortlessly.",
        "checks": ["Auto Scheduling", "Unified Content Calendar", "Performance Analytics", "Multi-Platform Sync"],
        "url": "social-media.html",
        "img": "social_dashboard.jpg",
        "filter": ""
    },
    {
        "id": "marketing",
        "icon": "⚡",
        "label": "Marketing Automation",
        "title": "Deliver personalized campaigns with intelligent workflows.",
        "desc": "Automate your marketing campaigns using drag-and-drop workflows. Trigger personalized actions based on customer behavior and interactions.",
        "checks": ["Visual Workflow Builder", "Behavioral Triggers", "Automated Sequences", "Campaign ROI Tracking"],
        "url": "marketing-automation.html",
        "img": "marketing_dashboard.jpg",
        "filter": ""
    },
    {
        "id": "email",
        "icon": "📨",
        "label": "Email & WhatsApp",
        "title": "Connect instantly with automated messaging channels.",
        "desc": "Communicate with customers through automated email and WhatsApp broadcasts. Keep your brand top of mind with high open rates and instant delivery.",
        "checks": ["Broadcast Messaging", "Dynamic Templates", "WhatsApp API Integration", "Delivery & Open Reports"],
        "url": "email-whatsapp.html",
        "img": "marketing_dashboard.jpg",
        "filter": "filter: hue-rotate(220deg);"
    },
    {
        "id": "calendar",
        "icon": "🗓️",
        "label": "Calendar",
        "title": "Smart scheduling and automated appointment booking.",
        "desc": "Manage meetings, client appointments, and team availability with a powerful booking system that syncs directly with your existing calendars.",
        "checks": ["Online Booking Pages", "Automated Reminders", "Team Calendar Sync", "Timezone Management"],
        "url": "calendar.html",
        "img": "social_dashboard.jpg",
        "filter": "filter: hue-rotate(150deg);"
    },
    {
        "id": "ai-bot",
        "icon": "🤖",
        "label": "AI Bot Automation",
        "title": "Qualify leads and support customers automatically 24/7.",
        "desc": "Deploy intelligent AI chatbots trained on your business data to answer questions, book appointments, and capture leads while you sleep.",
        "checks": ["Custom AI Training", "Automated Support", "Lead Qualification", "Human Handoff"],
        "url": "ai-bot.html",
        "img": "ai_bot_dashboard.jpg",
        "filter": ""
    },
    {
        "id": "analytics",
        "icon": "📈",
        "label": "Analytics",
        "title": "Make data-driven decisions with real-time reporting.",
        "desc": "Track business performance using beautiful, live analytics dashboards. Customize reports to focus on the metrics that matter most to your growth.",
        "checks": ["Live Revenue Tracking", "Custom Dashboards", "Conversion Metrics", "Exportable Reports"],
        "url": "analytics.html",
        "img": "crm_dashboard.jpg",
        "filter": "filter: hue-rotate(80deg);"
    },
    {
        "id": "reputation",
        "icon": "🏅",
        "label": "Reputation Management",
        "title": "Build trust and gather 5-star reviews automatically.",
        "desc": "Monitor online reviews across Google and Facebook, collect customer feedback automatically, and strengthen your digital brand reputation.",
        "checks": ["Review Monitoring", "Automated Requests", "Feedback Widgets", "Reputation Scoring"],
        "url": "reputation.html",
        "img": "funnel_dashboard.jpg",
        "filter": "filter: hue-rotate(300deg);"
    },
    {
        "id": "invoices",
        "icon": "💳",
        "label": "Invoices",
        "title": "Get paid faster with professional automated billing.",
        "desc": "Create branded invoices, manage recurring billing, track payments, and automatically send reminders to clients with overdue balances.",
        "checks": ["Custom Invoice Builder", "Stripe & PayPal Sync", "Recurring Subscriptions", "Auto Payment Reminders"],
        "url": "invoices.html",
        "img": "crm_dashboard.jpg",
        "filter": "filter: grayscale(0.8) sepia(0.2);"
    },
    {
        "id": "memberships",
        "icon": "🏫",
        "label": "Memberships",
        "title": "Launch courses and build exclusive communities.",
        "desc": "Host digital products, create structured online courses, and manage secure access to premium content for your members and students.",
        "checks": ["Course Builder", "Secure Video Hosting", "Student Progress Tracking", "Community Forums"],
        "url": "memberships.html",
        "img": "funnel_dashboard.jpg",
        "filter": "filter: hue-rotate(180deg);"
    },
    {
        "id": "integrations",
        "icon": "⚙️",
        "label": "Integrations",
        "title": "Plug Tasq into every tool you already use.",
        "desc": "Connect Google, Microsoft, Slack, Zapier, payment gateways and countless CRMs via native integrations, webhooks and a fully documented REST API.",
        "checks": ["Google & Microsoft 365", "Slack Notifications", "Stripe & Paddle", "REST API & Webhooks"],
        "url": "integrations.html",
        "img": "social_dashboard.jpg",
        "filter": "filter: hue-rotate(270deg);"
    }
]

html_output = '<div class="features-stack">\n'

for f in features:
    html_output += f'''
      <div class="feature-stack-block reveal">
        <div class="feature-stack-image-wrapper">
          <div class="feature-stack-browser">
            <div class="feature-stack-browser-header">
              <div class="feature-stack-browser-dots"><span></span><span></span><span></span></div>
              <div class="feature-stack-browser-address">app.tasq.com/{f['id']}</div>
            </div>
            <img src="assets/images/{f['img']}" alt="{f['label']} Dashboard" class="feature-stack-image" style="{f['filter']}">
          </div>
        </div>
        <div class="feature-stack-content">
          <div class="feature-stack-label"><span class="feature-stack-label-icon">{f['icon']}</span> {f['label']}</div>
          <h3 class="feature-stack-title">{f['title']}</h3>
          <p class="feature-stack-desc">{f['desc']}</p>
          <div class="feature-checklist">
            <div class="feature-checklist-item"><div class="feature-checklist-icon">✓</div> {f['checks'][0]}</div>
            <div class="feature-checklist-item"><div class="feature-checklist-icon">✓</div> {f['checks'][1]}</div>
            <div class="feature-checklist-item"><div class="feature-checklist-icon">✓</div> {f['checks'][2]}</div>
            <div class="feature-checklist-item"><div class="feature-checklist-icon">✓</div> {f['checks'][3]}</div>
          </div>
          <div class="feature-stack-btns">
            <a href="features/{f['url']}" class="btn" style="background:#8b5cf6;color:white;box-shadow:0 4px 14px rgba(139,92,246,0.3);">Explore {f['label']} →</a>
            <a href="pricing.html" class="btn btn-secondary">See pricing</a>
          </div>
        </div>
      </div>
'''

html_output += '</div>\n'

with open('features_stack.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("Generated features_stack.html")
