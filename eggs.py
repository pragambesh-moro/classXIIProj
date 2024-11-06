def gen_bill():
    import datetime as dt
    import json
    from prod import ui, uxname, total_cost, cart_items
    pc = json.dumps(cart_items, indent=4)
    with open('bill.txt', 'w') as f:
        f.write("######################################\n")
        f.write("          E-RETAIL-PLATFORM           \n")
        f.write(f"Customer ID: {ui}\n")
        f.write(f"Customer Name: {uxname}\n")
        f.write(f"Date and Time: {dt.datetime.now()}\n")
        f.write("\n")
        f.write("\n")
        f.write(f"             Total Cost: {total_cost}\n")
        f.write("######################################")


gen_bill()