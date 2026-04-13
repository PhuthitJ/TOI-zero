n = int(input())
answers = []
for _ in range(n):
    original_text = input()
    lower_text = original_text.lower()
    words = lower_text.split()

    if "hello" in words or "hi" in words:
        answers.append("Hello! How can I help you?")
    
    elif "bye" in words or "goodbye" in words:
        answers.append("Goodbye! Have a nice day!")
    
    elif original_text.endswith('?'):
        answers.append("That's an interesting question!")
    
    elif any(char.isdigit() for char in original_text):
        answers.append("I see some numbers there!")
    
    elif len(original_text.replace(" ", "")) > 19:
        answers.append("That's quite a long message!")
    
    else:
        answers.append("I understand.")

for answer in answers:
    print(answer)