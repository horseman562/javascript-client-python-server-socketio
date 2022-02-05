const sio = io()
var text = document.getElementById('text')

sio.on('connect', () => {
    console.log('connected')
    sio.emit('sum', {numbers: [1, 2]}, (result) => {
        console.log(result)
    });
})

sio.on('disconnect', () => {
    console.log('disconnected')
})

