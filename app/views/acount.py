from urllib import response
from flask import request, jsonify
from app.models.models import Account, db
from app.models.serealizer import account_share_schema, account_share_schema
from app.config import MEDIA_ROOT
import os


def get_account():
    account = Account.query.all()
    if not account:
        result = account_share_schema.dump(account)
        return jsonify({'message': 'Não esxite postagem', 'data': []})
    if account:
        result = account_share_schema.dump(account)
        return jsonify({'message': 'Dados retornados com sucesso', 'data': result})


def get_account_title(title):
    titleajust = title.replace('%20', ' ')
    print(titleajust)
    post = Account.query.filter(Account.title == titleajust).first()
    if post:
        result = account_share_schema.dump(post)
        return jsonify({'message': 'Título retornado com sucesso', 'data': result})

    return jsonify({'message': 'Título não encontrado na base de dados', 'data': {}}), 404


def register_account():
    response = request.form.to_dict()
    title = response['title']
    value = response['value']
    author_id = response['id_user']

    account = Account(
        title,
        value,
        author_id,
    )
    info = Account.query.filter(Account.title == account.title).first()

    if info:
        return jsonify({'nessage': 'Conta já cadastrada', 'data': {}}), 404

    try:
        db.session.add(account)
        db.session.commit()
        result = account_share_schema.dump(account)
        return jsonify({'message': 'Postagem registrada com sucesso', 'data': result}), 201
    except:
        return jsonify({'message': 'Não foi possível registrar a postagem', 'data': {}}), 500


def update_account(id):
    title = request.json['title']
    value = request.json['value']
    author_id = request.json['id_user']

    account = Account.query.get(id)

    if not account:
        return jsonify({'nessage': 'Postagem não existente na base da dados', 'data': {}}), 404

    try:
        account.title = title
        account.value = value
        account.author_id = author_id

        db.session.add(account)
        db.session.commit()
        result = account_share_schema.dump(account)
        return jsonify({'message': 'Conta atualizada com sucesso', 'data': result}), 201
    except:
        return jsonify({'message': 'Não foi possivel atualizar os dados', 'data': {}}), 500


def delete_account(id):
    account = Account.query.get(id)
    if not account:
        return jsonify({'message': 'Usuário não existente!', 'data': {}}), 404

    if account:
        try:
            db.session.delete(account)
            db.session.commit()
            result = account_share_schema.dump(account)
            return jsonify({'message': 'Postagem deletada com sucesso', 'data': result}), 200
        except:
            return jsonify({'message': 'Não foi possível deletar a postagem', 'data': {}}), 500


def account_by_title(title):
    try:
        return Account.query.filter(Account.title == title).one()
    except:
        return None
