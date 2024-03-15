from marshmallow import Schema, fields, validate, post_load
from loanflask.models import Loan, User

class RequestSchema(Schema):
    name   = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    amount = fields.Int(required=True, validate=validate.Range(min=1000, max=10000))
    term   = fields.Int(required=True, validate=validate.OneOf((3,6,9,12,15,18)))

    @post_load
    def make_user_loan(self, data, **kwargs):
        loan = Loan(amount=data["amount"], term=data["term"])
        user = User(name=data["name"])
        return (user, loan)
