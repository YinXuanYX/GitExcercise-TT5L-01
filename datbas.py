import sqlite3

def create_heroes_database(db_name):
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the heroes table with the specified columns
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS heroes (
        Id INTEGER PRIMARY KEY,
        Hero_name TEXT,
        Passive_name TEXT,
        Passive TEXT,
        Skill_1_name TEXT,
        Skill_1 TEXT,
        Skill_2_name TEXT,
        Skill_2 TEXT,
        Skill_3_name TEXT,
        Skill_3 TEXT,
        Ultimate_name TEXT,
        Ultimate TEXT
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage:
create_heroes_database('heroes.db')
