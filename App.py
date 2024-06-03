from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


def homepage(data_pesq):
    resultados = []
    try:
        con = mysql.connector.connect(
            host='nj5rh9gto1v5n05t.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            database='lpwutk3lkfoit7km',
            user='awtwiladckiuvow0',
            password='u0yx147k7k3cn6p8'
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
        dia = request.form['dia']
        mes = request.form['mes']
        ano = request.form['ano']
        data_pesq = f"{ano}-{mes.zfill(2)}-{dia.zfill(2)}"  # Combina dia, mês e ano em formato YYYY-MM-DD
        resultados = homepage(data_pesq)
    return render_template('homepage.html', resultados=resultados, data_pesq=data_pesq)

# Inicialização


if __name__ == '__main__':
    app.run(debug=True)
