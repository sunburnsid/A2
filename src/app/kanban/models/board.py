from . import *
from sqlalchemy.orm import backref

class Board(Base):
  __tablename__ = 'boards'
  id             = db.Column(db.Integer, primary_key=True)
  title          = db.Column(db.String(256), unique=True, nullable=False)
  board_elements = db.relationship('Element', backref=backref('elements'))

  def __init__(self, **kwargs):
    """
    Constructor
    """
    self.title = kwargs.get('title', None)


class Element(Base):
  __tablename__ = 'elements'
  id             = db.Column(db.Integer, primary_key=True)
  board_id       = db.Column(db.Integer, db.ForeignKey('boards.id'))
  category       = db.Column(db.String(256), nullable=False)
  description    = db.Column(db.String(512), nullable=False)

  def __init__(self, **kwargs):
    """
    Constructor
    """
    self.category = kwargs.get('category', None)
    self.board_id = kwargs.get('board_id', None)
    self.description = kwargs.get('description', None)
