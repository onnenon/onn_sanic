from sanic import Sanic
from sanic.response import json, text
from onn_sanic.api import register_blueprints

app = Sanic(__name__)

register_blueprints(app)


@app.route("/", methods=["POST", "GET"])
async def get(request):
    return text("Sanic Test App")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
