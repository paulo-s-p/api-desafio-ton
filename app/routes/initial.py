from flask import render_template
from app.routes import bp_routes


@bp_routes.route('/',)
def initial():
    return render_template('index.html')
