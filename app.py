from flask import Flask
from models import db
import config
from views import bp as main_bp


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
