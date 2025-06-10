# Store hotel data
hotels = []

# Get data for 4 hotels
for i in range(4):
    print(f"\nEnter details for Hotel {i+1}:")
    name = input("Hotel Name: ")
    rating = float(input("Rating (out of 5): "))
    cost = int(input("Hotel Cost: "))
    
    # Save each hotel as a dictionary
    hotel = {"name": name, "rating": rating, "cost": cost}
    hotels.append(hotel)

# Ask for user's budget
budget = int(input("\nEnter your budget: "))

# Filter hotels within budget
within_budget = []
for hotel in hotels:
    if hotel["cost"] <= budget:
        within_budget.append(hotel)

# Sort hotels by rating (highest first)
sorted_hotels = sorted(within_budget, key=lambda x: x["rating"], reverse=True)

# Show result
print("\nBest hotel(s) within your budget:")
if sorted_hotels:
    for hotel in sorted_hotels:
        print(f"{hotel['name']} - Rating: {hotel['rating']} - Cost: {hotel['cost']}")
else:
    print("Sorry, no hotels available within your budget.")


