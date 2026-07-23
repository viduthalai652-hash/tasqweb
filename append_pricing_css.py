import os

new_css = '''
/* ── New Service / Pricing Card ── */
.pricing-card {
  background: white;
  border-radius: var(--radius-xl);
  border: 1px solid rgba(0,0,0,0.08);
  box-shadow: var(--shadow-card);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition: transform var(--transition-base), box-shadow var(--transition-base);
  height: 100%;
  width: 380px; /* Base width for marquee and grid */
  flex-shrink: 0;
}

.pricing-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-orange);
  border-color: rgba(255,106,0,0.3);
}

.pricing-card-header {
  padding: 2rem;
  text-align: center;
  border-bottom: 1px solid rgba(0,0,0,0.08);
  background: var(--color-white-warm);
}

.pricing-card-title {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 1.5rem;
  color: var(--color-black);
  margin-bottom: 0.75rem;
  line-height: 1.2;
}

.pricing-card-desc {
  font-size: 0.95rem;
  color: #555;
  line-height: 1.5;
}

.pricing-card-plans {
  display: flex;
  border-bottom: 1px solid rgba(0,0,0,0.08);
}

.pricing-plan {
  flex: 1;
  padding: 1.25rem 1rem;
  text-align: center;
}

.pricing-plan:first-child {
  border-right: 1px solid rgba(0,0,0,0.08);
}

.plan-name {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.8rem;
  color: var(--color-orange);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.5rem;
}

.plan-price {
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--color-black);
}

.pricing-card-features {
  padding: 2rem;
  flex-grow: 1;
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
  font-size: 0.95rem;
  color: #444;
  line-height: 1.4;
}

.pricing-card-features .check {
  color: var(--color-orange);
  font-weight: bold;
}

.pricing-card-footer {
  padding: 0 2rem 2rem 2rem;
  margin-top: auto;
}

.pricing-card-footer .btn {
  width: 100%;
}
'''

with open('css/components.css', 'a', encoding='utf-8') as f:
    f.write(new_css)

print("Appended Pricing Card CSS to components.css")
