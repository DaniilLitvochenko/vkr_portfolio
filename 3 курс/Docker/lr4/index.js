const http = require('http');

http.createServer((req, res)=>{
    res.end(`Port ${process.env.PORT}. Env message: ${process.env.MESSAGE}`);
}).listen(process.env.PORT || 8080, ()=>{console.log(`Port 2: ${process.env.PORT} port`)});