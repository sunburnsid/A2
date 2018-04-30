from app.constants import *
from . import *

"""
Add more methods below!!!
"""

def board_by_id(board_id):
  """
  Get board by ID
  """
  return Board.query.filter_by(id=board_id).first()


def create_board(board_title):
  """
  Create a board with board_title as title
  """
  board = Board(title=board_title) # create instance of the board
  db.session.add(board) # add it to the current session
  try:
    db.session.commit() # push this session to the DB
    return board
  except Exception as e:
    db.session.rollback() # rollback the session if there was an exception
    return e
  return board