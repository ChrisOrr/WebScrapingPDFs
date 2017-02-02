from app import db

class User(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(64), index=True, unique=True)
    email         = db.Column(db.String(120), index=True, unique=True)
    hash          = db.Column(db.String(1024))
    salt          = db.Column(db.String(16))
    createddate   = db.Column(db.DATETIME())
    lastlogindate = db.Column(db.DATETIME())
    active        = db.Column(db.BOOLEAN())

    def __repr__(self):
        return '<User %r>' % (self.id)

class PDF(db.Model):
    id           = db.Column(db.Integer, primary_key = True)
    basewebsite  = db.Column(db.String(512))
    filelocation = db.Column(db.String(512))
    date         = db.Column(db.DATETIME())
    md5hash      = db.Column(db.String(32))
    user_id      = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.id)