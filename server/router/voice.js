let voice = (app,path) =>{
    app.route('/voice')
    .get((req, res) => {
        res.sendFile(path.join(__dirname, '..', 'html', 'webcam.html'));
    })
    .post((req, res) => {

    })
}