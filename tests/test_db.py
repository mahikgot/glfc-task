from loanflask.models import User, Loan, db
def test_init_user(app):
    with app.app_context():
        user = User(name="random", loans=[Loan(amount=1000, term=6)])
        db.session.add(user)
        fetchedUser = db.session.query(User).filter_by(name=user.name).first()
        fetchedLoan = db.session.query(Loan).filter_by(user_id=fetchedUser.id).first()

    assert user.name == "random"
    assert user == fetchedUser
    assert user.loans[0].amount == 1000
    assert user.loans[0].term == 6
    assert user.loans[0] == fetchedLoan

def test_stored_on_post(app, client):
    client.post("/loan", json={
        "name": "mark",
        "amount": "1000", 
        "term": "6"
        })
    client.post("/loan", json={
        "name": "mark",
        "amount": "10000", 
        "term": "12"
        })

    with app.app_context():
        fetchedUsers = db.session.execute(db.select(User).filter_by(name="mark")).scalars().all()
        assert len(fetchedUsers) == 1
        fetchedUser = fetchedUsers[0]
        assert fetchedUser.name == "mark"

        fetchedLoans = db.session.execute(db.select(Loan).filter_by(user_id=fetchedUser.id)).scalars().all()
        assert len(fetchedLoans) >= 2
        assert fetchedUser.loans == fetchedLoans


