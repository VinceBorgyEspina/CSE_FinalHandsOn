from flask import Flask, Response, make_response, jsonify, request, send_file, render_template
from flask_mysqldb import MySQL
import dicttoxml

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "borgyvince321"
app.config["MYSQL_DB"] = "mydb"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
print(mysql)

def generate_xml_response(results):
    xml_data = dicttoxml.dicttoxml(results)
    return Response(xml_data, mimetype='text/xml')

def data_fetch(query):
    try:
        format_requested = request.args.get('format') 
        cur = mysql.connection.cursor()
        cur.execute(query)
        
        results = cur.fetchall()
        
        if format_requested and format_requested.lower() == 'xml':
            xml_data = generate_xml_response(results)
            return xml_data
        else:
            return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()

@app.route('/athlete', methods=['GET'])
def get_employees():
    query = "SELECT * FROM mydb.athlete"
    result = data_fetch(query)
    return result

@app.route('/athlete/<int:id>', methods=['GET'])
def get_athlete__by_id(id):
    query = f"SELECT * FROM mydb.athlete WHERE athlete_id = {id}"
    result = data_fetch(query)
    return result

@app.route('/club', methods=['GET'])
def get_club():
    query = "SELECT * FROM mydb.club"
    result = data_fetch(query)
    return result

@app.route('/club/<int:id>', methods=['GET'])
def get_club__by_id(id):
    query = f"SELECT * FROM mydb.club WHERE club_id = {id}"
    result = data_fetch(query)
    return result

@app.route('/event_series', methods=['GET'])
def get_event_series():
    query = "SELECT * FROM mydb.event_series"
    result = data_fetch(query)
    return result

@app.route('/club/<int:id>', methods=['GET'])
def get_event_series__by_id(id):
    query = f"SELECT * FROM mydb.event_series WHERE series_number = {id}"
    result = data_fetch(query)
    return result
