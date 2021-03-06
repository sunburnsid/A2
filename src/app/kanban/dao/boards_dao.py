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
  print('Inserting board: ', board)
  db.session.add(board) # add it to the current session
  try:
    db.session.commit() # push this session to the DB
    return board
  except Exception as e:
    db.session.rollback() # rollback the session if there was an exception
    return e

def all_boards():
  """
  Get all boards in table
  """
  return Board.query.all()

def delete_board(board_id):
  """
  Deletes board
  """
  board = Board.query.filter_by(id=board_id).first()
  print('BOARD: ', board_id)
  db.session.delete(board)
  try:
    db.session.commit() # push this session to the DB
    return True
  except Exception as e:
    db.session.rollback() # rollback the session if there was an exception
    return e

def create_element(board_id, description, category):
  element = Element(board_id = board_id, description = description, category = category)
  board = Board.query.filter_by(id=board_id).first()
  board.board_elements.append(element)
  board.updated_at = db.func.current_timestamp()
  try:
    db.session.commit() # push this session to the DB
    return element
  except Exception as e:
    db.session.rollback() # rollback the session if there was an exception
    return e

def get_element_by_id(element_id):
  element = Element.query.filter_by(id=element_id).first()
  return element

def delete_element(element_id):
  element = Element.query.filter_by(id=element_id).first()
  db.session.delete(element)
  try:
    db.session.commit() # push this session to the DB
    return True
  except Exception as e:
    db.session.rollback() # rollback the session if there was an exception
    return e

def advance_element(element_id):
  element = Element.query.filter_by(id=element_id).first()
  if element.category == 'todo':
    element.category = 'inprogress'
    element.updated_at = db.func.current_timestamp()
  elif element.category == 'inprogress':
    element.category = 'done'
    element.updated_at = db.func.current_timestamp()
  try:
    db.session.commit() # push this session to the DB
    return True
  except Exception as e:
    db.session.rollback() # rollback the session if there was an exception
    return e