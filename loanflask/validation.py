from marshmallow import Schema, fields
from loanflask.models import Loan, User

class RequestSchema(Schema):
    name = fields.Str()
    amount = fields.Int()
    term = fields.Int()



