'''
Jake
IS 303 - A01

Event Budget Calculator
This program estimates the total cost of a campus event based on
the number of attendees, cost per person, and a venue fee.

Inputs:
- Event name (string)
- Number of attendees (int)
- Cost per person (float)
- Venue fee (float)

Processes:
- Convert attendees, cost, and venue fee to numbers
- Calculate subtotal: attendees * cost per person
- Calculate total cost: subtotal + venue fee
- Calculate cost per attendee including venue fee

Outputs:
- Print the event name, attendee count, subtotal, venue fee, and total cost
- Print effective cost per attendee
'''

event_name = input("What is the event name? ")
attendees = int(input("How many attendees do you expect? "))
cost_per_person = float(input("What is the cost per person? "))
venue_fee = float(input("What is the venue fee? "))

subtotal = attendees * cost_per_person
total_cost = subtotal + venue_fee
effective_cost = total_cost / attendees

print("---")
print(f"{event_name} | {attendees} attendees | ${cost_per_person:.2f} per person")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Venue fee: ${venue_fee:.2f}")
print(f"Estimated total cost: ${total_cost:.2f}")
print(f"Effective cost per attendee: ${effective_cost:.2f}")

