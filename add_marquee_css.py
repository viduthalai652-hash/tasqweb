import re

with open('css/home.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace .services-grid block with the new marquee styles
old_grid = '''.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-top: 3rem;
}'''

new_marquee = '''/* ── Services Marquee ── */
.services-marquee-wrapper {
  overflow: hidden;
  position: relative;
  width: 100%;
  margin-top: 3rem;
  padding: 1rem 0; /* Space for hover shadow */
  mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
}

.services-marquee-track {
  display: flex;
  gap: 1.5rem;
  width: max-content;
  animation: scroll-services 25s linear infinite;
}

.services-marquee-track:hover {
  animation-play-state: paused;
}

@keyframes scroll-services {
  0% { transform: translateX(0); }
  /* -50% translates it exactly half the total track width.
     Because we duplicated the exact 6 cards, half the track is exactly 1 full set of cards.
     We must also subtract half the gap (1.5rem / 2 = 0.75rem) to align perfectly. */
  100% { transform: translateX(calc(-50% - 0.75rem)); }
}'''

content = content.replace(old_grid, new_marquee)

# We also need to remove .services-grid media queries at the bottom
content = re.sub(r'\.services-grid\s*\{[^}]*\}', '', content)

with open('css/home.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated home.css")

# Update components.css to set a fixed width for service-card
with open('css/components.css', 'r', encoding='utf-8') as f:
    comp_content = f.read()

comp_content = comp_content.replace('.service-card {', '.service-card {\n  width: 350px;\n  flex-shrink: 0;')

with open('css/components.css', 'w', encoding='utf-8') as f:
    f.write(comp_content)

print("Updated components.css")
