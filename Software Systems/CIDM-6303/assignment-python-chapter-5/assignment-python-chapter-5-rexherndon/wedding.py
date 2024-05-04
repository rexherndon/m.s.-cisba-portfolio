# Follow the instructions for how to code this application

guest_list = []

print("Welcome to the guest list application!\n" + "-" * 30)

counter = 0
while True:
    add_to_list = input("Enter a guest's name or type \"end\" to stop adding guests: ")
    if add_to_list.lower() == "end":
        break
    added_to_guest_list = guest_list.append(add_to_list)
    counter += 1

for guest in guest_list:
    print(guest)

total_food_cost = counter * 12

print(f"You have invited {counter} guests at a cost of ${total_food_cost:.2f}")