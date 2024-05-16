import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("create table Heroes (Hero_name text, Passive text, Skill_1 text, Skill_2 text, Skill_3 text, Ultimate text)")
test_data = [
     (
        "Saber",
        "Saber's attacks reduce enemies' Physical Defense by 3 to 8 for 5 seconds on hit. This effect stacks up to 5 times.",
        "Saber releases 5 swords that orbit around him and deal 80 to 105 (+30 percent Extra Physical Attack) Physical Damage to nearby enemies on hit. The swords will retract back to him after a while. When the swords are present, Saber sends a sword toward his target on each attack, dealing 210–260 (+60 percent Extra Physical Attack) Physical Damage to the target and 50 percent of the damage to other enemies it passes through (damage against minions is reduced to 50%). Each attack also reduces the cooldown of Charge by 1 second.",
        "Saber dashes in the target direction, dealing 75 to 150 (+50 percent Extra Physical Attack) Physical Damage to enemies along the way while enhancing his next Basic Attack. The enhanced Basic Attack deals 75 to 150 (+120% Total Physical Attack) Physical Damage and slows the target by 60 percent for 1 second.",
        "None",
        "Saber charges at the target enemy hero, knocking them airborne for 1.2 seconds and striking them 3 times over the duration. The first two strikes deal 120 to 180 (+100 percent Extra Physical Attack) Physical Damage each, while the third strike deals 240 to 360 (+200 percent Extra Physical Attack) Physical Damage." 
    )
]
c.executemany("insert into Heroes values (?,?,?,?,?,?)", test_data)

#print database rows
for row in c.execute("select * from Heroes"):
    print(row)

c.close()
conn.close()