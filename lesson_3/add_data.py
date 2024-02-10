#!/usr/bin/python

import sqlite3


conn = sqlite3.connect('store.db')
print("База данных успешно открыта!!!")


conn.execute("INSERT INTO CONTACTS (ID,NAME,ADDRESS,PHONE) \
      VALUES (1, 'Arystan Dias', 'Aqtau', '7(708)252-11-22')");

conn.commit()
print("Записи успешно добавлены!!!")
conn.close()      
