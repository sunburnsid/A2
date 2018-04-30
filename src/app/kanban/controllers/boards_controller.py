from app.constants import *
from . import *
from flask import jsonify

@kanban.route('/boards', methods=['POST'])
def boards_post():
  board_title = request.args.get('board_title')
  print('New title: ', board_title)
  board = boards_dao.create_board()
  print(board)
  dump_data = board_schema.dump(board).data
  print(dump_data)
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
  print("OR IS IT ME")
  pass
