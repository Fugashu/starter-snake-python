import json
import os
import random
import bottle
from api import ping_response, start_response, move_response, end_response


### myStuff ###
import mCode.Board
import mCode.Snake


@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.com">https://docs.battlesnake.com</a>.
    '''


@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')


@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()


@bottle.post('/start')
def start():
    global BattleSnake
    global GameBoard
    data = bottle.request.json
   # data = json.loads(data)

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    bH = data["board"]["height"]
    bW = data["board"]["width"]

    bS = bH * bW
    food = data["board"]["food"] #  food[index]["key"] => key = x,y
    aliveSnakes = data["board"]["snakes"] # aliveSnakes[index]["key"] => key = id,name,health,body
    mySnake = data["you"]  # mySnake["key"] => key = id,name,health,body(array with x,y coords)


    """for i in range(len(food)):
        print (food[i]["x"])
        print (food[i]["y"])
    """

    print(json.dumps(data))

    GameBoard = mCode.Board.Board(bH, bW, bS, food, aliveSnakes)
    BattleSnake = mCode.Snake.Snake(len(mySnake["body"]),[mySnake["body"][0]["y"],mySnake["body"][0]["x"]])
    print(str(BattleSnake))
    print(str(GameBoard))
    color = "#00FF00"
    print("initialize complete")
    return start_response(color)


@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))

    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))
    return end_response()


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    global BattleSnake
    global GameBoard

    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )

