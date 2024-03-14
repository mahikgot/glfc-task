from flask import request
from loanflask import app, db
from loanflask.models import User, Loan
from loanflask.validation import RequestSchema
from marshmallow import ValidationError

@app.post('/loan')
def loan():
    if not request.is_json:
        return "415 Unsupported Media Type", 415
    try:
        result = RequestSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400
    return data

