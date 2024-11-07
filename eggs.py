def gen_bill():
    import datetime as dt
    import json
    import m2
    pc = json.dumps(m2.cart_items, indent=4)
    with open('bill.txt', 'w') as f:
        f.write("######################################\n")
        f.write("          E-RETAIL-PLATFORM           \n")
        f.write(f"Customer ID: {m2.ui}\n")
        f.write(f"Customer Name: {m2.uxname}\n")
        f.write(f"Date and Time: {dt.datetime.now()}\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write(f"             Total Cost: {m2.total_cost}\n")
        f.write("######################################")

gen_bill()