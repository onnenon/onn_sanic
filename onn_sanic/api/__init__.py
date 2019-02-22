def register_blueprints(app):
    from onn_sanic.api.projects import projects_bp
    from onn_sanic.api.skills import skills_bp
    from onn_sanic.api.xp import xp_bp

    app.blueprint(projects_bp)
    app.blueprint(skills_bp)
    app.blueprint(xp_bp)
