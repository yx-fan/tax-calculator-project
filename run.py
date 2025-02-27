from app import create_app
from config import CurrentConfig

app, redis_client = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=CurrentConfig.DEBUG, 
        port=CurrentConfig.PORT
    )