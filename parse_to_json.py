import json
import os

# remove embeds, gifs, attachments, reactions
# result is only text messages

users_to_view = set()

while True:
    try:
        user = input('Enter user to include (\'done\' to continue): ')
        if user == 'done':
            break
        else:
            users_to_view.add(user)
    except ValueError:
        print("Value error")
        continue;

if(os.path.exists('filtered_conversation.txt')):
    os.remove("filtered_conversation.txt")
    
to_write = open("filtered_conversation.txt", "w")

with open('chats.txt', 'r') as file:
    is_message = False
    user_message = ""
    for line in file:
        stripped_line = line.strip()
        # previous line was user, so message flag is true and current line is processed as a message
        if is_message and stripped_line and 'https://' not in stripped_line and 'http://' not in stripped_line:
            user_message += stripped_line
            to_write.write(user_message + '\n')
            # print(user_message)
            is_message = False
            user_message = ""
        else:
            is_message = False;
            user_message = ""


        # get user and their chat message
        # checks if current line is a message timestamp with a user
        if stripped_line and stripped_line[0] == '[' and 'M] ' in stripped_line: # denotes a message timestamp
            index = stripped_line.find('M] ') + 3  # 3 characters in 'M] '
            user = stripped_line[index:].strip()
            if user in users_to_view:
                # print(user, end = ": ")
                user_message += (user + ": ")
                is_message = True

to_write.close()

# parse raw text to q/a json