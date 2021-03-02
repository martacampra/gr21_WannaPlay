from flask_login import UserMixin
from flaskblog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Participant(db.Model):
    __tablename__ = 'Participant'
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    e_id = db.Column(db.Integer, db.ForeignKey('event.id'), index=True)

    def __repr__(self):
        return '<Participant %r %r>' %self.u_id %self.e_id


class SportPlayed(db.Model):
    __tablename__ = 'SportPlayed'
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    s_id = db.Column(db.Integer, db.ForeignKey('sport.id'), index=True)
    level = db.Column(db.String(60))

    def __repr__(self):
        return '<SportPlayed %r>' % self.level


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    events = db.relationship('Event', backref='creator', lazy=True)
    sport_played_2 = db.relationship('SportPlayed', foreign_keys=[SportPlayed.u_id], backref='played', lazy=True)
    participant = db.relationship('Participant', foreign_keys=[Participant.u_id], backref='joined', lazy=True)

    def __repr__(self):
        return '<User %r %r %r>' % self.name % self.surname % self.email

    # def get_reset_token(self, expires=500):
    #   return jwt.encode({'reset_password': self.email,
    #                     'exp': time() + expires},
    #                     key=os.getenv('SECRET_KEY_FLASK'))

    # def get_reset_token(self, expires_sec=1800):
    # s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    # return s.dumps({'user_id': self.id}).decode('utf-8')

    # @staticmethod
    # def verify_reset_token(token):
    #   try:
    #      email = jwt.decode(token, key=os.getenv('SECRET_KEY_FLASK'))['reset_password']
    #     print(email)
    # except Exception as e:
    #   print(e)
    #  return
    # return User.query.filter_by(email=email).first()


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    cost = db.Column(db.Float, nullable=False, default='To be defined')
    np = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)
    level = db.Column(db.String(60))
    participant2 = db.relationship('Participant', foreign_keys=[Participant.e_id], backref='part', lazy=True)

    def __repr__(self):
        return '<Event %r %r %r>' % self.date % self.time % self.np


class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(240), nullable=False)
    phone = db.Column(db.String(60), nullable=False, unique=True)
    events_2 = db.relationship('Event', backref='place', lazy=True)

    def __repr__(self):
        return '<Club %r %r %r>' % self.name % self.address % self.phone


class Sport(db.Model):
    __tablename__ = 'sport'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    sport_played = db.relationship('SportPlayed', foreign_keys=[SportPlayed.s_id], backref='sport', lazy=True)
    events_4 = db.relationship('Event', backref='sportevent', lazy=True)

    def __repr__(self):
        return '<Sport %r>' % self.name


db.create_all()

