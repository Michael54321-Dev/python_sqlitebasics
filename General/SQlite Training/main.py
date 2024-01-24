import sqlite3
import os

# Path to the SQLite database
db_path = "gta.db"

# Check if the database exists
if os.path.exists(db_path):
    # If it exists, delete the database file
    os.remove(db_path)
    print("Existing database deleted.")
else:
    print("Database does not exist. Continuing with creation.")

# Create a new database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# create empty database
connection = sqlite3.connect("gta.db")
# communicate with the database
cursor = connection.cursor()

# data to be inserted into the database
release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

city_list = [
    ("Liberty City", "New York"),
    ("state of New Guernsey", "state of New Jersey"),
    ("Anywhere, USA", "all USA cities"),
    ("Vice City", "Miami"),
    ("state of San Andreas", "state of California"),
    ("Los Santos", "Los Angeles")
]

# create database table and populate it 
cursor.execute("create table gta (release_year integer, release_name text, city text)")
cursor.executemany("insert into gta values (?,?,?)", release_list)
# save changes immediatley
connection.commit()

# create database table and populate it 
cursor.execute("create table cities (gta_city text, real_city text)")
cursor.executemany("insert into cities values (?,?)", city_list)
# save changes immediatley
connection.commit()


print("Inserted data successfully")


# Print database rows
for row in cursor.execute("SELECT * FROM gta"):
    print(row)

print("----------------------")

# print specific rows 
cursor.execute("select * from gta where city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)


# print specific rows 
cursor.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})
cities_search = cursor.fetchall()
print(f"from cities table {cities_search}")



#manipute database data 
print("-----------------------------------------------------------------")

for i in gta_search:
    #["New York" if value == "Libert City" else value for value in i]
    #Using slicers to achieve the same effect which is better practice 
    adjusted = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
    print(adjusted)


connection.close()
