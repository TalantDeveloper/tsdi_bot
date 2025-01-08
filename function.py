import sqlite3


def create_table():  # Create Table
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()

        create_table_query = """CREATE TABLE IF NOT EXISTS Rectors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, voice INTEGER);"""

        # Execute the SQL command
        cursor.execute(create_table_query)

        # Commit the changes
        connection.commit()

        print('Connected to database')


# create_table()


def insert_data():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()

        insert_query = """INSERT INTO Rectors (name, voice) VALUES (?, ?)"""
        rector = ("Ergashov Botirjon", 0)
        cursor.execute(insert_query, rector)
        connection.commit()
        print('Connected to database')


# insert_data()


def read_data():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        select_query = """SELECT * FROM Rectors;"""
        cursor.execute(select_query)
        rectors = cursor.fetchall()
        data = []
        print("All Rectors")
        for rector in rectors:
            dat = [rector[0], rector[1], rector[2]]
            data.append(dat)
        return data


print(read_data())


def update_data():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        update_query = """UPDATE Rectors SET name = ?, voice = ? WHERE id = ?;"""

        name = "Xaydarov Nodir"
        voice = 0
        id = 2
        cursor.execute(update_query, (name, +1, id))
        connection.commit()

        print(read_data())


# update_data()


def update_rector_voice(rector_id):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        data = read_data()[rector_id]
        update_query = """UPDATE Rectors SET voice = ? WHERE id = ?;"""
        voice = data[2] + 1
        cursor.execute(update_query, (voice, rector_id + 1))
        connection.commit()
        print(read_data())


# update_rector_voice(0)





# def result_add(index):
#     with open('index.txt', 'r') as f:
#         result = f.readlines()
#         results = []
#         for i in result:
#             results.append(int(i))
#         print(results)
#         results[index] += 1
#         print(results)
#         for i in results:
#             with open('index.txt', 'a') as fas:
#                 fas.write(str(i))
#
#
#
#
# result_add(1)
