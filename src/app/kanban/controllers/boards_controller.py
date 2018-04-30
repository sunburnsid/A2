from app.constants import *
from . import *
from flask import jsonify

@kanban.route('/boards', methods=['POST'])
def boards_post():
  board = create_board(request.args.get('board_title'))
  return jsonify(board)

@kanban.route('/boards', methods=['GET'])
def boards_get():

@kanban.route('/boards', methods=['DELETE'])
def boards_delete():
