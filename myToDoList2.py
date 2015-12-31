#make a list to hold our items
todo_list = []

#print out instructions on how to use the app
def show_help():
    print("What should we do today?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see the current list.
""")

show_help()

def show_list():
    #print out the list
    print("Here's your list:")

    for each in todo_list:
        print("~ " + each)

def add_to_list():
    #add new items
    todo_list.append(new_item)
    print("Added {}.  List now has {} items.".format(new_item, len(todo_list)))

while True:
    #ask for new items to be added
    new_item = input("~ ")
    
    #be able to quit app
    if new_item == "DONE":
        show_list()
        break
    
    #have a HELP cmd
    elif new_item == "HELP":
        show_help()
        continue
    
    #have a SHOW cmd
    elif new_item == "SHOW":
        show_list()
        print("Continue adding to your list.")
        continue

    add_to_list()
     
      



