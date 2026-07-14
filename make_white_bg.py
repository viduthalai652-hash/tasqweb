from PIL import Image
import math

def make_bg_white(img_path, out_path, tolerance=30):
    img = Image.open(img_path).convert("RGB")
    data = img.load()
    width, height = img.size
    
    # Assume top-left pixel is the background color
    bg_color = data[0, 0]
    
    for y in range(height):
        for x in range(width):
            r, g, b = data[x, y]
            # Calculate distance to background color
            dist = math.sqrt((r - bg_color[0])**2 + (g - bg_color[1])**2 + (b - bg_color[2])**2)
            
            if dist <= tolerance:
                data[x, y] = (255, 255, 255)
            elif dist <= tolerance + 20:
                # blend to smooth edges
                factor = (dist - tolerance) / 20.0
                new_r = int(255 * (1 - factor) + r * factor)
                new_g = int(255 * (1 - factor) + g * factor)
                new_b = int(255 * (1 - factor) + b * factor)
                data[x, y] = (new_r, new_g, new_b)
                
    img.save(out_path, quality=100)
    print("Saved to", out_path)

try:
    make_bg_white("assets/images/logo.jpg", "assets/images/logo.jpg")
except Exception as e:
    print("Error:", e)
