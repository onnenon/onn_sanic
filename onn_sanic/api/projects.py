from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import json


class Project(HTTPMethodView):
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


class Projects(HTTPMethodView):
    async def get(self, request):
        return json({"Projects"})

    async def post(self, request):
        pass

    async def put(self, request):
        pass

    async def patch(self, request):
        pass

    async def delete(self, request):
        pass


projects_bp = Blueprint("projects", url_prefix="/api", version="v1")
projects_bp.add_route(Project.as_view(), "/projects/<id>")
projects_bp.add_route(Projects.as_view(), "/projects")
