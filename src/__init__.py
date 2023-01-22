import flask, psycopg2
from os import environ
app = flask.Flask(__name__)


pg_conn_string = environ["DATABASE_URL"]


connection = psycopg2.connect(pg_conn_string)


# Set to automatically commit each statement
connection.set_session(autocommit=True)

cursor = connection.cursor()


# initialize db
cursor.execute("DROP TABLE IF EXISTS colorwars")
cursor.execute("CREATE TABLE IF NOT EXISTS colorwars ( id SERIAL PRIMARY KEY, color STRING, score INT);")
cursor.execute("SHOW COLUMNS FROM colorwars")
row = cursor.fetchone()
connection.commit()
if row: print(row[0])
cursor.execute("INSERT INTO colorwars(color, score) VALUES ('R', 1);")
cursor.execute("INSERT INTO colorwars(color, score) VALUES ('G', 1);")
cursor.execute("INSERT INTO colorwars(color, score) VALUES ('B', 1);")
connection.commit()

print("created table")
