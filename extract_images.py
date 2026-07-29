import re
import os
import base64

html_path = '/Users/naveennayak/Business-Ocean/index.html'
assets_dir = '/Users/naveennayak/Business-Ocean/assets'

if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all base64 data URIs
pattern = r'data:image/(png|jpeg|jpg);base64,([A-Za-z0-9+/=]+)'

def replace_b64(match):
    global img_counter
    ext = match.group(1)
    b64_data = match.group(2)
    
    filename = f'img_{img_counter}.{ext}'
    filepath = os.path.join(assets_dir, filename)
    
    with open(filepath, 'wb') as img_file:
        img_file.write(base64.b64decode(b64_data))
        
    img_counter += 1
    return f'assets/{filename}'

img_counter = 1
new_html = re.sub(pattern, replace_b64, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Images extracted successfully!")
