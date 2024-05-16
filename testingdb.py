from PySide6.QtSql import *
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCoreApplication
import sys 


con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("heroes.sqlite")
con.open()
if not con.open():
    print("Unable to connect to the database")

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec("""create table Heroes (Hero_name text,Passive_name text, Passive text,skill_1_name text, Skill_1 text, skill_2_name text, Skill_2 text, skill_3_name text, Skill_3 text,Ultimate_name text, Ultimate text)""")


# Creating a query for later execution using .prepare()
insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
    """
    INSERT INTO Heroes (
        Hero_name,
        Passive_name,
        Passive,
        skill_1_name,
        Skill_1,
        skill_2_name,
        Skill_2,
        skill_3_name,
        Skill_3,
        Ultimate_name,
        Ultimate
    )
    VALUES (?, ?, ?)
    """
)
test_data = [
     (
        "Saber",
        "Enemy's bane",
        "Saber's attacks reduce enemies' Physical Defense by 3 to 8 for 5 seconds on hit. This effect stacks up to 5 times.",
        "Orbiting Swords",
        "Saber releases 5 swords that orbit around him and deal 80 to 105 (+30 percent Extra Physical Attack) Physical Damage to nearby enemies on hit. The swords will retract back to him after a while. When the swords are present, Saber sends a sword toward his target on each attack, dealing 210–260 (+60 percent Extra Physical Attack) Physical Damage to the target and 50 percent of the damage to other enemies it passes through (damage against minions is reduced to 50%). Each attack also reduces the cooldown of Charge by 1 second.",
        "Charge",
        "Saber dashes in the target direction, dealing 75 to 150 (+50 percent Extra Physical Attack) Physical Damage to enemies along the way while enhancing his next Basic Attack. The enhanced Basic Attack deals 75 to 150 (+120% Total Physical Attack) Physical Damage and slows the target by 60 percent for 1 second.",
        "None",
        "None",
        "Triple Sweep",
        "Saber charges at the target enemy hero, knocking them airborne for 1.2 seconds and striking them 3 times over the duration. The first two strikes deal 120 to 180 (+100 percent Extra Physical Attack) Physical Damage each, while the third strike deals 240 to 360 (+200 percent Extra Physical Attack) Physical Damage." 
    )
]
for Hero_name, Passive_name, Passive, skill_1_name, Skill_1, skill_2_name, Skill_2, skill_3_name, Skill_3, Ultimate_name, Ultimate in test_data:
    insertDataQuery.addBindValue(Hero_name)
    insertDataQuery.addBindValue(Passive_name)
    insertDataQuery.addBindValue(Passive)
    insertDataQuery.addBindValue(skill_1_name)
    insertDataQuery.addBindValue(Skill_1)
    insertDataQuery.addBindValue(skill_2_name)
    insertDataQuery.addBindValue(Skill_2)
    insertDataQuery.addBindValue(skill_3_name)
    insertDataQuery.addBindValue(Skill_3)
    insertDataQuery.addBindValue(Ultimate_name)
    insertDataQuery.addBindValue(Ultimate)
    insertDataQuery.exec()

query = QSqlQuery()
query.exec("select hero_name from Heroes")
print(query.value(Skill_1))