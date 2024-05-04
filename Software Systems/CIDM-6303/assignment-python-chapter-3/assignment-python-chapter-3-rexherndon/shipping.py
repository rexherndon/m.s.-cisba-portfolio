# Determines the shipping cost based on the ship_to_state.
# When testing, change the ship_to_state to various state abreviations
# to verify your code works for all conditions.

print("Enter a state to ship to (e.g. TX, NM, OK, NY, AK, HI, etc.):")
ship_to_state = input()

if ship_to_state.upper() == ("TX" or "NM" or "OK"):
    print(f"Shipping to {ship_to_state.upper()} costs 0")
elif ship_to_state.upper() == ("NY"):
    print(f"Shipping to {ship_to_state.upper()} costs 7")
elif ship_to_state.upper() == ("AK"):
    print(f"Shipping to {ship_to_state.upper()} costs 15.75")
elif ship_to_state.upper() == ("HI"):
    print(f"Shipping to {ship_to_state.upper()} costs 20")
else:
    print(f"Shipping to {ship_to_state.upper()} costs 12.5")






