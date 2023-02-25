/* 
1. Node.JS is an open source environment 
2. Node.JS is used to run JS on the server 
 */
// Node.jsruns single-threaded, non-blocking, asynchronus programming, which is very memory efficent 


// var http = require('http');
// http.createServer( function( req , res ){
//     res.writeHead( 200 , {'Content-Type':'text/html'})
//     res.end('Hello Worslda')
// }).listen(8080);


// Node.js files must be initiated in the "command line interface" programm of your computer. 
// after running this file in your command linee your computer should work as a server for the localhost:8080
// the Built-in HTTP module in the node.js, this allow the node to transferr the data over the HTTP.
// createServer() <= this method is used to create an HTTP server 


// var http = require('http');
// http.createServer( function( req , res ){
//    res.writeHead( 200 ,{ 'Content-Type' : 'text/html'})
//    res.write("Hello World!\n") // write a response to the client 
//    res.write( req.url )
//    res.end() // this will end the response 
// }).listen(8080) ;// the server obj. listens on the port 8080


// req =request ; res =response
// > the first argument of the function res.writeHead() is the status-code and 200 means everything is OK and the second argument is an object containing the response headers.( for notifying the type of content in the file )

// Read the Query string :>
// http.createServer() has a req argument that represent the request from the client, as an object, this means that the ( req ) is an object 
// Now this object has a property called 'url' which holds the url that comes after the domain name:

// SPLITING OF THE QUERY STRING :
// there are built-in modules to easily split the query string into readable parts, such as the URL module.


// var http = require('http');
// var url = require('url');

// http.createServer(function (req, res) {
//   res.writeHead(200, {'Content-Type': 'text/html'});
//   var q = url.parse(req.url, true).query;
//   var txt = q.year + " " + q.month;
//   res.end(txt);
// }).listen(8081);


// here the url.parse() function is used 

// NODE.JS as a file server 

const fileSystem = require('fs')
const http = require('http')
http.createServer( function( req , res ){
   fileSystem.readFile('index.html', 'utf-8' ,( err, data) => {
      res.writeHead( 200 , {'Content-Type':'text/html'})
      res.write( data )
      return res.end( )
   } )
   fileSystem.appendFile( 'append.txt' , 'Hello Document' , function(err){
      if ( err ) throw err ;
   })
}).listen(8081)