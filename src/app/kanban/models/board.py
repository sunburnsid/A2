from . import *

class Board(Base):
  __tablename__ = 'boards'
  id             = db.Column(db.Integer, primary_key=True)
  title          = db.Column(db.String(256), unique=True, nullable=False)
  board_elements = db.Relationship("BoardElement")

  def __init__(self, **kwargs):
    """
    Constructor
    """
    self.title = kwargs.get('title', None)


class Element(Base):
  __tablename__ = 'elements'
  id             = db.Column(db.Integer, primary_key=True)
  board_id       = db.Column(db.Integer, db.ForeignKey('board.id'))
  category       = db.Column(db.String(256), nullable=False)
  description    = db.Column(db.String(512), nullable=False)

  def __init__(self, **kwargs):
    """
    Constructor
    """
    self.category = kwargs.get('category', None)
    self.board_id = kwargs.get('board_id', None)
    self.description = kwargs.get('description', None)
