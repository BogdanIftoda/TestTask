import sqlite3
from datetime import date


today = date.today().strftime("%d-%m-%Y")

connection = sqlite3.connect('test.db')
cur = connection.cursor()


def add_records():
    while True:
        user_input = input("Enter category and money: ")
        if user_input.lower() == 'q':
            break
        else:
            user_input = user_input.replace('-', ' ').split()
            category, money, *date = user_input
            try:
                money = int(money)
            except:
                print('Value money is not a number')
                continue
            date = '-'.join(date)
            if date:
                cur.execute("INSERT INTO category(name, money, date) VALUES(:category, :money, :date);",
                            {'category': category.rstrip(), 'money': money, 'date': date})
            else:
                cur.execute("INSERT INTO category(name, money, date) VALUES(:category, :money, :date);",
                            {'category': category.rstrip(), 'money': money, 'date': today})
            connection.commit()
            print("Record added")


def show_records(category_name=None):
    if category_name:
        cur.execute("SELECT * FROM category where name=:category_name;",
                    {"category_name": category_name})
    else:
        cur.execute("SELECT * FROM category;")
    result = cur.fetchall()
    if len(result) != 0:
        print('----------')
        for row in result:
            print(*row)
        print('----------')
    else:
        print("No records")


while True:
    input_value = input('''
Choose what you need, enter number:
1. Add expenses
2. Get all categories
3. Get one category
4. Clear all

''')
    if input_value.lower() == 'q':
        break
    elif int(input_value) == 1:
        add_records()
    elif int(input_value) == 2:
        print("\nAll records")
        show_records()
    elif int(input_value) == 3:
        category_name = input("Enter category name: ")
        print(f"\nCategory {category_name}")
        show_records(category_name)
    elif int(input_value) == 4:
        cur.execute("DELETE FROM category;")
        connection.commit()
        print('Data cleared')
    else:
        print('Wrong number')