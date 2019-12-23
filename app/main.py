import json
import os
import random
import bottle
from api import ping_response, start_response, move_response, end_response


### myStuff ###
import mCode.Board
import mCode.Snake

GameBoard = mCode.Board.Board()
BattleSnake = mCode.Snake.Snake()

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

    GameBoard.initialize(bH, bW, bS, food, aliveSnakes)
    BattleSnake.initialize(len(mySnake["body"]),[mySnake["body"][0]["y"],mySnake["body"][0]["x"]])
    print(str(BattleSnake))
    print(str(GameBoard))

    #print(GameBoard.isFree(1,0)) #Test function if specific tile is free
    color = "#00FF00"
    print("initialize complete")
    return start_response(color)


@bottle.post('/move')
def move():
    """
    """
    global BattleSnake
    global GameBoard

    data = bottle.request.json
    food = data["board"]["food"]  # food[index]["key"] => key = x,y
    aliveSnakes = data["board"]["snakes"]  # aliveSnakes[index]["key"] => key = id,name,health,body
    mySnake = data["you"]  # mySnake["key"] => key = id,name,health,body(array with x,y coords)

    GameBoard.updateBlocks(food, aliveSnakes)
    BattleSnake.updateHeadPos([mySnake["body"][0]["y"],mySnake["body"][0]["x"]])
    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))
    directions = ['up', 'down', 'left', 'right']
    safeMoves = BattleSnake.checkSurroundings(GameBoard)
    print(str(GameBoard))
    print("Fugas Battlesnakes safe options are: {}".format(safeMoves))
    if safeMoves == []:
        print ("lellek")
        return {"move": "up"}# if no free tiles are found snake will just suicide upwards
    direction = random.choice(safeMoves)

    print ("Fugas Battlesnake move decision: {}".format(direction))
    return { "move": direction }

@bottle.post('/end')
def end():
    data = bottle.request.json
    global GameBoard
    global BattleSnake
    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    del(GameBoard)
    del(BattleSnake)
    print ("my snake is dead")
    print(json.dumps(data))
    return end_response()


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', False)
    )

