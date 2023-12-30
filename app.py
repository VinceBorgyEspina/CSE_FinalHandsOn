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
