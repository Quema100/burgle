let webcam = (app,path) =>{
    app.route('/webcam')
    .get((req, res) => {
        res.sendFile(path.join(__dirname, '..', 'html', 'webcam.html'));
    })
    .post((req, res) => {

    })
}

module.exports = webcam