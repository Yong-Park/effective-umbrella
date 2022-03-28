from flask import Flask
import psycopg2 as bd

app = Flask(__name__)

#mimebros del API
@app.route("/database")
def members():

    # conectar a base de datos
    conn = bd.connect(
        database ="cpjklpze",
        user = "cpjklpze",
        password = "PbGV_JLGulr8ftaX3luPjvUZbk7q9nOI",
        host = "raja.db.elephantsql.com",
        port = "5432"
        )
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM nombres WHERE ID<3;
        """
    )
    data = cur.fetchall()
    parsed_data=[]

    for row in data:
        parsed_data.append(list(row))
    return {"nombre": parsed_data}


if __name__ == "__main__":
    app.run(debug=True)