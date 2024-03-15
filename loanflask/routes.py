from flask import request, Blueprint
from loanflask.models import User, Loan, db
from loanflask.validation import RequestSchema
from marshmallow import ValidationError

loan_bp = Blueprint("loan_bp", __name__)

@loan_bp.post('/loan')
def loan():
    if not request.is_json:
        return "415 Unsupported Media Type", 415

    errors = RequestSchema().validate(request.json)
    if errors:
        return errors, 400

    newUser, loan = RequestSchema().load(request.json)
    user = db.session.query(User).filter_by(name=newUser.name).first()
    if user == None:
        user = newUser
        db.session.add(user)
    user.loans.append(loan)
    db.session.add(loan)
    db.session.commit()

    r = .02
    monthlyPayment = (loan.amount * r*((1+r)**loan.term)) / (((1+r)**loan.term)-1)
    totalInterest  = monthlyPayment * loan.term
    res = {
            "Principal Loan Amount": loan.amount,
            "Monthly Payment Amount": monthlyPayment,
            "Total Interest Amount": totalInterest,
            "Loan Term": loan.term,
            "Total Sum of Payments": loan.amount+totalInterest
            }
    res = {k: round(v,2) for k, v in res.items()}


    return res
