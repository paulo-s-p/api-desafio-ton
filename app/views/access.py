from calendar import day_abbr
from flask import jsonify
from ..models.models import Access, db
from ..models.serealizer import access_share_schema


def get_all_access():
    access = Access.query.get(1)
    if not access:
        return 0
    if access:
        result = access_share_schema.dump(access)
        return jsonify({'message': 'retornado com sucesso','data': result})


def register_access():
    try:
        access = Access.query.get(1)
        
        if access != None:
            data = access
            data.access = access.access + 1
            print(data)
            db.session.add(data)
            db.session.commit()

        else:
            access = Access(1, 1)
            db.session.add(access)
            db.session.commit()
    except: 
        return 'saida inválida'