from loanflask import app

@app.post('/loan')
def loan():
    if not request.is_json:
        return "415 Unsupported Media Type", 415
    data = request.get_data()
    return data

