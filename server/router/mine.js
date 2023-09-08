let main = (app,path) =>{
    app.route('/main')
    .get((req, res) => {
        res.sendFile(path.join(__dirname, '..', 'html', 'main.html'));
    })
    .post((req, res) => {
    
    })
}

module.exports= main