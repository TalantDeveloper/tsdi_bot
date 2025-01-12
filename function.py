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


# print(read_data())


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


# update_rector_voice(1)


def result_add(index):
    with open('index.txt', 'r') as f:
        result = f.readlines()
        results = []
        for i in result:
            results.append(int(i))
        print(results)
        results[index] += 1
        print(results)
        for i in results:
            with open('index.txt', 'a') as fas:
                fas.write(str(i))


# result_add(1)


def create_dekan_table():  # Create Dekan Table query
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()

        create_table_query = """CREATE TABLE IF NOT EXISTS dekan (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, voice INTEGER);"""
        cursor.execute(create_table_query)
        connection.commit()


# create_dekan_table()


def insert_dekan_table(dekan: tuple):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        insert_query = """INSERT INTO dekan (name, voice) VALUES (?, ?);"""
        cursor.execute(insert_query, dekan)
        connection.commit()


# dekan = ("dekan_name", 0)
# insert_dekan_table(dekan)


def read_dekan_table():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        read_query = """SELECT * FROM dekan;"""
        cursor.execute(read_query)
        dekans = cursor.fetchall()
        data = []
        for dekan in dekans:
            data.append(dekan)
        return data


# print(read_dekan_table())


def add_dekan_voice(dekan_id):
    dekan = read_dekan_table()[dekan_id - 1]
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        update_query = """UPDATE dekan SET voice = ? where id = ?;"""
        voice = dekan[2] + 1
        cursor.execute(update_query, (voice, dekan_id))
        connection.commit()


# add_dekan_voice(1)
# print(read_dekan_table())


def create_zamDekan_table():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        create_table_query = """CREATE TABLE IF NOT EXISTS zamDekan (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, voice INTEGER);"""
        cursor.execute(create_table_query)
        connection.commit()


# create_zamDekan_table()


def insert_zamDekan_table(name, voice):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        insert_zamDekan_query = """INSERT INTO zamDekan (name, voice) VALUES (?, ?);"""
        zamdekan = (name, voice)
        cursor.execute(insert_zamDekan_query, zamdekan)
        connection.commit()


# insert_zamDekan_table("SAFAROV JO‘RABEK FATULLAYEVICH", 0)
# insert_zamDekan_table("ASHUROV FERUZ RAXMATULLAYEVICH", 0)
# insert_zamDekan_table("ESHMURODOV SUNNATILLA G‘ULOMOVICH", 0)
# insert_zamDekan_table("ALIMOVA KOMILA DEKANOVNA", 0)


def read_zamDekan_table():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        select_zamDekan_query = """SELECT * FROM zamDekan;"""
        cursor.execute(select_zamDekan_query)
        zamDekans = cursor.fetchall()
        data = []
        for zamDekan in zamDekans:
            data.append(zamDekan)
        return data


# print(read_zamDekan_table())


def add_zamDekan_voice(zamDekan_id):
    zamDekan = read_zamDekan_table()[zamDekan_id - 1]
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        update_zamDekan_query = """UPDATE zamDekan SET voice = ? where id = ?;"""
        voice = zamDekan[2] + 1
        cursor.execute(update_zamDekan_query, (voice, zamDekan_id))
        connection.commit()


# add_zamDekan_voice(4)
# print(read_zamDekan_table())


def create_voter_table():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        voter_query = """CREATE TABLE IF NOT EXISTS voter (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, name TEXT NOT NULL, dekan INTEGER, zamDekan INTEGER);"""
        cursor.execute(voter_query)
        connection.commit()


# create_voter_table()


def insert_voter_table(user_id, name, dekan):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        voter_query = """INSERT INTO voter (user_id, name, dekan) VALUES (?, ?, ?);"""
        cursor.execute(voter_query, (user_id, name, dekan))
        connection.commit()


def read_voter_table():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        voter_query = """SELECT * FROM voter;"""
        cursor.execute(voter_query)
        voters = cursor.fetchall()
        data = []
        for voter in voters:
            data.append(voter)
        return data


def update_voter_table(user_id, zamDekan):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        voter_query = """UPDATE voter SET zamDekan = ? WHERE user_id = ?;"""
        cursor.execute(voter_query, (zamDekan, user_id))
        connection.commit()


def result_all():
    dekans = read_dekan_table()
    zamDekans = read_zamDekan_table()
    dekan_text = ""
    for dekan in dekans:
        dekan_text += f"{dekan[1]}  => {dekan[2]}\n"
    zamDekan_text = ""
    for zamDekan in zamDekans:
        zamDekan_text += f"{zamDekan[1]}  => {zamDekan[2]}\n"
    message = (f"Dekanlar bo'yicha natijalar:\n"
               f"{dekan_text}\n"
               f"Yoshlar bilan ishlash bo'yicha dekam muovinlari bo'yicha natijalar\n"
               f"{zamDekan_text}")
    return message


def create_voter(msg, dekan_id):
    user_id = msg.from_user.id
    name = ''
    if msg.from_user.username:
        name = msg.from_user.username
    else:
        name = msg.from_user.first_name
    insert_voter_table(user_id, name, dekan_id)
