from flask import Flask, request
from flask import Flask, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)



# Verbindungseinstellungen zur PostgreSQL-Datenbank
dbname = 'postgres'
user = 'postgres'
password = 'mysecretpassword'
host = '127.0.0.1' #'10.104.98.120'  # z.B. 'example.com' oder '127.0.0.1', falls lokal
port = '5432'  # Standard-Port für PostgreSQL ist 5432

# Verbindung zur Datenbank herstellen
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Verbindung zur Datenbank erfolgreich hergestellt!")
        return conn
    except psycopg2.Error as e:
        print("Fehler beim Verbindungsaufbau zur Datenbank:", e)
        return None

@app.route('/')
def index():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM messages;')
    messages = cur.fetchall()
    print("Messages: ", messages)
    cur.close()
    conn.close()


@app.route('/receive_data', methods=['POST'])
def receive_data():
    conn = connect_to_db()
    cur = conn.cursor()

    data = request.get_json()
    print("Received data:", data)
    print(data)
    # Hier können Sie die empfangenen Daten verarbeiten
    #cur.execute('INSERT INTO messages (message_text)'
          #  'VALUES (%s)',
          #  (data["dataInput"],)
          #  )
    print("INSERT INTO points (position) VALUES(ST_GeomFromText('POINT(%s %s)', %s))" % (data["lat"], data["lng"], data["srid"]))
    cur.execute("INSERT INTO points (position) VALUES(ST_GeomFromText('POINT(%s %s)', %s))" % (data["lat"], data["lng"], data["srid"]))
    conn.commit()
    cur.close()
    conn.close()
    return "Data received successfully"

if __name__ == '__main__':
    app.run(debug=True)