use test

db.createCollection("mycollection")

db.createCollection("mycol", {"capped": true, "size": 3, max:3})

db.magicalCollection.insert(
    {
        "name": "this is new"
    }
)

db.collection_name.drop()


db.mycol.insert(
{
    Username: "123",
    Passwrod: "456"
})

db.mycol.insert([{}])


db.mycol.find({"title": "MongoDB Overview"})

//less then
db.mycol.find(
{
    "likes": {
        $lt: 50
    }
}).pretty()

// less then equal
db.mycol.find(
{
    "likes": {
        $lte: 50
    }
}).pretty()

//greater then
db.mycol.find(
{
    "likes": {
        $gt: 50
    }
}).pretty()

//greater then equals
db.mycol.find(
{
    "likes": {
        $gte: 50
    }
}).pretty()

//not equals
db.mycol.find(
{
    "likes": {
        $ne: 50
    }
}).pretty()

//And in mongodb
db.mycol.find(
{
    $and: 
    [
        {
            "likes": {
                $gt: 50
            }
        },
        {
            "likes": {
                $lt: 100
            }
        }
    ]
}).pretty()

//OR in mongodb
db.mycol.find(
{
    $or: 
    [
        {
            "likes": 10
        },
        {
            "title": "this is my title"
        }
    ]
}).pretty()

//updating in mongodb
db.mycol.update(
{
    "title": "this is my new title"
    },
    {
        $set: {
            "title": "this is my newer title"
        }
    })

db.mycol.find({},{"title":1, _id:0}).limit(7)