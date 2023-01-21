import flask
app = flask.Flask(__name__)

pg_conn_string="postgresql://gink_purdue_edu:4BxxDePQYkEYHLCYgVkNfA@misty-wombat-6961.5xj.cockroachlabs.cloud:26257/misty-wombat-6961.defaultdb?sslmode=verify-full"

connection = psycopg2.connect(pg_conn_string)


# Set to automatically commit each statement
connection.set_session(autocommit=True)

cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

def create_tables():
    cursor.execute(
    """
    CREATE TABLE colorwars (
      id SERIAL PRIMARY KEY, 
      group STRING, 
      score INT, 
    )"
    """
    )
    connection.commit()

    print("created table")
    