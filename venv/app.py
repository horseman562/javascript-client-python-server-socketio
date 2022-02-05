import socketio
import eventlet


sio = socketio.Server(async_mode='eventlet',cors_allowed_origins='*')

 

app = socketio.WSGIApp(sio)


@sio.event
def connect(self,sid, environ):
    print(sid, 'connected')

@sio.event
def send_message(self, sid, data):
    print(data)
     
    
    
@sio.event
def disconnect(sid):
    print(sid, 'disconnected')

""" @sio.event
def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    return result """

eventlet.wsgi.server(eventlet.listen(('', 8080)), app, debug=True)





    


