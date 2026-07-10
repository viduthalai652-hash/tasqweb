// ============================================
// TASQ – Feature Detail Page JavaScript
// ============================================

document.addEventListener('DOMContentLoaded', () => {
  initChartBars();
  initProgressBars();
  initMockupAnimations();
  initWorkflowAnimation();

  // Highlight pricing link based on feature
  const selectPlanBtns = document.querySelectorAll('[data-plan]');
  selectPlanBtns.forEach(btn => {
    const plan = btn.getAttribute('data-plan');
    btn.addEventListener('click', () => {
      window.location.href = `../pricing.html?plan=${plan}`;
    });
  });
});

// ── Animate Chart Bars ──
function initChartBars() {
  const barContainers = document.querySelectorAll('.chart-bars');
  if (!barContainers.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bars = entry.target.querySelectorAll('.chart-bar');
        bars.forEach((bar, i) => {
          bar.style.setProperty('--i', i);
          setTimeout(() => {
            bar.style.height = bar.style.getPropertyValue('--h') || '50%';
          }, i * 80);
        });
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  barContainers.forEach(c => observer.observe(c));
}

// ── Progress Bars ──
function initProgressBars() {
  const bars = document.querySelectorAll('.progress-bar');
  if (!bars.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target;
        const width = bar.getAttribute('data-width') || '75';
        setTimeout(() => {
          bar.style.width = width + '%';
        }, 200);
        observer.unobserve(bar);
      }
    });
  }, { threshold: 0.5 });

  bars.forEach(bar => {
    bar.style.width = '0%';
    bar.style.transition = 'width 1.5s cubic-bezier(0.4, 0, 0.2, 1)';
    observer.observe(bar);
  });
}

// ── Mockup Animations ──
function initMockupAnimations() {
  // Stagger mockup card entrance
  const mockupCards = document.querySelectorAll('.mockup-card');
  mockupCards.forEach((card, i) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 0.5s ease ${i * 0.08}s, transform 0.5s ease ${i * 0.08}s`;
  });

  const mockup = document.querySelector('.dashboard-mockup');
  if (mockup) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          mockupCards.forEach(card => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          });
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    observer.observe(mockup);
  }
}

// ── Workflow Step Animation ──
function initWorkflowAnimation() {
  const steps = document.querySelectorAll('.workflow-step');
  if (!steps.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        steps.forEach((step, i) => {
          setTimeout(() => {
            step.style.opacity = '1';
            step.style.transform = 'translateX(0)';
          }, i * 150);
        });
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });

  steps.forEach(step => {
    step.style.opacity = '0';
    step.style.transform = 'translateX(-20px)';
    step.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  });

  const workflowSection = document.querySelector('.workflow-steps');
  if (workflowSection) observer.observe(workflowSection);
}
