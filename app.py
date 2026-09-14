# ============================================================
# PRODUCT DEMAND CHANGE DETECTOR
# ============================================================

# -----------------------------
# 1. DATASET
# -----------------------------

# ============================================================
# PRODUCT DEMAND CHANGE DETECTOR
# ============================================================

# -----------------------------
# DATASET
# -----------------------------

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


# ============================================================
# FUNCTION TO DETECT DEMAND CHANGES
# ============================================================

def detect_demand_changes(data_lines):

    # LIST
    # Stores all sales records
    sales_list = []

    # SET
    # Stores unique product IDs
    product_set = set()

    # DICTIONARY
    # Stores product-wise information
    demand_dict = {}


    # ========================================================
    # LOOP 1: READ EVERY RECORD
    # ========================================================

    for line in data_lines:

        # Split the CSV line
        date, prod_id, name, category, price, promo, stock, sold = line.split(",")

        # Convert values to correct data types
        record = (
            date,
            prod_id,
            name,
            category,
            float(price),
            int(promo),
            int(stock),
            int(sold)
        )

        # Add record to list
        sales_list.append(record)

        # Add product ID to set
        product_set.add(prod_id)


    # ========================================================
    # LOOP 2: CREATE STORAGE FOR EACH PRODUCT
    # ========================================================

    for prod_id in product_set:

        demand_dict[prod_id] = {
            "Name": "",
            "normal_sales": [],
            "promo_sales": []
        }


    # ========================================================
    # LOOP 3: SEPARATE NORMAL AND PROMOTIONAL SALES
    # ========================================================

    for record in sales_list:

        date, prod_id, name, category, price, promo, stock, sold = record

        # Store product name
        demand_dict[prod_id]["Name"] = name

        # IF/ELSE
        # Check whether promotion was active

        if promo == 0:

            # Normal sale
            demand_dict[prod_id]["normal_sales"].append(sold)

        else:

            # Promotional sale
            demand_dict[prod_id]["promo_sales"].append(sold)


    # ========================================================
    # LOOP 4: ANALYZE EACH PRODUCT
    # ========================================================

    print("\n")
    print("=" * 65)
    print("             PRODUCT DEMAND CHANGE DETECTOR")
    print("=" * 65)

    for prod_id, data in demand_dict.items():

        product_name = data["Name"]
        normal_sales = data["normal_sales"]
        promo_sales = data["promo_sales"]


        # ----------------------------------------------------
        # Calculate normal average demand
        # ----------------------------------------------------

        if len(normal_sales) > 0:

            avg_normal = sum(normal_sales) / len(normal_sales)

        else:

            avg_normal = 0


        # ----------------------------------------------------
        # Calculate promotional average demand
        # ----------------------------------------------------

        if len(promo_sales) > 0:

            avg_promo = sum(promo_sales) / len(promo_sales)

        else:

            avg_promo = 0


        # ----------------------------------------------------
        # Calculate percentage change
        # ----------------------------------------------------

        if avg_normal > 0:

            change_pct = (
                (avg_promo - avg_normal)
                / avg_normal
            ) * 100

        else:

            change_pct = 0


        # ====================================================
        # DISPLAY PRODUCT INFORMATION
        # ====================================================

        print("\nProduct Name :", product_name)
        print("Product ID   :", prod_id)

        print(
            "Normal Demand Average      :",
            f"{avg_normal:.1f}",
            "units"
        )

        print(
            "Promotional Demand Average :",
            f"{avg_promo:.1f}",
            "units"
        )

        print(
            "Demand Change              :",
            f"{change_pct:+.1f}%"
        )


        # ====================================================
        # IF / ELIF / ELSE DEMAND DETECTION
        # ====================================================

        if change_pct > 50:

            print("Status : 🚨 SIGNIFICANT DEMAND SURGE")

        elif change_pct < -50:

            print("Status : 🚨 SIGNIFICANT DEMAND DROP")

        else:

            print("Status : ✅ DEMAND IS WITHIN NORMAL RANGE")

        print("-" * 65)


# ============================================================
# MAIN PROGRAM
# ============================================================

print("=" * 65)
print("          WELCOME TO PRODUCT DEMAND DETECTOR")
print("=" * 65)

print("\n1. Analyze Product Demand")
print("2. Exit")


# ============================================================
# USER INPUT
# ============================================================

choice = input("\nEnter your choice (1 or 2): ")


# ============================================================
# IF / ELSE FOR MENU
# ============================================================

if choice == "1":

    print("\nStarting Product Demand Analysis...")

    detect_demand_changes(raw_data)


elif choice == "2":

    print("\nProgram exited.")
    print("Thank you for using Product Demand Detector!")


else:

    print("\nInvalid choice!")
    print("Please enter 1 or 2.")


# ============================================================
# END OF PROGRAM
# ============================================================
