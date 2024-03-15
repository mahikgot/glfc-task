def test_given_example(client):
    response = client.post("/loan", json={
        "name": "mark guiang",
        "amount": "10000",
        "term": "12"
        })
    
    truth = {
        "Principal Loan Amount": 10000,
        "Monthly Payment Amount": 945.60,
        "Total Interest Amount": 1347.15,
        "Loan Term": 12,
        "Total Sum of Payments": 11347.15
        }
    assert response.json == truth

def test_missing_fields(client):
    response1 = client.post("/loan", json={
        "name": "",
        "amount": "10000",
        "term": "12"
        })
    response2 = client.post("/loan", json={
        "name": "mark",
        "amount": "",
        "term": "12"
        })
    response3 = client.post("/loan", json={
        "name": "mark",
        "amount": "1000",
        "term": ""
        })
    response4 = client.post("/loan", json={
        })

    assert response1.status_code == 400
    assert response2.status_code == 400
    assert response3.status_code == 400
    assert response4.status_code == 400
    
def test_amount(client):
    #more than 10000
    response1 = client.post("/loan", json={
        "name": "mark",
        "amount": "10001",
        "term": "6"
        })
    #less than 1000
    response2 = client.post("/loan", json={
        "name": "mark",
        "amount": "999",
        "term": "6"
        })

    assert response1.status_code == 400
    assert response2.status_code == 400

def test_term(client):
    correct = ["3", "6", "9", "12", "15", "18"]
    for i in range(19):
        response = client.post("/loan", json={
            "name": "mark",
            "amount": "1000",
            "term": str(i)
            })
        if str(i) in correct:
            assert response.status_code == 200
        else:
            assert response.status_code == 400
    
