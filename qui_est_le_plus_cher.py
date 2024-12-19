
import json
from pathlib import Path 

price_list_per_shop = {}
cumulative_price_difference = {}

# normalization
for json_file in Path('products').glob('*.json'):
    with json_file.open(encoding="utf8") as f:
        data = json.load(f)
        shop_name = data['shop_name']
 
        for product in data['products']:
            product_name = product['name']
            product_price = product["price"]

            price_per_shop = price_list_per_shop.setdefault(product_name, {})
            price_per_shop[shop_name] = product_price

# processing
for product_name, price_per_shop in price_list_per_shop.items():
    min_price = min(price_per_shop.values())
    for shop_name, shop_specific_product_price in price_per_shop.items():
        price_delta = shop_specific_product_price - min_price   
        cumulative_price_difference[shop_name] = cumulative_price_difference.get(shop_name, 0) + price_delta


# display
wall_of_shame = sorted(cumulative_price_difference.items(), key=lambda e: e[1], reverse=True)
for shop_name, price_diff in wall_of_shame:
    print(f"{shop_name}: {price_diff:.2f}€")