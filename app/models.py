from . import db


class Position(db.Model):
    __tablename__ = 'position'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    weight = db.Column(db.Integer(), nullable=True)


class User(db.Model):
    __tablename__='user_base'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.Integer(), nullable=True)
    position_id = db.Column(db.Integer(), db.ForeignKey('position.id'), nullable=True)
    sound_url = db.Column(db.String(100), nullable=True)
    status = db.Column(db.Boolean, default=False)
    sound_text = db.Column(db.String(500), nullable=True)
    is_super_user = db.Column(db.Boolean, default=False)


class Recommend(db.Model):
    __tablename__ = 'recommend'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    recommend_ids = db.Column(db.String(50), nullable=True)
    recommend_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=True)


class Instruction(db.Model):
    __tablename__ = 'instruction'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    instruction = db.Column(db.String(100))


class UserDouble(db.Model):
    __tablename__ = 'user_double'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    sound_url = db.Column(db.String(100))
    sound_text = db.Column(db.String(500), nullable=True)
    position_id = db.Column(db.Integer(), db.ForeignKey('position.id'), nullable=True)


class WelcomeSound(db.Model):
    __tablename__ = 'welcomesound'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    sound_url = db.Column(db.String(100))
    sound_text = db.Column(db.String(500), nullable=True)
    stranger_status = db.Column(db.Integer())  # 陌生人
    open_status = db.Column(db.Integer())      # 有无权限
    one_or_more = db.Column(db.Integer())
    super_status = db.Column(db.Integer())    # 是否为内部欢迎词



class Loudspeaker(db.Model):
    __tablename__ = 'loudspeaker'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    no = db.Column(db.Integer())
    area = db.Column(db.String(50))