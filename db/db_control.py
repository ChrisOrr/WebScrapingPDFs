from db import models
from app import db
import datetime
import hashlib

def EraseAllData():
    users = models.User.query.all()
    for user in users:
        db.session.delete(user)
        db.session.commit()

    PDFs = models.PDF.query.add()
    for PDF in PDFs:
        db.session.delete(PDF)
        db.session.commit()

def insertUser(email, username, password):
    id = 1

    tupe = hashpassword(password)
    hash = tupe[0]
    salt = tupe[1]

    user = models.User(id=id, name=username, email=email, hash=hash, salt=salt, createddate=datetime.datetime.now(), lastlogindate=None, active=True)
    print (user)

    db.session.add()
    db.session.commit()

def hashpassword(password):
    import random
    salt = random._urandom(16)
    salt = str(salt)
    h = hashlib.md5()
    h.update(salt.encode())
    h.update(password.encode())
    hash = salt + h.hexdigest()
    return hash, salt

insertUser('someone@example.com', 'StevenMarshall', 'Neueda')

