import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('<i class="fa-solid fa-image text-6xl text-gray-300"></i>')
if len(parts) >= 5:
    new_content = parts[0]
    new_content += '<img src="assets/images/irrigation_stakes.png" alt="Product" class="max-h-full max-w-full object-contain">' + parts[1]
    new_content += '<img src="assets/images/product_shears.png" alt="Product" class="max-h-full max-w-full object-contain">' + parts[2]
    new_content += '<img src="assets/images/manual_seeder.png" alt="Product" class="max-h-full max-w-full object-contain">' + parts[3]
    new_content += '<img src="assets/images/synthetic_oil.png" alt="Product" class="max-h-full max-w-full object-contain">' + parts[4]
    if len(parts) > 5:
        new_content += '<i class="fa-solid fa-image text-6xl text-gray-300"></i>'.join(parts[5:])
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Done replacing images in index.html')
else:
    print('Could not find 4 placeholders. Found:', len(parts)-1)
