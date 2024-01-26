import os

if(os.path.exists('chats_no_empty_lines.txt')):
    os.remove("chats_no_empty_lines.txt")

to_write = open("chats_no_empty_lines.txt", "w")
with open("chats.txt", "r") as file:
    for line in file:
        stripped_line = line.strip();
        if stripped_line:
            to_write.write(stripped_line + '\n')
to_write.close()