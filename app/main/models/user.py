from app.main import db, flask_bcrypt
from sqlalchemy.sql import func
from app.main.config import SECRET_KEY, ALGORITHM
# from app.main.models.blacklist import Blacklist
# from app.main.utils.utils import DateTimeEncoder
# from typing import Optional
# import jwt
import datetime
import logging

log = logging.getLogger(__name__)


class User(db.Model):
    """
    User model for storing user 
    related details
    """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    public_id = db.Column(db.String(30), unique = True)
    username = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(50), unique = True)
    registered_on = db.Column(db.DateTime, default = func.now())
    updated_on = db.Column(db.DateTime, default = func.now(), onupdate = func.now())
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    password_hash = db.Column(db.String(100))
    roles = db.relationship('role', secondary = 'user_roles', backref = db.backref('users', lazy='joined'), uselist=False)
    seller = db.Column(db.Boolean, default=False)
    def __repr__(self):
        return '<User %r>' %self.username

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # @property
    # def password(self):
    #     raise AttributeError("password: write-only field")
    
    # @password.setter
    # def password(self, password):
    #     self.password_hash= flask_bcrypt.generate_password_hash(password).decode('utf-8')

    # def check_password(self, password):
    #     return flask_bcrypt.check_password_hash(self.password_hash, password)

    # @staticmethod
    # def encode_auth_token(user_id) -> Optional[str]:
    #     """
    #     Generates the auth token
    #     ;return: string 
    #     """
    #     try:
    #         payload = {
    #             'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
    #             'iat': datetime.datetime.utcnow(),
    #             'sub': user_id
    #         }
    #         return jwt.encode(
    #             payload,
    #             SECRET_KEY,
    #             algorithm=ALGORITHM,
    #             json_encoder=DateTimeEncoder
    #         ).encode('utf-8')
    #     except Exception as e:
    #         log.error(f'Error in encode_auth_token:{e}')
    #         return None
    
    
    # @staticmethod
    # def decode_auth_token(auth_token):
    #     """
    #     Decodes the auth token
    #     ;param auth_token:
    #     ;return:
    #     """
    #     try:
    #         payload = jwt.decode(auth_token, SECRET_KEY, algorithm=ALGORITHM)
    #         isBlacklistedToken: bool = Blacklist.check_blacklist(auth_token)

    #         if isBlacklistedToken:
    #             log.info('Token blacklisted. Please log in again.')
    #             return {
    #                 'Success': False,
    #                 'Message': 'Token blacklisted. Please log in again.'
    #             }
    #         return payload
        
    #     except jwt.ExpiredSignatureError:
    #         log.info('Signature Expired. Please log in again.')
    #         return  'Signature Expired. Please log in again.'
            
    #     except jwt.InvalidTokenError:
    #         log.info('Invalid token. Please log in again.')
    #         return 'Invalid token. Please log in again.'
            
    #     except Exception as e:
    #         log.info(f'Error in decode_auth_token: {e}')
    #         return  'Error in decode_auth_token'
            


class Role(db.Model):
    """
    User model for storing role related details
    """
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), unique = True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class UserRoles(db.Model):
    """UserRoles model for storing user roles"""
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    