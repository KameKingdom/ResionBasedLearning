import json
jacket_num = 0
max_price = 0
min_price = 100000
file_name = "catalog.json"

# JSONファイルの読み込み
with open(file_name) as file:
    data = json.load(file)
    for info in data:
        price = info["price"]
        item = info["name"]
        if item == "jacket":
            jacket_num += 1
            if price >= int(max_price):
                max_price = price
            if price <= int(min_price):
                min_price = price

print(f"ジャケットの数{jacket_num}\n最高価格{max_price}\n最低価格{min_price}")        
