# Name: Theresa Quach
# Course: CS361
# Project: Assignment#7: Cue Card Editing microservice for Christopher Irwin

import time

cont = 1                                                                                                                # Global variable to keep function running in editing mode; == 0 means editing mode has ended.

def editcard():
    """
    Function that, if it reads the line "save" a first time in the document 'tempsave.txt', will enter editing mode and save the line passed to it 
    by the current program. If it reads the line "undo", will return the saved line 
    """
    global cont

    # Open and read the first line from the file and strip off newline to get action
    fd = open("tempsave.txt","r+")
    action = fd.readline()
    action = action.strip('\n')

    # If action is "save", enter editing mode
    if (action == "save"):
        cont = 1
        print("Editing mode on")
        # Save the original line
        saved_line = ""
        line = fd.readline()
        saved_line = line.strip('\n')
        # While still in editing mode
        while (cont):
            fd.seek(0)
            action = fd.readline()
            action = action.strip('\n')
            # If microservice is told to save a new change
            if (action == "save"):
                line = fd.readline()
                saved_line = line.strip('\n')
                #print("New line saved.")                                                                               # commented out line check
                #print(saved_line)
            if (action == "undo"):
                fd.seek(0)
                fd.truncate(0)
                fd.write(saved_line)
                print(saved_line)
            # If microservice is told to exit editing mode, return the most current saved line
            if (action == "end"):
                fd.seek(0)
                fd.truncate(0)
                fd.write(saved_line)
                cont = 0
                print("Editing mode off.")
                print(saved_line)
                break
    
    fd.close()




if __name__ == '__main__':
    print("Card Editing Program running.")
    while True:
        time.sleep(1)
        editcard()