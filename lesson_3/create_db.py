#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('store.db')
print("База данных успешно открыта!")

conn.execute('''CREATE TABLE CONTACTS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         ADDRESS        CHAR(50),
         PHONE          TEXT    NOT NULL);
         ''')
print("Таблица CONTACTS успешно создана!")

conn.close()
