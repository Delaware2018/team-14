var mysql = require("mysql");
//Database connection
app.use(function(req, res, next){
	res.locals.connection = mysql.createConnection({
		host     : 'localhost',
		user     : 'root',
		password : ' ',
		database : 'test'
	});
	res.locals.connect();
	next();
});

/*const express = require('express')
const app = express()
const port = 3000

app.get('/api', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`)*/