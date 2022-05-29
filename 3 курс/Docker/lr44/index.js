const http = require("http");

http.createServer((req, res) => {
    res.end(`Salut de la part de ${process.env.MSG}`)
}).listen(process.env.PORT);
