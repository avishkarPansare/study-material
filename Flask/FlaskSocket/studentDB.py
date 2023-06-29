from pymongo import MongoClient
import datetime as datetime

client = MongoClient("mongodb://localhost:27017/")
print(client)
print(client.list_database_names())
mydatabase = client['Students11']
studentTable = mydatabase['studentName']
lst = [
     {

        "fname": "III",
        "Lname": "JJJ",
        "City": "Pune",
        "Country": "India"
    },{

        "fname": "III",
        "Lname": "JJJ",
        "City": "Pune",
        "Country": "India"
    }
]

# output= studentTable.insert_many(lst).inserted_ids
# for i in output:
#     print(i)
#     studentTable.update_one({"_id" : i}, {"$set":{"UID":str(i)}})
# output= studentTable.insert_many(lst)
def studentInsertMany(data):
    output= studentTable.insert_many(data).inserted_ids
    for i in output:
        print(i)
        studentTable.update_one({"_id" : i}, {"$set":{"UID":str(i)}})
    output = studentTable.find({}, {"_id":0})
    # print(output)
    all_x = []
    for x in output:
        all_x.append(x)
    # print(all_x)
    return all_x
def display_student():

    myquery = {}
    output = studentTable.find({}, {"_id":0})
    # print(output)
    all_x = []

    for x in output:
        all_x.append(x)

    return all_x


def student_getDataId(DataId):
    myquery = {"UID": DataId}
    output = studentTable.find(myquery,{"_id":0})
    all_x = []
    for x in output:
        all_x.append(x)
    print("In function ",all_x)
    return all_x

def studentUpdateId(data):
    print(data)
    UID = data['UID']
    fname= data['Fname']
    Lname= data['Lname']
    City= data['City']
    Country = data['Country']
    queryWhere = {"UID":UID}
    queryUpdate = {"$set":{"City":City,"Country":Country}}

    output = studentTable.update_one(queryWhere,queryUpdate)
    print("Output of update",output.modified_count)

    output = studentTable.find(queryWhere,{"_id":0})
    # print(output)
    all_x = []

    for x in output:
        all_x.append(x)
    print(all_x)
    return all_x

def studentinsert(data):
    print(data)

    fname= data['Fname']
    Lname= data['Lname']
    City= data['City']
    Country = data['Country']

    #
    # if len(present)>0:
    #     print("Hello DAta persent ")
    #     findData = {"UID": UID}
    #     mydict = {"$set":{"fname": fname, "Lname": Lname, "City": City, "Country": Country}}
    #     output = studentTable.update_one(findData, mydict)
    # else  :
    mydict = {"fname": fname, "Lname": Lname, "City": City, "Country": Country}
    output= studentTable.insert_many([mydict]).inserted_ids
    for i in output:
        print(i)
        studentTable.update_one({"_id" : i}, {"$set":{"UID":str(i)}})

    output = studentTable.find({},{"_id":0})
            # print(output)
    all_x = []

    for x in output:
                all_x.append(x)
    return all_x
