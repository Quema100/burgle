let socket;

window.onload = () => {
    socket = new WebSocket('ws://localhost:8767');
    const audioElement = document.getElementById('audioElement');
    const stream = document.getElementById('Stream');
    const audioContext = new AudioContext({ sampleRate: 88200 });
    socket.binaryType = "arraybuffer";
    stream.textContent  = 'WebSocket connection is pending'

    socket.onopen = (event) => {
        console.log('WebSocket connection opened.');
        stream.textContent  = 'WebSocket connection'
        if (stream.textContent === 'WebSocket connection') {
            stream.style.animation = '2s blank infinite';
        }
    };

    socket.onmessage = (event) => {
        stream.style.animation = null;
        stream.textContent  = 'Voice Streaming'
        stream.textContent += '.'
        setTimeout(()=>{
            if(stream.textContent === 'Voice Streaming.'){
                stream.textContent += '.'
            }
        },300)

        setTimeout(()=>{
            if(stream.textContent === 'Voice Streaming..'){
                stream.textContent += '.'
            }
        },600)


        setTimeout(()=>{
            if(stream.textContent === 'Voice Streaming...'){
                stream.textContent  = 'Voice Streaming'
            }
        },900)

        const floatArray = new Float32Array(event.data);

        const audioBuffer = audioContext.createBuffer(2, floatArray.length / 2, audioContext.sampleRate);

        for (let channel = 0; channel < 2; channel++) {
            const channelData = audioBuffer.getChannelData(channel);
            for (let i = 0; i < channelData.length; i++) {
                channelData[i] = floatArray[i * 2 + channel];
            }
        }

        audioElement.src = '';
        audioElement.srcObject = audioContext.createMediaStreamDestination().stream;

        const source = audioContext.createBufferSource();
        source.buffer = audioBuffer;
        source.connect(audioContext.destination);
        source.connect(audioContext.createMediaStreamDestination());

        source.start();
    };


    socket.onclose = (event) => {
        if (event.wasClean) {
            console.log(`WebSocket connection closed cleanly, code=${event.code}, reason=${event.reason}`);
            stream.textContent  = 'WebSocket connection closed cleanly'
        } else {
            console.error('WebSocket connection died');
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