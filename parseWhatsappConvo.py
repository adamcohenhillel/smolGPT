import re

with open('_chat.txt', 'r', encoding='utf-8') as f:
    chat_text = f.read()

# Define a regular expression pattern for the chat format
pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')

# Find all matches in the chat text
matches = pattern.findall(chat_text)

# Extract and print the components of each message
with open('output.txt', 'w+', encoding='utf-8') as f:
    last_sender = None
    for match in matches:
        timestamp, sender, message = match

        if sender != last_sender:
            if sender == "Adam Cohen hillel":
                f.write(f"\nאדם:")
            else:
                f.write(f"\nאמא:")
            last_sender = sender
        f.write(f"{message}\n")
