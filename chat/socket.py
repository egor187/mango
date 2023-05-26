import socketio


sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    static_files={'/': './public/'}
)


@sio_server.event
async def connect(sid, data):
    print('connected: ', sid, data)


@sio_server.event
async def disconnect(sid, namespace):
    print('disconnected: ', namespace)
