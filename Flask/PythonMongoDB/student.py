from pymongo import  MongoClient
import datetime as datetime
client = MongoClient("mongodb://localhost:27017/")
print(client)
print(client.list_database_names())
mydatabase = client['Students11']
studentTable=mydatabase['student']

lst = [
{
  "country" : 'Spain',
  "city" : 'Salamanca',
  "name" : 'USAL',
  "location" : {
    "type" : 'Point',
    "coordinates" : [ -5.6722512,17, 40.9607792 ]
  },
  "students" : [
    { "year" : 2014, "number" : 24774 },
    { "year" : 2015, "number" : 23166 },
    { "year" : 2016, "number" : 21913 },
    { "year" : 2017, "number" : 21715 }
  ]
},
{
  "country" : 'India',
  "city" : 'Pune',
  "name" : 'Pune City',
  "location" : {
    "type" : 'Point',
    "coordinates" : [ -5.6722512,17, 40.9607792 ]
  },
  "students" : [
    { "year" : 2014, "number" : 24774 },
    { "year" : 2015, "number" : 23166 },
    { "year" : 2016, "number" : 21913 },
    { "year" : 2017, "number" : 21715 }
  ]
}
]


# output= studentTable.insert_many(lst)
for x in studentTable.find():
  print(x)

query1 = studentTable.aggregate([
    {"$match" : {"name":"Pune City"}}

])
print("Query 1")
for x in query1:
    print(x)

query2 = studentTable.aggregate([
    {"$match": {"name": "Pune City","students.year":2014}},
    { "$unwind" : '$students' },
    { "$project": {"_id": 0}},


])
print("Query 2")
for x in query2:
    print(x)

query3 = studentTable.aggregate(
    [
        {"$match": {"students.year":2014}},
        { "$unwind" : '$students' },
        { "$count" : 'total_documents' }

    ]
)
for x in query3:
    print(x)

query4 = studentTable.aggregate(
    [
        {
            "$project":{
                "students":{
                    "$filter":{
                        "input":"$students",
                        "as":"student",
                        "cond":{"$gt":["$$student.year",2016]},
                        "limit":2
                    }
                }
            }
        }
    ]
)
print("Query 4")
for x in query4:
    print(x)

dic = {"year" : 2018, "number" : 24774}
print("Insert element in exsiting list of elements")
# studentTable.update_one(
#     {"name": "Pune City"},
#     {"$push":{"students":dic}}
# )
#
# for x in studentTable.find():
#   print(x)


lst= [{ "year" : 20, "number" : 24774 }
,{ "year" : 213, "number" : 23166 }
      ]

# studentTable.update_many(
#     {"name": "Pune City"},
#     {"$push":{"students":{"$each":lst}}}
# )

query3 = studentTable.aggregate(
    [

        {
            "$project":{
                "students":{
                    "$filter":{
                        "input":"$students",
                        "as":"student",
                        "cond":{"$lt":["$$student.year",2016]}
                    }
                }
            }
        },
        { "$unwind" : '$students' },

    ]
)
for x in query3:
    print(x)
