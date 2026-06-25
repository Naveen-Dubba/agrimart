import re

with open('cart.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(
    r'<i class="fa-solid fa-image text-4xl text-gray-300 bg-gray-100 p-4 rounded"></i>',
    r'<img src="assets/images/irrigation_stakes.png" alt="Irrigation Stakes" class="h-16 w-16 object-contain bg-gray-100 p-2 rounded">',
    content
)

with open('cart.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Updated cart.html")
