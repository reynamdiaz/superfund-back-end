import os
import requests
from app import db
from app.models.superfund_site import superfund_site
from dotenv import load_dotenv
from flask import Blueprint, request, make_response

load_dotenv()

superfund_bp = Blueprint("superfund_bp", __name__, url_prefix="/superfunds")

from app import db

LOCATIONS =[]

@superfund_bp.route("", methods=["POST"])
def create_superfund():
    request_body = request.get_json()
    new_superfund = superfund_site.from_dict(request_body)
    db.session.add(new_superfund)
    db.session.commit()

    return {"message":"success"}, 201