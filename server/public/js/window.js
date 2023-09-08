let socket;

window.onload = () => {
    socket = new WebSocket('ws://localhost:8765');

    socket.onopen = (event) => {
        console.log('WebSocket connection opened.');
    };

    socket.onmessage = (event) => {
        const blob = new Blob([event.data], { type: 'image/png' });
        const imgUrl = URL.createObjectURL(blob);
        document.getElementById('video').src = imgUrl;
    };

    socket.onclose = (event) => {
        if (event.wasClean) {
            console.log(`WebSocket connection closed cleanly, code=${event.code}, reason=${event.reason}`);
        } else {
            console.error('WebSocket connection died');
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