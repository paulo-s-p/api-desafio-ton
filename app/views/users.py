from werkzeug.security import generate_password_hash
from flask import request, jsonify
from ..models.models import Users, db
from ..models.serealizer import user_share_schema, users_share_schema
from ..views import access


def get_users():
    users = Users.query.all()
    if users:
        result = users_share_schema.dump(users)
        access.register_access()

        return jsonify({'message': 'Dados retornados com sucesso', 'data': result})

    else: return jsonify({'message': 'Não existe dados para essa consulta', 'data': []})


def get_user_email(email):
    user = Users.query.filter(Users.email == email).first()
    if user:
        result = user_share_schema.dump(user)
        return jsonify({'message': 'Usuário retornado com sucesso', 'data': result})

    return jsonify({'message': 'Usuário não encontrado na base de dados', 'data': {}}), 404


def register_user():
    email = request.json['email']
    password = request.json['password']
    firstName = request.json['firstName']
    lastName = request.json['lastName']
    pass_hash = generate_password_hash(password)
    user = Users(
        email,
        pass_hash,
        firstName,
        lastName,
    )
    info = Users.query.filter(Users.email == user.email).first()

    if info:
        return jsonify({'nessage': 'email já cadastrado', 'data': {}}), 404

    try:

        
        db.session.add(user)
        
        db.session.commit()
        result = user_share_schema.dump(user)
        return jsonify({'message': 'Usuário registrado com sucesso', 'data': result}), 201
    except:
        return jsonify({'message': 'Não foi possível registrar o usuário', 'data': {}}), 500


def update_user(id):
    email = request.json['email']
    password = request.json['password']
    firstName = request.json['firstName']
    lastName = request.json['lastName']

    user = Users.query.get(id)

    if not user:
        return jsonify({'nessage': 'usuário não existente na base da dados', 'data': {}}), 404

    pass_hash = generate_password_hash(password)

    try:
        user.email = email
        user.password = pass_hash
        user.firstName = firstName
        user.lastName = lastName
        db.session.add(user)
        db.session.commit()
        result = user_share_schema.dump(user)
        return jsonify({'message': 'Atualizado com sucesso', 'data': result.data}), 201
    except:
        return jsonify({'message': 'Não foi possivel atualizar os dados', 'data': {}}), 500


def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': 'Usuário não existente!', 'data': {}}), 404

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = user_share_schema.dump(user)
            return jsonify({'message': 'Usuário deletado com sucesso', 'data': result}), 200
        except:
            return jsonify({'message': 'Não foi possível deletar o usuário', 'data': {}}), 500


def user_by_email(email):
    try:
        return Users.query.filter(Users.email == email).one()
    except:
        return None
