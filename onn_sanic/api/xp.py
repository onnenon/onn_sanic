from sanic import Blueprint
from sanic.response import json
from sanic.views import HTTPMethodView


class SingleXp(HTTPMethodView):
    async def get(self, request, id):
        pass

    async def post(self, request, id):
        pass

    async def put(self, request, id):
        pass

    async def patch(self, request, id):
        pass

    async def delete(self, request, id):
        pass


class Xp(HTTPMethodView):
    async def get(self, request):
        return json({"Experience"})

    async def post(self, request):
        pass

    async def put(self, request):
        pass

    async def patch(self, request):
        pass

    async def delete(self, request):
        pass


xp_bp = Blueprint("xp", url_prefix="/api", version="v1")
xp_bp.add_route(SingleXp.as_view(), "/xp/<id>")
xp_bp.add_route(Xp.as_view(), "/xp")
