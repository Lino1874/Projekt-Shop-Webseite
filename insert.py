import sqlite3

connection = sqlite3.connect('database.db') 
cursor = connection.cursor() 

cursor.execute(""" 

Insert Into Benutzer
Values (123,'Benjamin','Vorst','Benvgmail.com');


""") 


cursor.execute(""" 

Insert Into Buch
Values (12343,'Q1',20,'Gut');

""") 

connection.commit() 

connection.close() 