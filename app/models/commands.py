from .models import db
from .models import Users, Account ,Access


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def create_users_table():
    """ Create table model in the database """
    Users.__table__.create(db.engine)


def create_acount_table():
    """ Create table model in the database """
    Account.__table__.create(db.engine)

def create_access_table():
    """ Create table model in the database """
    Access.__table__.create(db.engine)


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, create_users_table, create_acount_table, create_access_table]:
        app.cli.add_command(app.cli.command()(command))
