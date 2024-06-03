from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Consulta
def homepage(data_pesq):
    resultados = []
    try:
        con = mysql.connector.connect(
            host='localhost',
            database='cad_cia_aberta',
            user='root',
            password='123456'
        )

        if con.is_connected():
            cursor = con.cursor()
            query = "SELECT * FROM cad_cia_aberta WHERE DT_INI_SIT = %s"
            cursor.execute(query, (data_pesq,))
            resultados = cursor.fetchall()
            cursor.close()
            con.close()

    except Error as e:
        print("Erro ao conectar ao MySQL:", e)
    return resultados

# Resultados
@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    data_pesq = ""
    if request.method == 'POST':
        data_pesq = request.form['data']
        resultados = homepage(data_pesq)
    return render_template('homepage.html', resultados=resultados, data_pesq=data_pesq)

# Inicialização
if __name__ == '__main__':
    app.run(debug=True)