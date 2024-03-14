from flask import request, Blueprint
from loanflask.models import User, Loan, db
from loanflask.validation import RequestSchema
from marshmallow import ValidationError

loan_bp = Blueprint("loan_bp", __name__)

@loan_bp.post('/loan')
def loan():
    if not request.is_json:
        return "415 Unsupported Media Type", 415
    try:
        result = RequestSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400
    return result

