let socket;

window.onload = () => {
    socket = new WebSocket('ws://localhost:8765');
    const stream = document.getElementById('Stream');
    const video = document.getElementById('video');
    video.style.display = 'none'
    stream.textContent  = 'WebSocket connection is pending'

    socket.onopen = (event) => {
        console.log('WebSocket connection opened.');
    };

    socket.onmessage = (event) => {
        video.style.display = null
        stream.textContent = null
        const blob = new Blob([event.data], { type: 'image/png' });
        const imgUrl = URL.createObjectURL(blob);
        document.getElementById('video').src = imgUrl;
    };

    socket.onclose = (event) => {
        if (event.wasClean) {
            console.log(`WebSocket connection closed cleanly, code=${event.code}, reason=${event.reason}`);
            video.style.display = 'none'
            stream.textContent  = 'WebSocket connection closed cleanly'
        } else {
            console.error('WebSocket connection died');
            video.style.display = 'none'
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