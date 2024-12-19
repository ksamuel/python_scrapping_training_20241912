# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "faker",
#     "faker-commerce",
# ]
# ///

import json
import random
from faker import Faker
from faker_commerce import Provider

# Initialize Faker with commerce provider
fake = Faker()
fake.add_provider(Provider)

# Function to generate products
def generate_products(num_products):
    products = []
    used_names = set()  # To ensure unique names
    
    while len(products) < num_products:
        name = fake.ecommerce_name()
        
        # Only add if name is unique
        if name not in used_names:
            used_names.add(name)
            product = {
                'id': len(products) + 1,
                'name': name,
                'category': fake.ecommerce_category(),
                'base_price': round(random.uniform(9.99, 999.99), 2)
            }
            products.append(product)
    
    return products

# Generate 500 unique products
products = generate_products(500)

# Shop names
shops = [
    "MegaMart",
    "ValueKing",
    "PrimePicks",
    "ShopSmart",
    "BargainBest",
    "RetailRush",
    "DealsDirect"
]

# Generate price variations for each shop
def generate_shop_prices(products, shop_name):
    # Each shop has a different pricing strategy
    variation_factors = {
        "MegaMart": {"min": 0.95, "max": 1.15},
        "ValueKing": {"min": 0.90, "max": 1.05},
        "PrimePicks": {"min": 1.05, "max": 1.25},
        "ShopSmart": {"min": 0.92, "max": 1.08},
        "BargainBest": {"min": 0.88, "max": 1.02},
        "RetailRush": {"min": 0.98, "max": 1.18},
        "DealsDirect": {"min": 0.93, "max": 1.12}
    }
    
    shop_products = []
    factors = variation_factors[shop_name]
    
    for product in products:
        variation = random.uniform(factors["min"], factors["max"])
        new_price = round(product["base_price"] * variation, 2)
        
        shop_product = {
            "id": product["id"],
            "name": product["name"],
            "category": product["category"],
            "price": new_price
        }
        shop_products.append(shop_product)
    
    return shop_products

# Generate and save files for each shop
for shop in shops:
    shop_data = {
        "shop_name": shop,
        "products": generate_shop_prices(products, shop)
    }
    
    filename = f"{shop.lower().replace(' ', '_')}_products.json"
    with open(filename, 'w') as f:
        json.dump(shop_data, f, indent=2)

print("Generated files:")
for shop in shops:
    print(f"- {shop.lower().replace(' ', '_')}_products.json")