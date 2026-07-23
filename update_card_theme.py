import re

with open('css/components.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Update Pricing Card to Dark Theme
dark_css = '''/* ── New Service / Pricing Card (Dark Theme) ── */
.pricing-card {
  background: #141518;
  border-radius: var(--radius-xl);
  border: 1px solid rgba(255,255,255,0.05);
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition: transform var(--transition-base), box-shadow var(--transition-base), border-color var(--transition-base);
  height: 100%;
  width: 100%;
  max-width: 380px;
  flex-shrink: 0;
}

.services-marquee-track .pricing-card {
  width: 380px;
  max-width: none;
}

.pricing-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 40px rgba(255,106,0,0.15);
  border-color: rgba(255,106,0,0.3);
}

.pricing-card-header {
  padding: 1.5rem;
  text-align: center;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  background: #1a1b1f;
}

.pricing-card-title {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 1.4rem;
  color: white;
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.pricing-card-desc {
  font-size: 0.9rem;
  color: rgba(255,255,255,0.65);
  line-height: 1.5;
}

.pricing-card-plans {
  display: flex;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  background: #141518;
}

.pricing-plan {
  flex: 1;
  padding: 1rem 0.75rem;
  text-align: center;
}

.pricing-plan:first-child {
  border-right: 1px solid rgba(255,255,255,0.05);
}

.plan-name {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.75rem;
  color: var(--color-orange);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.25rem;
}

.plan-price {
  font-weight: 700;
  font-size: 1rem;
  color: white;
}

.pricing-card-features {
  padding: 1.5rem;
  flex-grow: 1;
  background: #141518;
}

.pricing-card-features ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.pricing-card-features li {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.9rem;
  color: rgba(255,255,255,0.75);
  line-height: 1.4;
}

.pricing-card-features .check {
  color: var(--color-orange);
  font-weight: bold;
}

.pricing-card-footer {
  padding: 0 1.5rem 1.5rem 1.5rem;
  margin-top: auto;
  background: #141518;
}

.pricing-card-footer .btn {
  width: 100%;
}

.pricing-card-img {
  width: 100%;
  height: 180px;
  background: #0f1013;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.pricing-card-img::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--gradient-orange);
  opacity: 0;
  transition: opacity var(--transition-slow);
}

.pricing-card:hover .pricing-card-img::after {
  opacity: 0.15;
}
'''

# We will replace from `.pricing-card {` all the way down to `.pricing-card:hover .pricing-card-img::after { \n}`
start_idx = css_content.find('.pricing-card {')
if start_idx != -1:
    # Find the end of the last rule
    end_marker = '.pricing-card:hover .pricing-card-img::after {'
    end_idx = css_content.find(end_marker)
    if end_idx != -1:
        # find the closing brace for that rule
        close_brace = css_content.find('}', end_idx)
        if close_brace != -1:
            css_content = css_content[:start_idx] + dark_css + css_content[close_brace+1:]
            with open('css/components.css', 'w', encoding='utf-8') as f:
                f.write(css_content)
            print("Successfully updated components.css with dark theme cards.")
        else:
            print("Could not find closing brace.")
    else:
        print("Could not find end marker.")
else:
    print("Could not find start marker.")
