# Define a dictionary to store the game state  
game_state = {  
  "current_room": "start",  
  "inventory": []  
}  
  
# Define a dictionary to store the rooms  
rooms = {  
  "start": {  
   "description": "You are standing at the entrance of a dark cave.",  
   "exits": ["north", "south"],  
   "items": ["torch"]  
  },  
  "north_room": {  
   "description": "You are in a narrow corridor.",  
   "exits": ["south", "east"],  
   "items": []  
  },  
  "south_room": {  
   "description": "You are in a large chamber.",  
   "exits": ["north", "west"],  
   "items": ["key"]  
  },  
  "east_room": {  
  "description": "You are in a small room.",  
  "exits": ["west"],  
   "items": ["treasure"]  
  }  
}  
  
# Define a function to print the current room description  
def print_room_description():  
  room = rooms[game_state["current_room"]]  
  print(room["description"])  
  print("Exits:", ", ".join(room["exits"]))  
  print("Items:", ", ".join(room["items"]))  
  
# Define a function to handle user input  
def handle_input(input_text):  
 # Split the input into words  
  words = input_text.split()  
 
  # Handle movement commands  
  if words in ["go", "move"]:  
   direction = words  
   if direction in rooms[game_state["current_room"]]["exits"]:  
 game_state["current_room"] = direction + "_room"  
 print_room_description()  
  else:  
 print("You can't go that way.")  
 
  # Handle take commands  
  elif words == "take":  
  item = words  
   if item in rooms[game_state["current_room"]]["items"]:  
 game_state["inventory"].append(item)  
   rooms[game_state["current_room"]]["items"].remove(item
 print("You took the", item)  
   else:  
   print("There is no", item, "here.")  
  # Handle inventory command  
  elif words == "inventory":  
   print("You have:", ", ".join(game_state["inventory"]))  
 
  # Handle unknown commands  
  else:  
 print("Unknown command. Try 'go', 'take', or 'inventory'.")  
  
# Start the game  
print_room_description()  
  
# Loop until the user quits  
while True:  
  input_text = input("> ")  
  if input_text.lower() == "quit":  
   break  
handle_input(input_text)