import os
import requests
from app import db
from app.models.superfund_site import superfund_site
from dotenv import load_dotenv
from flask import Blueprint, request, make_response, jsonify

load_dotenv()

superfund_bp = Blueprint("superfund_bp", __name__, url_prefix="/superfunds")

from app import db

LOCATIONS =[]

@superfund_bp.route("", methods=["POST"])
def create_superfund():
    request_body = request.get_json()
    for i in range(len(request_body)):
        new_superfund = superfund_site.from_dict(request_body[i])
        db.session.add(new_superfund)
        db.session.commit()

    return {"message":"success"}, 201

@superfund_bp.route("", methods=["GET"])
def get_superfunds():
    superfunds = superfund_site.query.all()
    response = [superfund.to_dict() for superfund in superfunds]

    return jsonify(response)

@superfund_bp.route("", methods=["DELETE"])
def delete_superfund():
    superfunds=superfund_site.query.all()
    for superfund in superfunds:
        db.session.delete(superfund)
        db.session.commit()

    return make_response("delete successful", 200)