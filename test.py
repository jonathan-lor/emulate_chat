import json


ignore_keywords = {'{Embed}', '{Reactions}'}

with open('chats.txt', 'r') as file:
    skip = False
    for line in file:
        stripped_line = line.strip();

        if '{Embed}' in stripped_line or '{Reactions}' in stripped_line:
            skip = True  # Start skipping lines
            continue

        # Check if the line is empty, indicating the end of a section to skip
        if skip and not stripped_line:
            skip = False  # Stop skipping lines
            continue

        if not skip and 'http://' not in stripped_line and 'https://' not in stripped_line:
            print(stripped_line)

        # if stripped_line and not any(keyword in stripped_line for keyword in ignore_keywords) and 'http://' not in stripped_line and 'https://' not in stripped_line:
        #     print(stripped_line)
        #print(line.strip())