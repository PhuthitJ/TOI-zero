# Condition Number in Text is wrong.

n = int(input())
texts = []
for _ in range(n):
    texts.append((input().lower()).split())

answer = []

for i in range(n):
    if "hello" in texts[i] or 'hi' in texts[i]:
        answer.append("Hello! How can I help you?")
    elif "bye" in texts[i] or 'goodbye' in texts[i]:
        answer.append("Goodbye! Have a nice day!")
    elif '?' in texts[i][-1]:
        answer.append("That's an interesting question!")
    elif any(char.isdigit() for char in texts[i]):
        print("I see some numbers there!")
    elif sum(len(text) for text in texts[i]) > 19:
        answer.append("That's quite a long message!")
    else:
        answer.append("I understand.")

print(answer)