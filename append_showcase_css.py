css_add = '''
/* ── Feature Showcase Cards (Reference Image Layout) ── */
.feature-showcase-container {
  display: flex;
  flex-direction: column;
  gap: 3.5rem;
  margin-top: 2rem;
}

.feature-showcase-card {
  background: #FAF9F6;
  border-radius: 24px;
  border: 1px solid rgba(0, 0, 0, 0.06);
  padding: 3rem;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.04);
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.feature-showcase-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 50px rgba(255, 106, 0, 0.08);
}

.feature-showcase-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3.5rem;
  align-items: center;
}

.feature-showcase-card.reverse .feature-showcase-grid > *:first-child {
  order: 2;
}

.feature-showcase-card.reverse .feature-showcase-grid > *:last-child {
  order: 1;
}

.feature-pill-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 106, 0, 0.1);
  color: var(--color-orange, #FF6A00);
  padding: 0.4rem 1rem;
  border-radius: 50px;
  font-family: var(--font-heading);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: 1.25rem;
}

.feature-pill-badge::before {
  content: '•';
  font-size: 1.2rem;
  color: var(--color-orange, #FF6A00);
}

.feature-showcase-title {
  font-family: var(--font-heading);
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--color-black, #111);
  line-height: 1.25;
  margin-bottom: 1rem;
}

.feature-showcase-title span {
  color: var(--color-orange, #FF6A00);
}

.feature-showcase-desc {
  font-size: 1.05rem;
  color: #555;
  line-height: 1.6;
  margin-bottom: 1.75rem;
}

.feature-bullets-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem 1.5rem;
  margin-bottom: 2rem;
}

.feature-bullet-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 700;
  color: #222;
}

.feature-bullet-icon {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--gradient-orange, linear-gradient(135deg, #FF6A00, #FF8A00));
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  font-weight: 800;
  flex-shrink: 0;
  box-shadow: 0 4px 10px rgba(255, 106, 0, 0.25);
}

.feature-pricing-box {
  background: white;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 16px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 2rem;
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.feature-price-plan {
  flex: 1;
}

.feature-price-plan:first-child {
  border-right: 1px solid rgba(0, 0, 0, 0.08);
  padding-right: 1.5rem;
}

.feature-plan-lbl {
  font-size: 0.75rem;
  text-transform: uppercase;
  font-weight: 800;
  color: var(--color-orange);
  letter-spacing: 0.05em;
  margin-bottom: 0.25rem;
}

.feature-plan-val {
  font-size: 1.1rem;
  font-weight: 800;
  color: #111;
}

.feature-dashboard-preview {
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
  background: #0f1013;
  border: 1px solid rgba(255, 255, 255, 0.1);
  aspect-ratio: 16/10;
  transition: transform var(--transition-base);
}

.feature-showcase-card:hover .feature-dashboard-preview {
  transform: scale(1.02);
}

.feature-dashboard-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

@media (max-width: 992px) {
  .feature-showcase-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .feature-showcase-card.reverse .feature-showcase-grid > *:first-child {
    order: 1;
  }
  .feature-showcase-card.reverse .feature-showcase-grid > *:last-child {
    order: 2;
  }
  .feature-showcase-card {
    padding: 2rem 1.5rem;
  }
  .feature-bullets-grid {
    grid-template-columns: 1fr;
  }
  .feature-pricing-box {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
  }
  .feature-price-plan:first-child {
    border-right: none;
    border-bottom: 1px solid rgba(0,0,0,0.08);
    padding-right: 0;
    padding-bottom: 0.75rem;
    width: 100%;
  }
}
'''

with open('css/components.css', 'r', encoding='utf-8') as f:
    content = f.read()

if '.feature-showcase-card' not in content:
    content += css_add
    with open('css/components.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Appended feature showcase card styles to components.css")
