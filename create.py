import sqlite3

connection = sqlite3.connect('database.db') 
cursor = connection.cursor() 

cursor.execute(""" 

    Create Table Benutzer (ID Zahl, Name Text, Nachname Text, Email Text );

""") 


cursor.execute(""" 

   Create Table Buch (BuchID Zahl, Semester Text, Preis Zahl, Zustand Text);

""") 

connection.commit() 
connection.close() 