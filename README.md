# Microservice: Cue-Card-Editor
# Written by Theresa Quach
# For Christopher Irwin - CS361 Partner Microservice Implementation.

This program is a microservice that enables editing (saving and undoing) lines on cue cards of the main program and requires input from a UI. As previously agreed, this microservice will use a text file (tempsave.txt) as its communication pipeline with the main program. 


Requesting data from the microservice:
1. To begin interacting with the microservice, the user will enter editing mode on the UI. Entering "Editing" mode means that the main program writes "save" on the first line of 'tempsave.txt', and the JSON line found on the cuecard being edited to the second line. The microservice will read this action ('save') and store the JSON text found on the second line in a variable for the duration of editing mode.
2. To save a new change to the cue card, the user will click "Save" on the UI of the main program. The main program writes the action 'save' to the text file tempsave.txt along with the new line (JSON format) to be stored, which the microservice will store.
3. To undo a change within the UI, The user will hit "Undo", which causes the main program writes 'undo' to tempsave.txt, which the microservice will read and return the most recently saved line.
4. To end editing mode, the user will click out of the card being edited, which causes the main program to write 'end' to the text document pipe and wait for the microservice to return the last saved line.


Receiving data from the microservice:
1. The microservice will not return a newly saved line immediately once a change is saved - instead, the new line is stored in a the microservice until the user clicks out of editing mode. By existing, the main program writes 'end' into the communication text file, which the microservice will read and return the saved line to the main program through the same text file.
2. The user can request to see what the most recent saved line to the card is by clicking undo, which will cause the main program to write 'undo' into the text file and wait for the microservice to return the most recent saved line for that card.
