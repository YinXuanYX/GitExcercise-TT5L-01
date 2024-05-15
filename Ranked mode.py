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
    ("Great Dragon Spear", "+70 Physical Attack,+10% Cooldown Reduction+20% Crit Chance","Unique Passive - Supreme Warrior: After casting an Ultimate, increase Movement Speed by 30% which last 7.5 seconds This effect has a 15 seconds cooldown")
    ("Sea Halbert", "+80 Physical Attack+20% Attack Speed", "Unique Passive - Lifebane: Dealing damage to a target will reduce the Shield and HP Regen effects on them to 50%, of normal for 3 seconds.Unique Passive - Punish: Increase damage by 8%, against enemy heroes with higher extra HP.")
    ("Rose Gold Meteor", "+60 Physical Attack+23 Magic Defense+10% Lifesteal")


    ()
    ()
   
]  

cursor.executemany("insert into items values (?, ?, ?)", items_list)


#print database rows
for row in cursor.execute("select * from items"):
    print(row)




#commit the command
connection.commit()

#close the cnnection
connection.close