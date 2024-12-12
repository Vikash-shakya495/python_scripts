def sum1(a,b ):
    s = a+b
    return s

print(sum1(2,5))


print("apna college" ,end=" % ")
print("vikash shakya")

print("hello " ,len("this is python course you must have to watch this"))


# default parameters
def cal_prod(a,b=23):
    print(a*b)
    return a*b

cal_prod(8);


cities = [ "delhi" , "pune" , "gurgaon" , "chennai ", " mumbai "]

heros = [ "thor" , "captain america" , "iron man" , "widow"]
def print_len(cities):
    print(len(cities))
    
    
print_len(cities)
print_len(heros)

print(cities[1],"in the of " , end="")
print(heros[2], end="\n")


def print_list(list):
    for item in list:
        print(item,end=" ")
        
print_list(heros)


# write a program to calculate factorial
def cal_fact(n):
    fact =1
    for i in range(1, n+1):
        fact *= i
        print(fact)
        
cal_fact(6)

# convert this USD to INR
def convert_INR(n):
    inr_val = n * 83
    print(n," USD = ",inr_val," INR")

convert_INR(1)



# recursion
def show(n):
    if(n ==0):
        return
    print(n)
    show(n-1)

show(5)

