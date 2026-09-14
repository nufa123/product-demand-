# x = 10
# print(x)
# a = "nufa"
# print(a)
# list = [1,2,3,4]
# print(list)
# fruits = ["apple","orange","mango"]
# print(fruits)
# fruits.append("grapes")
# print(fruits)
# fruits.insert(1,"avacado")
# print(fruits)
# fruits.extend(["blueberry","pineapple","strawberry","apple"])
# print(fruits)
# count_apple = fruits.count('apple')
# print(count_apple)


# tuple = (1,2,3,4,5)
# print(tuple)

# print(len(tuple))
# print(max(tuple))
# print(min(tuple))
# print(sum(tuple))


# dict = {
#     "name" : "amal",
#     "age" : 18,
#     "place" : "calicut"
# }
# print(dict)
# dict["age"] = 25
# print(dict)









# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# print(A | B)  
# print(A & B)  
# print(A - B)  
# print(A ^ B) 
# print(2 in A)
# print(10 not in A)
# A.add(5)
# print(A)
# A.remove(2)
# print(A)





# Raw dataset containing daily sales records
raw_data = [
    "2026-01-01,P001,Wireless Mouse,Electronics,599,0,100,12",
    "2026-01-02,P001,Wireless Mouse,Electronics,599,0,88,14",
    "2026-01-03,P001,Wireless Mouse,Electronics,599,0,74,13",
    "2026-01-04,P001,Wireless Mouse,Electronics,549,1,61,25",
    "2026-01-05,P001,Wireless Mouse,Electronics,549,1,36,29",
    "2026-01-06,P001,Wireless Mouse,Electronics,549,1,7,31",
    "2026-01-01,P002,Keyboard,Electronics,899,0,80,10",
    "2026-01-02,P002,Keyboard,Electronics,899,0,70,11",
    "2026-01-05,P002,Keyboard,Electronics,849,1,40,19",
    "2026-01-06,P002,Keyboard,Electronics,849,1,21,21"
]

def detect_demand_changes(data_lines):
    sales_list = []
    product_set = set()
    demand_dict = {}

    # 1. Parse data into Tuples and add to List and Set
    for line in data_lines:
        date, prod_id, name, cat, price, promo, stock, sold = line.split(",")
        
        # TUPLE: Immutable daily record
        record = (date, prod_id, name, cat, float(price), int(promo), int(stock), int(sold))
        sales_list.append(record) # LIST
        product_set.add(prod_id)   # SET (Unique products)

    # 2. Group data by Product ID using a Dictionary
    for prod_id in product_set:
        demand_dict[prod_id] = {
            "Name": "",
            "normal_sales": [],
            "promo_sales": []
        }

    for record in sales_list:
        date, prod_id, name, cat, price, promo, stock, sold = record
        demand_dict[prod_id]["Name"] = name
        
        if promo == 0:
            demand_dict[prod_id]["normal_sales"].append(sold)
        else:
            demand_dict[prod_id]["promo_sales"].append(sold)

    # 3. Analyze Demand Changes (Comparing normal vs promo average)
    print("--- Product Demand Change Detector Report ---")
    for prod_id, data in demand_dict.items():
        normals = data["normal_sales"]
        promos = data["promo_sales"]
        
        avg_normal = sum(normals) / len(normals) if normals else 0
        avg_promo = sum(promos) / len(promos) if promos else 0
        
        # Calculate percentage change in demand
        if avg_normal > 0:
            change_pct = ((avg_promo - avg_normal) / avg_normal) * 100
        else:
            change_pct = 0
            
        print(f"\nProduct: {data['Name']} (ID: {prod_id})")
        print(f"  - Baseline Avg Demand (Normal): {avg_normal:.1f} units")
        print(f"  - Promotional Avg Demand: {avg_promo:.1f} units")
        print(f"  - Demand Shift: {change_pct:+.1f}%")
        
        if change_pct > 50:
            print("  ⚠️ [ALERT]: Significant demand surge detected during promotions!")

# Run the detector
detect_demand_changes(raw_data)