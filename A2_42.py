commands = []

while True:
    try:
        command = input().strip()
        if not command:
            continue
        if command == "END":
            break
        commands.append(command.split())
    except EOFError:
        break

stock = {}
outputs = []

for cmd in commands:
    op = cmd[0]
    
    if op == "ADD":
        name = cmd[1]
        qty = int(cmd[2])
        if name in stock:
            stock[name] += qty
        else:
            stock[name] = qty
            
    elif op == "REMOVE":
        name = cmd[1]
        qty = int(cmd[2])
        current_qty = stock.get(name, 0)
        
        if qty > current_qty:
            outputs.append(f"Not enough stock for {name}")
            if name in stock:
                del stock[name]
        else:
            stock[name] -= qty
            if stock[name] == 0:
                del stock[name]
                
    elif op == "CHECK":
        low_stocks = []
        for name, qty in stock.items():
            if qty < 5:
                low_stocks.append(name)
                
        if len(low_stocks) == 0:
            outputs.append("All stocks are sufficient")
        else:
            low_stocks.sort()
            for name in low_stocks:
                outputs.append(name)
                
    elif op == "REPORT":
        sorted_items = sorted(stock.items())
        for name, qty in sorted_items:
            outputs.append(f"{name}: {qty}")

for out in outputs:
    print(out)