blocks = []

while True:
    try:
        line = input().strip()
        if not line:
            continue
            
        prev_hash, current_hash = map(int, line.split())
        blocks.append((prev_hash, current_hash))
        
        if current_hash == 0:
            break
    except EOFError:
        break

def check_blockchain(index):
    if index == len(blocks) - 1:
        return
    
    check_blockchain(index + 1)
    
    current_hash = blocks[index][1]
    next_prev_hash = blocks[index + 1][0]
    
    block_num = index + 1
    if current_hash == next_prev_hash:
        print(f"{block_num}P")
    else:
        print(f"{block_num}X")

if len(blocks) <= 1:
    print("1X")
else:
    check_blockchain(0)