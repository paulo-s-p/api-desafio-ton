from flask import render_template
from app.routes import bp_routes, routes_access, routes_users
from app.routes.forms import RegisterUser, RegisterAccount
from app.views.access import register_access


@bp_routes.route('/')
def initial():
    register_access()
    return render_template('base.html')

@bp_routes.route('/api/access')
def access():
    register_access()
    access = routes_access.get_all_access().get_json()
    ac = access['data']['access']
    return render_template('numberAccess.html', data=ac)

@bp_routes.route('/api/register-user')
def user_register():
    form = RegisterUser()
    return render_template('registerUser.html', form=form)

@bp_routes.route('/api/register-account')
def account_register():
    form = RegisterAccount()
    return render_template('registerAccount.html', form=form)

@bp_routes.route('/api/list-users')
def list_users():
    users = routes_users.get_users().get_json()
    dic_users = users['data']
    print(dic_users)
    return render_template('listUsers.html', users=dic_users)
