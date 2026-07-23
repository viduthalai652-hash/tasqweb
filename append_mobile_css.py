with open('css/base.css', 'a', encoding='utf-8') as f:
    f.write('''
/* ============================================
   Global Mobile Responsiveness Fixes
   ============================================ */

@media (max-width: 768px) {
  /* Scale down overall rem values slightly */
  html {
    font-size: 14px;
  }
  
  /* Reduce container and section padding */
  .container {
    padding: 0 1.25rem;
  }
  .section {
    padding: 3rem 0;
  }

  /* Typography Scaling */
  h1 { font-size: 2.25rem !important; }
  h2 { font-size: 1.8rem !important; }
  .hero-title { font-size: 2.2rem !important; line-height: 1.2 !important; }
  .pricing-hero h1 { font-size: 2.2rem !important; }
  
  /* Feature Showcase Cards (features.html) */
  .feature-showcase-card {
    padding: 1.5rem 1rem !important;
  }
  .feature-showcase-grid {
    gap: 1.5rem !important;
  }
  .feature-showcase-title {
    font-size: 1.7rem !important;
  }
  .feature-bullet-item {
    font-size: 0.85rem !important;
  }

  /* Pricing Cards (pricing.html) */
  .pricing-card-dark {
    padding: 1.5rem 1rem !important;
  }
  .dark-plan-price {
    font-size: 2rem !important;
  }
  .dark-plan-currency {
    font-size: 1.5rem !important;
  }
  .dark-plan-desc {
    font-size: 0.85rem !important;
  }

  /* Service Tab Switcher */
  .service-tab-bar {
    gap: 0.3rem !important;
    padding: 0.4rem !important;
  }
  .service-tab-btn {
    padding: 0.4rem 0.8rem !important;
    font-size: 0.75rem !important;
    flex-grow: 1; /* allow them to stretch nicely */
    text-align: center;
  }

  /* Overview Table */
  .pricing-overview-section {
    padding: 4rem 0 !important;
  }
}

@media (max-width: 480px) {
  /* Stack buttons on very small screens */
  .hero-btns, .final-cta-btns {
    flex-direction: column;
    width: 100%;
    align-items: stretch !important;
  }
  .hero-btns .btn, .final-cta-btns .btn {
    width: 100%;
    text-align: center;
    justify-content: center;
  }
  
  /* Make pricing plan grid 1 column in feature showcase */
  .feature-pricing-box {
    flex-direction: column;
    gap: 1rem;
    padding: 1rem !important;
  }
  .feature-price-plan:first-child {
    border-right: none !important;
    border-bottom: 1px solid rgba(0,0,0,0.08) !important;
    padding-right: 0 !important;
    padding-bottom: 1rem !important;
  }

  /* Typography */
  .hero-title { font-size: 2rem !important; }
}
''')

print("Successfully appended mobile fixes to base.css")
