from app.routes import bp_routes
from app.views import users, access


@bp_routes.route('/api/get-users/', methods=['GET'])
# @authentication.token_required
def get_users():
    return users.get_users()


@bp_routes.route('/api/get-user-email/<email>', methods=['GET'])
def get_user_email(current_user, email):
    return users.get_user_email(email)


@bp_routes.route('/api/register-user/', methods=['POST'])

def register_user():
    access.register_access()
    return users.register_user()


@bp_routes.route('/update-user/<id>', methods=['PUT'])
def update_user(id):
    return users.update_user(id)


@bp_routes.route('/delete-user/<id>', methods=['DELETE'])
def delete_user(id):
    return users.delete_user(id)
