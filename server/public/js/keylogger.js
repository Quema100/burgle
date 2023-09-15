
let socket;

window.onload = () => {
    socket = new WebSocket('ws://localhost:8768');
    const logList = document.getElementById('log-list');

    socket.onopen = (event) => {
        console.log('WebSocket connection opened.');
    };

    socket.onmessage = (event) => {
        const logItem = document.createElement('li');
        logItem.textContent = event.data;
        logList.appendChild(logItem);
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