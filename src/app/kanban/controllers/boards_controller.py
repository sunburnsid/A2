from app.constants import *
from . import *
from flask import jsonify

@kanban.route('/boards', methods=['POST'])
def boards_post():
  board = boards_dao.create_board(request.args.get('board_title'))
  print("AM I HAPPENING")
  return jsonify({'success':True})

@kanban.route('/boards', methods=['GET'])
def boards_get():
  print("OR IS IT ME")
  pass

@kanban.route('/boards', methods=['DELETE'])
def boards_delete():
  print("OR IS IT ME")
  pass
