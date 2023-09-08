let voice = (app,path) =>{
    app.route('/voice')
    .get((req, res) => {
        res.sendFile(path.join(__dirname, '..', 'html', 'voice.html'));
    })
    .post((req, res) => {

    })
}

module.exports = voice