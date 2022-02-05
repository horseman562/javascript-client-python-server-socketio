import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")
    
    
    

@sio.event
def connect_error(data):
    print("The connection failed!")


@sio.event
def disconnect():
    print("I'm disconnected!")


sio.connect('http://localhost:8080')

 

 
     


 