let socket;

window.onload = () => {
    socket = new WebSocket('ws://localhost:8767');
    const audioElement = document.getElementById('audioElement');
    const audioContext = new AudioContext({ sampleRate: 88200 });
    socket.binaryType = "arraybuffer";

    socket.onopen = (event) => {
        console.log('WebSocket connection opened.');
    };

    socket.onmessage = (event) => {
        // event.data에 수신된 ArrayBuffer가 있음

        // ArrayBuffer를 Float32Array로 변환
        const floatArray = new Float32Array(event.data);

        // Float32Array를 AudioBuffer로 변환
        const audioBuffer = audioContext.createBuffer(2, floatArray.length / 2, audioContext.sampleRate);

        // 각 채널에 데이터 채우기
        for (let channel = 0; channel < 2; channel++) {
            const channelData = audioBuffer.getChannelData(channel);
            for (let i = 0; i < channelData.length; i++) {
                channelData[i] = floatArray[i * 2 + channel];
            }
        }

        // 오디오 데이터를 재생
        audioElement.src = '';
        audioElement.srcObject = audioContext.createMediaStreamDestination().stream;
        //audioElement.play();

        const source = audioContext.createBufferSource();
        source.buffer = audioBuffer;
        source.connect(audioContext.destination);
        source.connect(audioContext.createMediaStreamDestination());

        source.start();
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