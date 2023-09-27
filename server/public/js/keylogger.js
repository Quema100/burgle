
let socket;

window.onload = () => {
    socket = new WebSocket('ws://localhost:8768');
    const logList = document.getElementById('log-list');
    const stream = document.getElementById('Stream')
    stream.innerHTML  = 'WebSocket connection is pending'
    logList.style.display = 'none'

    socket.onopen = (event) => {
        console.log('WebSocket connection opened.');
        stream.innerHTML  = 'Keylogger pending<span class="circle" id="circle1"></span><span class="circle" id="circle2"></span><span class="circle" id="circle3"></span>'
    };

    socket.onmessage = (event) => {
        logList.style.display = null
        stream.innerHTML = null
        stream.style.display="none"
        const logItem = document.createElement('li');
        logItem.textContent = event.data;
        logList.appendChild(logItem);
    };


    socket.onclose = (event) => {
        if (event.wasClean) {
            console.log(`WebSocket connection closed cleanly, code=${event.code}, reason=${event.reason}`);
            stream.style.display= null
            logList.style.display = 'none'
            stream.textContent  = 'WebSocket connection closed cleanly'
        } else {
            console.error('WebSocket connection died');
            stream.style.display= null
            logList.style.display = 'none'
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