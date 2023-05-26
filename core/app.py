from fastapi import FastAPI

from chat.socket import sio_app


app = FastAPI()
app.mount('/', app=sio_app)


# @app.get('/')
# async def root():
#     return {'message': 'You in a root of future Telegram v.2'}

