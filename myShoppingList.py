#make a list to hold our items

todo_list = []

#print out instructions on how to use the app

print("What should we do today?")
print("Enter 'Done' to stop adding items.")

while True:
    #ask for new items to be added
    new_item = input("~ ")
    #be able to quit app
    if new_item == "Done":
        break

    #add new items
    todo_list.append(new_item)  
      
#print out the list
print("Here's your list:")

for each in todo_list:
    print("~ " + each)

