let socket;

window.onload = () => {
    socket = new WebSocket('ws://localhost:8766');
    const stream = document.getElementById('Stream')
    const img = document.getElementById('video')
    stream.textContent  = 'WebSocket connection is pending'

    socket.onopen = (event) => {
        console.log('WebSocket connection opened.');
        stream.innerHTML = 'Webcam Stream<span class="circle" id="circle1"></span><span class="circle" id="circle2"></span><span class="circle" id="circle3"></span>'
    };

    socket.onmessage = (event) => {
        stream.textContent = null
        const blob = new Blob([event.data], { type: 'image/png' });
        const imgUrl = URL.createObjectURL(blob);
        document.getElementById('video').src = imgUrl;
    };

    socket.onclose = (event) => {
        if (event.wasClean) {
            console.log(`WebSocket connection closed cleanly, code=${event.code}, reason=${event.reason}`);
            img.style.display = 'none'
            stream.textContent  = 'WebSocket connection closed cleanly'
        } else {
            console.error('WebSocket connection died');
            img.style.display = 'none'
            stream.textContent  = 'WebSocket connection died'
        }
    };

    socket.onerror = (error) => {
        console.error(`WebSocket error: ${error.message}`);
    };
};

window.onbeforeunload = () => {
    if (socket) {
        socket.close();
    }
};