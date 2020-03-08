from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('user.username'))
    # TODO: Undefined string lengths are only valid in Postgres. Bad!
    entry = db.Column(db.String())

    def __repr__(self):
        return '<JournalEntry {}, {}>'.format(self.id, self.username)
