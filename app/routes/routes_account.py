from app.routes import bp_routes
from app.views import acount, access

@bp_routes.route('/api/get-account/', methods=['GET'])
def get_account():
    access.register_access()
    return acount.get_account()

@bp_routes.route('/api/register-account', methods=['POST'])
def register_account():
    access.register_access()
    return acount.register_account()


@bp_routes.route('/api/update-account/<id>/', methods=['PUT'])
def update_account(current_user, id):
    return acount.update_account(id)


@bp_routes.route('/api/delete-account/<id>/', methods=['DELETE'])
def delete_account(current_user, id):
    return acount.delete_account(id)
