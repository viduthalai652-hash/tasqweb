from PIL import Image
import math
import os

def make_bg_transparent(img_path, out_path, tolerance=30):
    img = Image.open(img_path).convert("RGBA")
    data = img.load()
    width, height = img.size
    
    # Assume top-left pixel is the background color
    bg_color = data[0, 0]
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = data[x, y]
            # Calculate distance to background color
            dist = math.sqrt((r - bg_color[0])**2 + (g - bg_color[1])**2 + (b - bg_color[2])**2)
            
            if dist <= tolerance:
                # Fully transparent
                data[x, y] = (255, 255, 255, 0)
            elif dist <= tolerance + 30:
                # Smooth edge (alpha blending)
                factor = (dist - tolerance) / 30.0
                new_a = int(255 * factor)
                data[x, y] = (r, g, b, new_a)
                
    img.save(out_path, format="PNG")
    print("Saved transparent image to", out_path)

try:
    make_bg_transparent("assets/images/logo.jpg", "assets/images/logo.png")
except Exception as e:
    print("Error:", e)

# Now update the HTML files to use logo.png instead of logo.jpg
html_files = ['index.html', 'features.html', 'pricing.html', 'contact.html']

for fname in html_files:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    updated = content.replace('assets/images/logo.jpg', 'assets/images/logo.png')
    
    if updated == content:
        print(f"  WARNING: logo.jpg not found in {fname}")
    else:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"  Updated: {fname}")

print("Done!")
