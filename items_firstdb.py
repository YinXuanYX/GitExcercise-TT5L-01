import sqlite3

connection = sqlite3.connect('itemsF.db')

#create a cursor
cursor = connection.cursor()

#create a Table
cursor.execute("create table items (name text, attributes text, passive text)")


#datatypes 1)NULL (DOESNT EXIST) 2) INTEGER (WHOLE NUM)\
# 3) REAL (DECIMAL) 4) TEXT (TEXT) 5) BLOB (STORE EXACTLY LIKE HOW IT IS LIKE IMG AND MP3)
items_list = [
    ("Blade Of Despair", "+160physical attack, +5 movement speed", "Unique Passive: Dealing damage to non-Minion enemies below 50% HP increases physical attack by 25% which last 2 seconds(take effect before the damage is dealt)"),
    ("Melefic Roar", "+60physical attack", "Unique Attribute: +20& Physical Penetration. Unique Passive: When attacking an enemy, gains 0.125% more physical penetrationcapped at 40%")
   
]  

cursor.executemany("insert into items values (?, ?, ?)", items_list)


#print database rows
for row in cursor.execute("select * from items"):
    print(row)




#commit the command
connection.commit()

#close the cnnection
connection.close
