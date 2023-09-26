import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=flask_db, user=postgres, password=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates new tables
cur.execute("CREATE TABLE IF NOT EXISTS categories (id serial PRIMARY KEY, name varchar);")
cur.execute("CREATE TABLE IF NOT EXISTS items (id serial PRIMARY KEY, name varchar, description varchar, category_id integer REFERENCES categories (id));")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO categories (name) VALUES (%s)", ("Sport",))
cur.execute("INSERT INTO categories (name) VALUES (%s)", ("Music",))
cur.execute("INSERT INTO categories (name) VALUES (%s)", ("Food",))

cur.execute("INSERT INTO items (name, description, category_id) VALUES (%s, %s, %s)", ("Football", "A ball to play football", 1)) 
cur.execute("INSERT INTO items (name, description, category_id) VALUES (%s, %s, %s)", ("Guitar", "A musical instrument", 2))
cur.execute("INSERT INTO items (name, description, category_id) VALUES (%s, %s, %s)", ("Pizza", "A delicious food", 3))

conn.commit()
cur.close()
conn.close()