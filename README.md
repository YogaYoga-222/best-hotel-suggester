# Best Hotel Suggester

This is a simple Python project that helps users find the best hotel to stay based on their **budget** and **hotel ratings**. The project uses basic Python and `pandas` to filter and suggest the most suitable hotel(s).

---

## Project Files

- `hotel_recommender.py`  
  → Loads hotel data from a CSV file and recommends the best hotels under the user's budget.

- `hotel_recommender_1.py`  
  → Lets the user manually enter hotel information and then recommends the best hotel under their budget.

---

## How It Works

### `hotel_recommender.py`
- Reads hotel data from a `.csv` file
- Asks the user for their budget
- Filters hotels within that budget
- Sorts the hotels by rating (highest first)
- Recommends the best options

### `hotel_recommender_1.py`
- Takes input for 4 hotels from the user (name, rating, cost)
- Asks for the user's budget
- Filters hotels based on the given budget
- Sorts hotels by rating (highest first)
- Recommends the best hotel(s)

---

## Sample Dataset (CSV Format)

If you're using `hotel_recommender.py`, create a CSV file like below:

```csv
Hotel,Rating,Cost
Green View,4.5,1500
City Lodge,3.8,1000
Luxury Stay,4.9,2500
Budget Inn,3.2,800
```
------
## Requirements

```bash
pip install pandas
```
-------
## How to Run

```bash
python3 hotel_recommender.py
```
or

```bash
python3 hotel_recommender_1.py
```
