
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando um banco de dados em memória
produtos = []

# Rota GET - Listar produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos), 200

# Rota POST - Adicionar produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify({"mensagem": "Produto adicionado com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
