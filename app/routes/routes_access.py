from app.routes import bp_routes
from app.views import access


@bp_routes.route('/api/get-access', methods=['GET'])
def get_all_access():
    return access.get_all_access()


@bp_routes.route('/api/register-access', methods=['POST'])
def register_access():
    return access.register_access()
