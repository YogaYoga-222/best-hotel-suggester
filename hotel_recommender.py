import pandas as pd

# Load data
df = pd.read_csv("/home/stemland/Documents/hotel_data.csv") 

# Get user's budget
budget = int(input("Enter your budget: "))

# Filter hotels within budget
affordable_hotels = df[df["Cost"] <= budget]

# Sort by rating (highest first)
recommended = affordable_hotels.sort_values(by="Rating", ascending=False)

# Show the best hotel(s)
if not recommended.empty:
    print("\nBest hotel(s) within your budget:\n")
    print(recommended)
else:
    print("Sorry, no hotels are available within your budget.")

