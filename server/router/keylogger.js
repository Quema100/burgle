let keylogger = (app,path) =>{
    app.route('/keylogger')
    .get((req, res) => {
        res.sendFile(path.join(__dirname, '..', 'html', 'keylogger.html'));
    })
    .post((req, res) => {
    
    })
}

module.exports= keylogger