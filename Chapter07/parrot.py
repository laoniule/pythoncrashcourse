prompt="\nTell me something, and I will repeat it back to you!"
prompt+="\nEnter 'quit' to end programe.\n"

message=""

while message!='quit':
    message=input(prompt)

    if message!='quit':
        print(message)