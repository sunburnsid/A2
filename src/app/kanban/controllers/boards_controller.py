from app.constants import *
from . import *
from flask import jsonify

def index_elements(board):
  board['todo_count'] = 0
  board['inprogress_count'] = 0
  board['done_count'] = 0
  for e in board['board_elements']:
    element = boards_dao.get_element_by_id(e)
    element = element_schema.dump(element).data
    if element['category'] == 'todo':
      board['todo_count'] += 1
    elif element['category'] == 'inprogress':
      board['inprogress_count'] += 1
    else:
      board['done_count'] += 1
  return board

@kanban.route('/boards', methods=['POST'])
def boards_post():
  title = request.args.get('title')
  board = boards_dao.create_board(title)
  dump_data = board_schema.dump(board).data
  return jsonify({
    'success':True,
    'data': {
      'board':dump_data
    }
  })

@kanban.route('/boards', methods=['GET'])
def boards_get():
  boards = boards_dao.all_boards()
  content = []
  for board in boards:
    b = board_schema.dump(board).data
    b = index_elements(b)
    content.append(b)
  return jsonify({
    'success':True,
    'data': {
      'boards':content
    }
  })

@kanban.route('/boards', methods=['DELETE'])
def boards_delete():
  board_id = request.args.get('id')
  boards_dao.delete_board(board_id)
  return jsonify({
    'success':True
  })

@kanban.route('/boards/<board_id>', methods=['GET'])
def boards_get_by_id(board_id):
  board = boards_dao.board_by_id(board_id)
  board = board_schema.dump(board).data
  
  board['todo'] = []
  board['inprogress'] = []
  board['done'] = []
  
  for e in board['board_elements']:
    element = boards_dao.get_element_by_id(e)
    element = element_schema.dump(element).data
    element['board_id'] = element['elements'] 
    element['tags'] = []
    del element['elements']
    
    if element['category'] == 'todo':
      board['todo'].append(element)
    elif element['category'] == 'inprogress':
      board['inprogress'].append(element)
    else:
      board['done'].append(element)
  
  del board['board_elements']
  return jsonify({
    'success':True,
    'data': {
      'board':board
    }
  })

@kanban.route('/board_elements', methods=['POST'])
def boards_create_element():
  board_id = request.args.get('board_id')
  description = request.args.get('description')
  category = request.args.get('category')
  element = boards_dao.create_element(board_id, description, category)
  element = element_schema.dump(element).data
  element['board_id'] = element['elements'] 
  element['tags'] = []
  del element['elements']
  return jsonify({
    'success':True,
    'data': {
      'board_element':element
    }
  })

@kanban.route('/board_elements', methods=['DELETE'])
def boards_delete_element():
  element_id = request.args.get('board_element_id')
  boards_dao.delete_element(element_id)
  return jsonify({
    'success':True
  })

@kanban.route('/board_elements/advance', methods=['POST'])
def boards_advance_element():
  element_id = request.args.get('board_element_id')
  boards_dao.advance_element(element_id)
  return jsonify({
    'success':True
  })