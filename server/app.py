from flask import Flask, request, jsonify
from flask_cors import CORS
from server.extensions import db
from server.models import Message

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    CORS(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/messages', methods=['GET'])
    def get_messages():
        messages = Message.query.order_by(Message.created_at.asc()).all()
        return jsonify([message.to_dict() for message in messages])

    # Add other routes here...

    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555)