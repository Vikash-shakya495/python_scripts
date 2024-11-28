cars = ["volvo", "ford", "honda", "tata"]

for car in cars:
    print(car)


newCar = ["lambo", "maruti"]
cars.append(newCar)
print(cars)
print(cars[0])
print(cars[0:2])
print(cars.pop(4))
print(cars)

modernCar = ['farrari','creta']
newCar.extend(modernCar)
print(newCar)

num = [1,2,3,4,5,6,8,9,10]
for squa in num:
    print(squa*squa)

def calc(num1,num2, oper):
    if(oper == "+"):
        print(num1 + num2)
    elif(oper == "-"):
        print(num1-num2)
    elif(oper == "/"):
        print(num1/num2)
    elif(oper == "*"):
        print(num1*num2)

calc(3,4,"+")