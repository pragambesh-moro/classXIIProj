def gen_bill():
    import datetime as dt
    import json
    import main
    pc = json.dumps(main.cart_items, indent=4)
    with open('bill.txt', 'w') as f:
        f.write("######################################\n")
        f.write("          E-RETAIL-PLATFORM           \n")
        f.write(f"Customer ID: {main.ui}\n")
        f.write(f"Customer Name: {main.ui}\n")
        f.write(f"Date and Time: {dt.datetime.now()}\n")
        f.write("\n")
        f.write("\n")
        f.write(f"Cart: {pc}\n")
        f.write("\n")
        f.write("\n")
        f.write(f"             Total Cost: {main.total_cost}\n")
        f.write("######################################")


