import os
import glob

files = glob.glob('*.html')

header_old = """
                <div class="flex items-center space-x-6">
                    <div class="flex items-center gap-2 cursor-pointer hover:text-agrigreen transition">
                        <div class="bg-gray-100 p-3 rounded-full text-gray-600"><i class="fa-solid fa-user"></i></div>
                        <div class="hidden sm:block">
                            <span class="text-sm text-gray-500 block">Account</span>
                            <span class="font-bold">Sign In</span>
                        </div>
                    </div>
                    <div class="flex items-center gap-2 cursor-pointer hover:text-agrigreen transition">
                        <div class="bg-agrigreen p-3 rounded-full text-white relative">
                            <i class="fa-solid fa-shopping-cart"></i>
                            <span class="absolute -top-1 -right-1 bg-yellow-500 text-xs font-bold px-1.5 rounded-full border border-white">0</span>
                        </div>
                        <div class="hidden sm:block">
                            <span class="text-sm text-gray-500 block">My Cart</span>
                            <span class="font-bold text-agrigreen">₹ 0.00</span>
                        </div>
                    </div>
                </div>
"""

header_new = """
                <div class="flex items-center space-x-6">
                    <a href="login.html" class="flex items-center gap-2 cursor-pointer hover:text-agrigreen transition">
                        <div class="bg-gray-100 p-3 rounded-full text-gray-600"><i class="fa-solid fa-user"></i></div>
                        <div class="hidden sm:block">
                            <span class="text-sm text-gray-500 block">Account</span>
                            <span class="font-bold">Sign In</span>
                        </div>
                    </a>
                    <a href="cart.html" class="flex items-center gap-2 cursor-pointer hover:text-agrigreen transition">
                        <div class="bg-agrigreen p-3 rounded-full text-white relative">
                            <i class="fa-solid fa-shopping-cart"></i>
                            <span class="absolute -top-1 -right-1 bg-yellow-500 text-xs font-bold px-1.5 rounded-full border border-white">0</span>
                        </div>
                        <div class="hidden sm:block">
                            <span class="text-sm text-gray-500 block">My Cart</span>
                            <span class="font-bold text-agrigreen">₹ 0.00</span>
                        </div>
                    </a>
                </div>
"""

for file in files:
    # Skip login and cart since they are already built with links
    if file in ['login.html', 'cart.html', 'agrimart-testing-capstone.html']: continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace header
    content = content.replace(header_old.strip(), header_new.strip())
    
    # 2. Replace buttons
    content = content.replace('<button class="w-full bg-agrigreen text-white font-bold py-2 rounded shadow-md hover:bg-green-800 transition">BUY NOW</button>', '<a href="cart.html" class="block text-center w-full bg-agrigreen text-white font-bold py-2 rounded shadow-md hover:bg-green-800 transition">BUY NOW</a>')
    
    content = content.replace('<button class="bg-agrigreen text-white text-xs font-bold py-2 px-4 rounded w-full">VIEW MORE</button>', '<a href="contact.html" class="block text-center bg-agrigreen text-white text-xs font-bold py-2 px-4 rounded w-full">VIEW MORE</a>')
    
    content = content.replace('<button class="bg-yellow-500 text-gray-900 text-xs font-bold py-2 px-4 rounded">VIEW MORE</button>', '<a href="products.html" class="inline-block text-center bg-yellow-500 text-gray-900 text-xs font-bold py-2 px-4 rounded">VIEW MORE</a>')
    
    content = content.replace('<button class="bg-yellow-500 text-gray-900 text-xs font-bold py-2 px-4 rounded">VIEW NOW</button>', '<a href="about.html" class="inline-block text-center bg-yellow-500 text-gray-900 text-xs font-bold py-2 px-4 rounded">VIEW NOW</a>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links and buttons!")
