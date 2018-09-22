/*var mysql = require("mysql");
//Database connection
app.use(function(req, res, next){
	res.locals.connection = mysql.createConnection({
		host     : '35.173.239.182',
		user     : 'team14',
		password : 'goTeam14',
		database : 'bpos'
	});
	res.locals.connect();
	next();
});*/

const mysql = require("mysql");
const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const port = 3000
const api = '/api'
const users = api + '/users'

const bposConnection = mysql.createConnection({
    host     : '35.173.239.182',
    user     : 'team14',
    password : 'goTeam14',
    database : 'bpos'
});

const klusterConnection = mysql.createConnection({
    host     : '35.173.239.182',
    user     : 'team14',
    password : 'goTeam14',
    database : 'kMeansClusteringModel'
});


app.use(bodyParser.json())
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });
app.get(api, (req, res) => res.send('Hello World!'))

app.get(users, function (req, res) {
    bposConnection.query('SELECT * from users', function (error, results, fields) {
        if(error){
            res.send(JSON.stringify({"status": 500, "error": error, "response": null})); 
            //If there is error, we send the error in the error section with 500 status
        } else {
            res.send(JSON.stringify(results));
            //If there is no error, all is good and response is 200OK.
        }
    });
  })

  app.get(users + '/email/', function (req, res) {
    bposConnection.query('SELECT email from users', function (error, results, fields) {
        if(error){
            res.send(JSON.stringify({"status": 500, "error": error, "response": null})); 
            //If there is error, we send the error in the error section with 500 status
        } else {
            res.send(JSON.stringify(results));
            //If there is no error, all is good and response is 200OK.
        }
    });
  })

  app.get(users + '&state/', function (req, res) {
    bposConnection.query('SELECT firstname, lastname, email, state FROM bpos.users;', function (error, results, fields) {
        if(error){
            res.send(JSON.stringify({"status": 500, "error": error, "response": null})); 
            //If there is error, we send the error in the error section with 500 status
        } else {
            res.send(JSON.stringify(results));
            //If there is no error, all is good and response is 200OK.
        }
    });
  })


/*
  app.get(users + '/email/', function (req, res) {
    connection.query('SELECT email from users', function (error, results, fields) {
        if(error){
            res.send(JSON.stringify({"status": 500, "error": error, "response": null})); 
            //If there is error, we send the error in the error section with 500 status
        } else {
            res.send(JSON.stringify(results));
            //If there is no error, all is good and response is 200OK.
        }
    });
  })
*/
/*
  app.get(users + '/' , function (req, res) {
    res.send('root')
  })

  app.get('/', function (req, res) {
    res.send('root')
  })

  app.get('/', function (req, res) {
    res.send('root')
  })*/
  
app.listen(port, () => console.log(`Example app listening on port ${port}!`))