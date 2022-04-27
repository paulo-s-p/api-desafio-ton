from flask_marshmallow import Marshmallow


ma = Marshmallow()

def configure(app):
    ma.init_app(app)
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password',
                  'firstName', 'lastName', 'created_on')


user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)


class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'value', 'author_id', 'created_on')


account_share_schema = AccountSchema()
accounts_share_schema = AccountSchema(many=True)


class AccessSchema(ma.Schema):
    class Meta:
        fields = ('id', 'access')


access_share_schema = AccessSchema()
accesss_share_schema = AccessSchema(many=True)
