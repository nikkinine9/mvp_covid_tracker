from flask import Flask
import dbcreds
import mariadb

app = Flask(__name__);

@app.route('/src/api/index.js', methods=['GET'])
def api():
    return mariadb.connect(
        user=dbcreds.user,
        password=dbcreds.password,
        host=dbcreds.host,
        port=dbcreds.port,
        database=dbcreds.database
    )
    
    
def add_data():
    country = ""
    infected = ""
    recovered = ""
    deaths = ""

    conn = api()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO daily_data (country, infected, recovered, deaths) VALUES (?, ?, ?, ?)",
        [country, infected, recovered, deaths]
    )
    conn.commit()

    if (cursor.rowcount == 1):
        add_data()
    else:
        print("There was an error")

    cursor.close()
    conn.close()
    
    
   
