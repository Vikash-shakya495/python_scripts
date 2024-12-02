info = {
    "key":"value",
    "name":"Vikash",
    "age":25,
    "is_Adult": True,
    "Marks":94.4,
    "Subjects":["Javascript","React","Nodejs"],
    420:"Yes"
}

print(info["name"],info["Subjects"],info["age"])
info["name"] = "Suraj"

student={
    "name":"Rahul Kumar",
    "subject":{
        "Maths":90,
        "Science":85
    },
    "Age":19
}

print(student["subject"]["Maths"])
print(student.keys())
print(student.values())
print(len(student))
newList =list(student.values())
print(newList)

dict1 = {"name":"vikash","age":19}
dict2 ={"Subjects":{"maths":89,"English":82,"Phe":99,"IP":97}}
dict1.update(dict2)
print(dict1)


collection =set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("Hello world")
collection.add((6,4,5,))
print(collection)
print(len(collection))
collection2 = {"Hello world","this is" , "my name" ," is vikash"}
print(collection.union(collection2))
print(collection.intersection(collection2))


subject = {'python','java','c++','python','javascript','java','python','java','c++','c'}
print(len(subject))

marks ={}
x =int(input("enter phy:"))
marks.update({"Phy":x})
y =int(input("enter maths:"))
marks.update({"maths":y})
z =int(input("enter chem:"))
marks.update({"chem":z})
print(marks)

store = {
    ("int",9),("float", 9.0)
}
print(store)