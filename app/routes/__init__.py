from flask import Blueprint
from flask_cors import CORS
from sqlalchemy import true

bp_routes = Blueprint('routes', __name__)


# cors = CORS()
# cors.init_app(bp_routes, methods=['GET, POST'])

CORS(bp_routes,
     resources={r'/api/*': {'origins':'*'}},
     supports_credentials=true,
     allow_headers=['Authorization', 'Content-Type', 'enctype'],
     
     )


# ,  "Content-Length", 'Origin',  'Accept'


# 'Content-Length',

# api_cors_config = {
#     "origins": ["http://localhost:5000"],
#     "methods": ["OPTIONS", "GET", "POST"],
#     "allow_headers": ["Authorization", "Content-Type"]
# }


# api_cors_config2 = {
#     'Access-Control-Allow-Origin': 'http://localhost:5000',
#     'Access-Control-Allow-Credentials': 'true',
#     'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
#     'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept', }

# CORS(bp_routes, resources={r"/api/*": {"origins": "*"}})
