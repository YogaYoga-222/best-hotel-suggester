# Best Hotel Suggester

This project helps users find the best hotel to stay based on their **budget**, **rating**, and **cost**. It includes three different approaches, including one using **Logistic Regression**.

---

## Project Files

- `hotel_recommender.py`  
  → Loads hotel data from a CSV file and recommends hotels within the user's budget based on rating.

- `hotel_recommender_1.py`  
  → Lets the user manually enter hotel details and recommends the best option under their budget.

- `hotel_recommender_2.py`  
  → Uses **Logistic Regression** to predict whether a customer will stay at a hotel based on cost, rating, and budget.

---

## How Each Script Works

### `hotel_recommender.py`
- Reads hotel data from a CSV file
- Asks for user's budget
- Filters and sorts hotels based on rating
- Displays hotels under budget

### `hotel_recommender_1.py`
- Takes hotel info as input from the user
- Asks for user's budget
- Suggests best option(s) using simple filtering and sorting

### `hotel_recommender_2.py`
- Uses `scikit-learn` to train a **Logistic Regression model**
- Predicts if a user will choose to stay at a hotel based on:
  - Rating
  - Hotel Cost
  - Customer Budget
- Prints accuracy, confusion matrix, and prediction

---

## Sample CSV Format (for `hotel_recommender.py`)

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

## How to Run This Project

1. Clone the repository:

 ```bash
 git clone git@github.com:YogaYoga-222/best-hotel-suggester.git
 cd best-hotel-suggester
 ```
2.Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```
3.Install dependencies:

```bash
pip install -r requirements.txt
```
4.Run the desired script:

```bash
python3 hotel_recommender.py
```
or
```bash
python3 hotel_recommender_1.py
```
or
```bash
python3 hotel_recommender_2.py
```
> **Note:** Use `python` if `python3` doesn't work on your system.
---------

## What You'll Learn

* How to filter and sort hotel data based on cost and rating
* How to take user input and process it
* How to use Logistic Regression for binary classification (e.g., will the user stay or not)


