import sqlite3

import requests
from telebot import types

from keys import bot_url, photo_1, caption_1, caption_2, photo_2, TOKEN


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
        rector = ("Name", 0)
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

        name = "Name"
        voice = 0
        id = 2
        cursor.execute(update_query, (name, voice, id))
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


# dekan = ("Name", 0)
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
# add_dekan_voice(2)
# add_dekan_voice(3)
# add_dekan_voice(4)
# add_dekan_voice(5)
# add_dekan_voice(6)
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


# insert_zamDekan_table("Name", 0)
# insert_zamDekan_table("Name", 0)
# insert_zamDekan_table("Name", 0)
# insert_zamDekan_table("Name", 0)


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


# add_zamDekan_voice(1)
# add_zamDekan_voice(2)
# add_zamDekan_voice(3)
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


# print(read_voter_table())


def delete_votes():
    voters = read_voter_table()
    for voter in voters:
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            query = f"""DELETE FROM voter WHERE id = {voter[0]};"""
            cursor.execute(query)
            connection.commit()


# delete_votes()


def update_voter_table(user_id, zamDekan_id):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        voter_query = """UPDATE voter SET zamDekan = ? WHERE user_id = ?;"""
        cursor.execute(voter_query, (zamDekan_id, user_id))
        connection.commit()


def create_messages():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        query = """CREATE TABLE IF NOT EXISTS message (id INTEGER PRIMARY KEY AUTOINCREMENT, channel TEXT NOT NULL, message_id INTEGER NOT NULL);"""
        cursor.execute(query)
        connection.commit()


# create_messages()


def insert_message(channel, message_id):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        query = """INSERT INTO message (channel, message_id) VALUES (?, ?);"""
        cursor.execute(query, (channel, message_id))
        connection.commit()


# insert_channels_msg_id('-2481531999', 12, "majburiyobunaqilish")


def read_message():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        query = """SELECT * FROM message;"""
        cursor.execute(query)
        channels = cursor.fetchall()
        data = []
        for channel in channels:
            data.append(channel)
        return data


# print(read_message())


def delete_message():
    messages = read_message()
    for message in messages:
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            query = f"""DELETE FROM message WHERE id = {message[0]};"""
            cursor.execute(query)
            connection.commit()


# delete_message()


def result_all(bot, msg):
    result_dekan = types.InlineKeyboardMarkup(row_width=1)
    dekans = read_dekan_table()
    for dekan in dekans:
        result_dekan.add(
            types.InlineKeyboardButton(text=f"{dekan[2]} - {dekan[1]}", url=bot_url)
        )
    bot.send_photo(msg.from_user.id,
                   photo=photo_1,
                   caption=caption_1,
                   parse_mode='HTML',
                   reply_markup=result_dekan)
    result_zamDekan = types.InlineKeyboardMarkup(row_width=1)
    zamDekans = read_zamDekan_table()
    for zamDekan in zamDekans:
        result_zamDekan.add(
            types.InlineKeyboardButton(text=f"{zamDekan[2]} - {zamDekan[1]}", url=bot_url)
        )
    bot.send_photo(msg.from_user.id,
                   photo=photo_2,
                   caption=caption_2,
                   parse_mode='HTML',
                   reply_markup=result_zamDekan)


def create_voter(msg, dekan_id):
    user_id = msg.from_user.id
    name = ''
    if msg.from_user.username:
        name = msg.from_user.username
    else:
        name = msg.from_user.first_name
    insert_voter_table(user_id, name, dekan_id)


def last_message_id(chat_id):
    base_url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

    parameters = {
        'offset': chat_id,
        'limit': '100',
    }
    response = requests.get(base_url, data=parameters)
    first = response.json()
    second = first['result']
    length = len(second)
    return second[length - 1]['channel_post']['message_id']


# print(last_message_id(-1002481531999))


def zero_voice():
    dekans = read_dekan_table()
    for dekan in dekans:
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            update_query = """UPDATE dekan SET voice = ? where id = ?;"""
            voice = 0
            cursor.execute(update_query, (voice, dekan[0]))
            connection.commit()
    zamDekans = read_zamDekan_table()
    for zamDekan in zamDekans:
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            update_zamDekan_query = """UPDATE zamDekan SET voice = ? where id = ?;"""
            voice = 0
            cursor.execute(update_zamDekan_query, (voice, zamDekan[0]))
            connection.commit()
