let socket;

window.onload = () => {
    socket = new WebSocket('ws://localhost:8765');

    socket.onopen = (event) => {
        console.log('WebSocket connection opened.');
    };

    socket.onmessage = (event) => {
        const audioBlob = new Blob([event.data], { type: 'audio/wav' }); // 오디오 형식에 맞게 타입 설정
        const audioUrl = URL.createObjectURL(audioBlob);
        document.querySelector('audio').src = audioUrl;
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