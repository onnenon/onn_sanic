from sanic import Sanic, response

from onn_sanic.api import register_blueprints

app = Sanic(__name__)

register_blueprints(app)

app.static("/static", "./onn_sanic/static")


@app.route("/", methods=["GET"])
async def index(request):
    return await response.file("./onn_sanic/static/html/index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
