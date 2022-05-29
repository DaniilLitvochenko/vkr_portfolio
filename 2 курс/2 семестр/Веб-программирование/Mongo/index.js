const MongoClient = require("mongodb").MongoClient;

const url = "mongodb+srv://admin:admin@cluster0-s3k0c.mongodb.net/test?retryWrites=true&w=majority";
const mongoClient = new MongoClient(url, {useNewUrlParser: true});

mongoClient.connect(function(err, client){

    const db = client.db("asadf");
    const collection = db.collection("qwe");

    collection.find().toArray(function(err, results){
        console.log(results);
        client.close();
    })
})