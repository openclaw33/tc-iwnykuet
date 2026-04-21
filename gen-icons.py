from PIL import Image, ImageDraw, ImageFont
import os

out_dir = os.path.dirname(os.path.abspath(__file__))

for size in [192, 512]:
    img = Image.new('RGB', (size, size), '#6c5ce7')
    draw = ImageDraw.Draw(img)
    
    for y in range(size):
        r = int(108 + (162-108) * y/size)
        g = int(92 + (155-92) * y/size)
        b = int(231 + (254-231) * y/size)
        draw.line([(0,y),(size,y)], fill=(r,g,b))
    
    cx, cy = size//2, int(size*0.42)
    radius = int(size*0.25)
    draw.ellipse([cx-radius, cy-radius, cx+radius, cy+radius], outline='white', width=max(2, size//80))
    draw.line([(cx, cy), (cx, cy-int(radius*0.7))], fill='white', width=max(2, size//100))
    draw.line([(cx, cy), (cx+int(radius*0.5), cy-int(radius*0.3))], fill='white', width=max(2, size//100))
    dot = max(3, size//60)
    draw.ellipse([cx-dot, cy-dot, cx+dot, cy+dot], fill='white')
    
    try:
        font = ImageFont.truetype('arial.ttf', size//8)
    except:
        font = ImageFont.load_default()
    
    text = 'TIME'
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((size-tw)//2, int(size*0.78)), text, fill='white', font=font)
    
    fp = os.path.join(out_dir, f'icon-{size}x{size}.png')
    img.save(fp)
    print(f'Created {fp} ({os.path.getsize(fp)} bytes)')
