# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


from pymongo import  MongoClient
import datetime as datetime
client = MongoClient("mongodb://localhost:27017/")
print(client)
print(client.list_database_names())
mydatabase = client['Students']
print(mydatabase)

collection=mydatabase['studentscores']
print("Insert single row")
data = { "name": "John", "address": "Highway 37","date" : datetime.datetime.now()}
output =collection.insert_one(data)
print("After Inserting Data :",output.inserted_id)
print("Insert many data")
data = [
    {"user":"Krish", "subject":"Database", "score":80,"date" : datetime.datetime(2010, 12, 31, 12, 30, 30, 125000)},
    {"user":"Amit",  "subject":"JavaScript", "score":90,"date" : datetime.datetime(2011, 12, 31, 12, 30, 30, 125000)},
    {"user":"Amit",  "title":"Database", "score":85,"date" : datetime.datetime(2014, 12, 31, 12, 30, 30, 125000)},

    {"user":"Amit",  "title":"Data Science", "score":60,"date" : datetime.datetime(2010, 11, 21, 12, 30, 30, 125000)},
    {"user":"Krish",  "title":"Data Science", "score":95,"date" : datetime.datetime(2010, 11, 30, 12, 30, 30, 125000)}]
output= collection.insert_many(data)
# print("After Inserting Data :",output.inserted_id)

print(client.list_database_names())

print("Print All Columns")
for x in collection.find():
  print(x)

print("Print same Columns only")
for x in collection.find({},{"score": 0,"_id":0}):
  print(x)

print("Select query")
query = {"score":95}
output_query = collection.find(query,{"score": 0,"_id":0})
for x in output_query:
  print(x)

print("Query Aggregate")
print("GT")
query = {"score":{"$gt":85}}
output_query = collection.find(query,{"_id":0})
for x in output_query:
  print(x)
print("LT")
query = {"score":{"$lt":85}}
output_query = collection.find(query,{"_id":0})
for x in output_query:
  print(x)
print("EQ")
query = {"score":{"$eq":85}}
output_query = collection.find(query,{"_id":0})
for x in output_query:
  print(x)

print("regex")
query = {"user":{"$regex":"^K"}}
output_query = collection.find(query,{"_id":0})
for x in output_query:
  print(x)

print("Sort ascending")
query = {"score":{"$lt":85}}
output_query = collection.find(query,{"_id":0}).sort("score")
for x in output_query:
  print(x)

print("Sort descending")
query = {"score":{"$lt":85}}
output_query = collection.find(query,{"_id":0}).sort("score",-1)
for x in output_query:
  print(x)


print("Update Single Data")
find_query = {"score":{"$eq":85}}
update_query = {"$set":{"score":100}}
x = collection.update_one(find_query, update_query)
print(x.modified_count, "documents updated.")
for x in collection.find().sort("score",-1):
  print(x)

print("Limit")
for x in collection.find().sort("score",-1).limit(3):
  print(x)
print("Group User name and Sum by subject count")
agg_result= collection.aggregate(
    [
      {
        "$group" :
          {
            "_id" : "$user",
            "Total Subject" : {"$sum" : 1}
          }
      }
    ]
)
for i in agg_result:
    print(i)

print("Sum of socre ")
agg_result= collection.aggregate(
    [{
    "$group" :
        {"_id" : "$user",
         "Total Marks" : {"$sum" :"$score"}
         }}
    ])
for i in agg_result:
    print(i)

print("Avg of socre ")
agg_result=collection.aggregate([
   {
      "$group": {
         "_id": '$user',
         "StudentScoreAverage": {
            "$avg": "$score"
         }
      }
   }
])
for i in agg_result:
    print(i)


print("Date Time filter")
from_date = datetime.datetime(2010, 10, 31, 12, 30, 30, 125000)
to_date = datetime.datetime(2012, 12, 31, 12, 30, 30, 125000)
find_query = {"date":{"$gt": from_date, "$lt": to_date}}
output_query = collection.find(query)
for x in output_query:
  print(x)



print("Delete Single Data")
query = {"address":{"$regex":"^H"}}
output_query = collection.delete_one(query)
print(output_query.deleted_count, " documents deleted.")

print("Delete Many Data")
query = {"score":{"$lt":85}}
output_query = collection.delete_many(query)
print(output_query.deleted_count, " documents deleted.")


print("Delete All Data")
query = {}
output_query = collection.delete_many(query)
print(output_query.deleted_count, " documents deleted.")

print("Delete Collection")
collection.drop()
print(client.list_database_names())

