#Q2
a=5**9
print(a)

a=3//2
print(a)

a=7//3
print(a)

a=7/3
print(a)

print(6==6)

a=20
a+=30
a%=3
print(a)

print(True*False)
print(True &False)
print(True and False)
print ((6>3) and (7<4) or (18==3) and (9>3))
print(True is False)
 # print(False in 'False')      #show error
print((True== False) or (False >True)) and (False <=True)

#____________________________________________________________________________________
#Q3
s1="nice to have it "
s2="here"
print(s1 + s2)
#----------------------------------------------------------------------------------------
#Q4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11,],1,7]
print(a[3][1][2][0])


#--------------------------------------------------------------------------------

#Q5
a.insert(0,s1)
a.append(s2)
print(a)
#-----------------------------------------------------------------------------------

#Q6
number=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,
         758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,
         512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
for i in number :
    if (i==237):
        break
    elif(i%2==0):
        print(i)

    
#-------------------------------------------------------------------------------------
#Q7

color_list_1 =set(["White","Black","Red"])
color_list_2 = set (["Red" ,"Green"])

print(color_list_1-color_list_2)


#----------------------------------------------------------------------------------

#Q8

string = input("enter the string ")
string=  set (string)
alpha = list('abcdefghijklmnopqrstuvwxyz')
i=0
for word in string :
    if (word in alpha):
        i+=1
if (i==26):
    print('string is pangram')
else :
    print('string is not pangram')


#---------------------------------------------------------------------------------------

#Q9

n=(input("enter a number"))
num1=n
num2=n*2
num3=n*3
print(int (num1)+int(num2)+int(num3))


 #-------------------------------------------------------------------------------

 #Q10


#--------------------------------------------------------------------------------------
#Q11

s=input()
a= d.split(',')
a.sort()
b=','.join(a)
print(b)


#--------------------------------------------------------------------------------
#Q 12

d ={'student':['rahul','kishore','vidhya','raakhi'],'marks':[ 57,87,67,79]}
a=d['marks']
max=a[0]
for i in range(len(a)):
    if(max<a[i]):
        max=a[i]
        pos=i
print(d['students'][post])

#--------------------------------------------------------------------------------

#Q 13

s=input()
alp=0
num=0
for i in s:
    if (i.isalpha()==True):
        alp+=1
    if(i.isnumeric()==True):
        num+=1
print("LETTER",alp)
print("DIGITS",num)

#--------------------------------------------------------------------------------

#Q14
#Q15
#Q16



                
