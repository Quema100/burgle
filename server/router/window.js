let window = (app,path) =>{
    app.route('/window')
    .get((req, res) => {
        res.sendFile(path.join(__dirname, '..', 'html', 'window.html'));
    })
    .post((req, res) => {

    })
}

module.exports = window