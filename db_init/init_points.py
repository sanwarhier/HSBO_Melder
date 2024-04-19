import psycopg2

dbname = 'postgres'
user = 'postgres'
password = 'mysecretpassword'
host = '127.0.0.1' # '10.104.98.120' für Hochschul-Server oder '127.0.0.1', falls lokal
port = '5432'  # Standard-Port für PostgreSQL ist 5432

conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS points;')
cur.execute('CREATE TABLE points (id serial PRIMARY KEY,'
              'date_added date DEFAULT CURRENT_TIMESTAMP,'
              'position GEOMETRY(Point, 3857));'
            )

cur.execute("SELECT UpdateGeometrySRID('public', 'points', 'position', 3857)")

# Insert data into the table

cur.execute("INSERT INTO points (position) VALUES(ST_GeomFromText('POINT(51.46213587023546 7.233123779296875)', 3857))")


conn.commit()

cur.close()
conn.close()