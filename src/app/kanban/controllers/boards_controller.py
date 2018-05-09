from app.constants import *
from . import *
from flask import jsonify

def count_elements(board):
  pass

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
    content.append(board_schema.dump(board).data)
  print(content)
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
    print(element_schema.dump(e).data)
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
  print('Creating new element', board_id, description, category)
  element = boards_dao.create_element(board_id, description, category)
  element = element_schema.dump(element).data
  element['tags'] = []
  return jsonify({
    'success':True,
    'data': {
      'board_element':element
    }
  })