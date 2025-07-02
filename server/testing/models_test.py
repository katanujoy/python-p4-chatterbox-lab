import pytest
from server.extensions import db
from server.models import Message
from server.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_message_creation(app):
    with app.app_context():
        message = Message(body="Test message", username="testuser")
        db.session.add(message)
        db.session.commit()
        
        assert message.id is not None
        assert message.body == "Test message"
        assert message.username == "testuser"