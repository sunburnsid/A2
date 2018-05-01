from . import *

class BoardElement(Base):
  __tablename__ = 'board_elements'
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