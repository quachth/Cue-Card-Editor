# Name: Theresa Quach
# Course: CS361
# Project: Assignment#7: Testing program for Cue Card Editing microservice for Christopher Irwin


if __name__ == '__main__':
    # open the communication pipeline with microservice
    default_line = "{'Card Front':'Some text', 'Card Back':'Some text'}"
    line = default_line
    print("Test UI running")
    while True:
        fd = open("tempsave.txt", "r+")
        action = input()
        action = action.strip('\n')
        if (action == "edit"):
            print("Now editing")
            fd.write("save\n")
            fd.write(default_line)
            print("Original line is: ", default_line)
        if (action == "end"):
            fd.seek(0)
            fd.truncate(0)
            fd.write("end")
            fd.close()
            break
        if (action == "save"):
            line = input()
            fd.seek(0)
            fd.truncate(0)
            fd.write("save\n")
            fd.write(line)
        if (action == "undo"):
            print(line)
        fd.close()



