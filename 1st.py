# question 1
# num1 = int(input("enter your num1"));
# if(num1%7==0):
#     print(num1)
# else:
#     print('it is not devisible by 7');


#qustion 2
# num1 = int(input("enter your num1"));
# num2 = num1%10;
# if(num2==4):
#     print(num2);
# else:
#     print('last digit is not 4');


#question 3
# num1 = int(input("enter your num1"))
# if(num1%3==0 and num1%10==4):
#     print('the no. is divisible by 3 and last digit is 4', num1);
# else:
#     print('last digit is not 4')


#question 4
# num1 = int(input("enter your num1"))
# if(num1%3==0 or num1%10==4):
#     print('the no. is divisible by 3 and last digit is 4', num1);
# else:
#     print('last digit is not 4')


#question 5
# num1 = int(input("enter your num1"))
# if(num1%5==0 and num1%11==0):
#     print('the no. is divisible by 5 and divisible by 11', num1);
# else:
#     print('not divisible')


#question 6
# a = int(input("write vertices"))
# b = int(input("write vertices"))
# c = int(input("write vertices"))
# if(a+b+c <= 180):
#     if(a==90 or b<=90):
#         if(c<=b):
#             print("this is right angle")
#         else:
#             print("not triangle")
    


#question 7
# a = int(input("write vertices"))
# b = int(input("write vertices"))
# c = int(input("write vertices"))
# if(a+b+c != 180):
#     print("not triangle")
# elif((a==90 or b==90 or c == 90) and (a<90 or b<90 or c<90)):
#     print("right triangle")
# elif(a+b+c == 180):
#     if(((a>=90 and a<=180) or (b>=90 and b<=180) or (c>90 and c<=180)) and (b+c <= 90)):
#         print("obtuse angle")


#question 10
# num1 = int(input("enter your num1"))
# if(num1 == 0):
#     print("Monday");
# elif(num1 == 1):
#     print("Tuesday");
# elif(num1 == 2):
#     print("Wednesday");
# elif(num1 == 3):
#     print("Thursday");
# elif(num1 == 4):
#     print("Friday");
# elif(num1 == 5):
#     print("Saturday");
# elif(num1 == 6):
#     print("Sunday");
# else:
#     print("invalid")


#question 11 - average of 5 marks
# num1 = int(input("enter your marks"))
# num2 = int(input("enter your marks"))
# num3 = int(input("enter your marks"))
# num4 = int(input("enter your marks"))
# num5 = int(input("enter your marks"))
# average = (num1+num2+num3+num4+num5)/5
# print("your average is", average)  #average of 5 marks



#question 12
# num1 = int(input("enter your a"))
# num2 = int(input("enter your b"))
# num3 = int(input("enter your c"))
# if(num1+num2+num3==180):
#     print("this is triangle")
# else:
#     print("no triangle") 



#question 13 find the maximum
# num1 = int(input("enter the no. 1"))
# num2 = int(input("enter the no. 2"))
# num3 = int(input("enter the no. 3"))
# if(num1>num2 and num1>num3):
#     print("max is", num1)
# elif(num2>num1 and num2>num3):
#     print("max is", num2)
# else:
#     print("max is", num3)  #find the maximum of three numbers



#question 14 find the minimum 
# num1 = int(input("enter the no. 1"))
# num2 = int(input("enter the no. 2"))
# num3 = int(input("enter the no. 3"))
# if(num1<num2 and num1<num3):
#     print("min is", num1)
# elif(num2<num1 and num2<num3):
#     print("min is", num2)
# else:
#     print("min is", num3)  #find the minimum of three numbers


#question 15 grading System
# num = int(input("enter your marks"))
# if(num>=90):
#     print("grade is A")
# elif(num>=80):
#     print("grade is B")
# elif(num>=70):
#     print("grade is C")
# elif(num>=60):
#     print("grade is D")
# else:
#     print("grade is F")  #grading system based on marks


#question 16 find the n natural no.
# num = int(input("enter the no."))
# for i in range(1,num+1):
#     print(i)  #print the natural numbers from 1 to n



#question 4 sheet - 2
# num1 = int(input("enter your numebr"));
# for i in range(num1+1):
#     for j in range(1,i+1):
#         if(j%2==0):
#             print("*", end="")
#         else:
#             print(j, end="")
#     print()









