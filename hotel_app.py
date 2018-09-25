# Let's imagine that you're running a hotel, 
# and you want to keep track of guests by floor 
# and room number:

# Write a program that works with this hotel data:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.


hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
    '102': [],
    '103': [],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
    '238': [],
    '239': [],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus'],
    '334': [],
    '335': [],
  }
}

bad_input = True

while bad_input:
    check_in = input("Checking in? ").lower()
    if check_in == "yes":
        floor_number = ''
        while floor_number not in hotel:
            floor_number = input("Floor number? ")
        room_number = ''
        while room_number not in hotel[floor_number]:
            room_number = input("Room number? ")
        num_occupants = 0
        while num_occupants <= 0:
            try:
                num_occupants = int(input("Number of occupants? "))
            except:
                num_occupants = 0
        occupant_names = []
        while len(occupant_names) < num_occupants:
            occupant_name = input("Who is occupant #%d? " % (len(occupant_names) + 1))
            if occupant_name not in occupant_names:
                occupant_names.append(occupant_name)
        if hotel[floor_number][room_number] == []:
            hotel[floor_number][room_number] = occupant_names
            print("Enjoy your stay.")
            bad_input = False
    else:
        check_out = input("Checking out? ").lower()
        if check_out == "yes":
            floor_number = ''
            while floor_number not in hotel:
                floor_number = input("Floor number? ")
            room_number = ''
            while room_number not in hotel[floor_number]:
                room_number = input("Room number? ")
            if hotel[floor_number][room_number] != []:
                hotel[floor_number][room_number] = []
                print("Thanks for staying with us. Goodbye.")
                bad_input = False

print(hotel)