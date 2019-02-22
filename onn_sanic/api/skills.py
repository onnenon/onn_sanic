from sanic import Blueprint
from sanic.response import json
from sanic.views import HTTPMethodView


class Skill(HTTPMethodView):
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


class Skills(HTTPMethodView):
    async def get(self, request):
        return json({"Skills"})

    async def post(self, request):
        pass

    async def put(self, request):
        pass

    async def patch(self, request):
        pass

    async def delete(self, request):
        pass


skills_bp = Blueprint("skills", url_prefix="/api", version="v1")
skills_bp.add_route(Skill.as_view(), "/skills/<id>")
skills_bp.add_route(Skills.as_view(), "/skills")
