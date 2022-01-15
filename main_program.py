import sqlite3
from flask import Flask
import json

app = Flask(__name__)

@app.route('/animals/<idx>')
def animals(idx):
    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()

        query = f"""
            select * from animals_final
            left join outcomes on outcomes.animal_id = animals_final.animal_id
            where animals_final.id = {idx}
        """

        cursor.execute(query)
        result = cursor.fetchall()

        if len(result) == 1:
            line = result[0]
            result_dict = {}
            number = 1
            for i in line:
                result_dict[f"{number}"] = i
                number += 1
        else:
            result_dict = "Nothing found"
        return json.dumps(result_dict)

app.run(debug=True, port=5001)
