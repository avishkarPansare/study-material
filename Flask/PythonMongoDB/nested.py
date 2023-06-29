from pymongo import  MongoClient
import datetime as datetime
client = MongoClient("mongodb://localhost:27017/")
print(client)
print(client.list_database_names())
mydatabase = client['Students11']
studentscores=mydatabase['studentscores']
print(mydatabase)


dict2=[
              {
                  'Name':"DDDDD",

                          # {'Fname':'sss','Lname':'121'},
                  "company":"SRV",
                  "salary":1000000,
              }
              ,
                {
                  'Name':"CCCC",

                          # {'Fname':'111','Lname':'22'},
                  "company":"SRV1",
                  "salary":1000000,
              },
                {
                  'Name':'BBBB',

                          # {'Fname':'22','Lname':'33'},
                  "company":"SRV",
                  "salary":100,
              },
{
                  'Name':"AAAAAA",

                          # {'Fname':'21','Lname':'31'},
                  "company":"SRV",
                  "salary":100,
              },
{
                  'Name':"QQQQQ",

                          # {'Fname':'221','Lname':'331'},
                  "company":"SRV",
                  "salary":10000,
              },
{
                  'Name':"ZZZZZ",

                          # {'Fname':'212','Lname':'313'},
                  "company":"SRV",
                  "salary":10000,
              }
]


# output= collection.insert_one({"emp_details":dict2,"comp_name":"AAA"})
# print(client.list_database_names())
# print("Print All Columns")
for x in studentscores.find({"comp_name":"AAA"}):
  print(x.get("emp_details"))


print("Output of nested ")

query6 = studentscores.find(
    {'emp_details.salary':{"$lt":1000}},{"emp_details.$":True,"comp_name":True}
)

for out in query6:
    print("Print Out :",out)