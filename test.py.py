import pymongo
connection_string = "mongodb://localhost:27017"
client = pymongo.MongoClient(connection_string)
mydb = client["university"]
collection = mydb["ST"]
print("1. sakht hesab")
print("2. vorod be hesab")
vorodi = input("\nentekhab konid: ")
if(vorodi == '1'):
    first_name = input("\nenter first name: ")
    last_name = input("enter last name: ")
    user_name = input("enter username: ")
    password = input("enter password: ")
    collection.insert_one({
        "first_name": first_name,
        "last_name": last_name,
        "username": user_name,
        "password": password
    })
    print("\nsabt nam kamel shod")
    exit()
if(vorodi == '2'):
    user_name = input("\nenter username: ")
    password = input("enter password: \n")
    document = collection.find( {"username": user_name})
    record = 0
    for i in document:
        record = record + 1
        temp = i["password"]
        if(password == temp):
            print("\nvared shodid")
        else:
            print("password eshteba hast.")
            exit()
    if(record == 0):
        print("\nusername vojod nadare.")
        exit()
    
    print("\n1.namayesh dore ha")
    print("\n2. namayesh nomre")
    vorod = input("\nyek gozineh vared kon:")
    if(vorod=="1"):
        collection = mydb["CT"]
        document = collection.find()
        print(("\nname doreha.yeki ra entekhab kon:\n"))
        counter = 1
        for i in document:
            print(f"{counter}. {i["lesson"]}")
            counter += 1
        
        
        entekhab = input("\nyek dars ra entekhab kon: ")
        collection=mydb["STCT"]
        
        if (entekhab=="1"):
            collection.insert_one({
                "username": user_name,
                "lesson": "python basics",
                "grade": 0
                })
            print("\nsabt anjamid")
            
        if (entekhab=="2"):
            collection.insert_one({
                "username": user_name,
                "lesson": "python adv",
                "grade": 0
            })
            print("\nsabt anjamid")
            
        if (entekhab=="3"):
            collection.insert_one({
                "username": user_name,
                "lesson": "riazi monhadesi",
                "grade": 0
            })
            print("\nsabt anjamid")
        
        if(entekhab=="4"):
            collection.insert_one({
                "username": user_name,
                "lesson": "memari computer",
                "grade": 0
                
            })
            print("\nsabt anjamid")
            
    if(vorod=="2"): #karname
        collection=mydb["STCT"]
        document=collection.find({"username":user_name},{"_id":0,"username":0})
        for i in document:
            print(i)
        
        
        
        
        
            
            
    
    