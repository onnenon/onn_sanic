from sanic import Sanic, response
from sanic.log import logger
from sanic.websocket import WebSocketProtocol
from websockets import ConnectionClosed

from onn_sanic.api import register_blueprints

app = Sanic(__name__)

register_blueprints(app)

app.static("/static", "./onn_sanic/static")


@app.route("/", methods=["GET"])
async def index(request):
    return await response.file("./onn_sanic/static/html/index.html")


sockets = []


@app.websocket("/chat")
async def chat(request, ws):
    sockets.append(ws)

    while not ws.closed:
        message = await ws.recv()
        logger.debug({"Message": message})
        for socket in sockets:
            try:
                if socket != ws:
                    await socket.send(message)
            except ConnectionClosed:
                sockets.remove(socket)

    sockets.remove(ws)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, protocol=WebSocketProtocol)
