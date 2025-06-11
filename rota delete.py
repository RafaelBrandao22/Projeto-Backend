# Rota DELETE - Excluir cliente por ID
@app.route('/clientes/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    global clientes
    clientes = [cli for cli in clientes if cli.get('id') != id]
    return jsonify({"mensagem": f"Cliente com ID {id} excluído com sucesso!"}), 200
