name = input("Enter your name to store in file or enter to proceed: ")

if name:
    open("user_info.txt", "a").write(name + "\n")

if input("Do you want to see all user names? y/n: ") == "y":
    try:
        for line in open("user_info.txt"):
            print(line.strip())
    except Exception as e:
        print(e)