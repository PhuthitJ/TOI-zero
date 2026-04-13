import sys

line1 = sys.stdin.readline()
if not line1:
    exit()
n = int(line1.strip())

for _ in range(n):
    original_text = sys.stdin.readline().rstrip('\n\r')
    
    lower_text = original_text.lower()
    words = lower_text.split()

    if "hello" in words or "hi" in words:
        print("Hello! How can I help you?")
    
    elif "bye" in words or "goodbye" in words:
        print("Goodbye! Have a nice day!")
    
    elif original_text.endswith('?'):
        print("That's an interesting question!")
    
    elif any(char.isdigit() for char in original_text):
        print("I see some numbers there!")
    
    elif len("".join(original_text.split())) > 19:
        print("That's quite a long message!")
    
    else:
        print("I understand.")