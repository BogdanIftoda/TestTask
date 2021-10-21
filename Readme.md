# Test Task

Console application for cost control.

## Table of contents
<h3>
  • <a href="#installation">Installation</a><br>
  • <a href="#how-to-use">How To Use</a><br>
</h3>

## Installation

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/BogdanIftoda/TestTask.git

# Go into the repository
$ cd TestTask

# create database
$ python create_database.py

# Run the app
$ python test_task.py
```

## How To Use

To add costs, enter **1**, and then enter category and money with a hyphen, if you do not enter a date, today's date will be added automatically.

#### Output
```text
Choose what you need, enter number:
1. Add expenses
2. Get all categories
3. Get one category
4. Clear all

1
Enter category and money: Food - 250
Record added
```

To add a category with a date, enter the date after the money.

#### Output
```text
Enter category and money: Gym - 250 10-11-2020
Record added
```

Press **'q'** to close adding categories, and then enter **2** to get all categories

#### Output
```text
All records
----------
1 Food 250 21-10-2021
2 Gym 250 10-11-2020
3 Cinema 100 21-10-2021
4 Taxi 120 21-10-2021
----------
```

To get a specific category enter **3**, and then write the name of the category

#### Output
```text
Enter category name: Food

Category Food
----------
1 Food 250 21-10-2021
5 Food 400 10-11-2010
6 Food 350 05-06-2021
----------
```

Enter **4** to clear all data

#### Output
```text
Data cleared
```

Press **'q'** to close the application

