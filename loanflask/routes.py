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
        newUser, loan = RequestSchema().load(request.json)
        user = db.session.query(User).filter_by(name=newUser.name).first()
        if user == None:
            user = newUser
            db.session.add(user)
        user.loans.append(loan)
        db.session.add(loan)
        db.session.commit()
    except ValidationError as err:
        return err.messages, 400
    return "Success", 200

