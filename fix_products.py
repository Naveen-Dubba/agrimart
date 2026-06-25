import re

with open('products.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<i class="fa-solid \$\{product\.image_url\} text-6xl text-gray-300"></i>', r'<img src="${product.image_url}" alt="${product.name}" class="max-h-full max-w-full object-contain">', content)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated products.html")
