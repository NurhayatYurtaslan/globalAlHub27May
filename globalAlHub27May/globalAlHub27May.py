#LIST
# creating a list
mylist = [3,5,6,7]
print(mylist)
print("--------------------------------------------------")
print(type(mylist))
print("--------------------------------------------------")
print(mylist[0])
print(mylist[2])
print(mylist[-1])
print(mylist[-3])
print("--------------------------------------------------")
mylist[2] = "python" # lists can be taken different types of data
print(mylist)
print("--------------------------------------------------")
mylist.append('course') # append(): adding some items end of the list
print(mylist)
print("--------------------------------------------------")
mylist = [3,4,5,6,7]
mylist.append('course')
mylist.append('course')
print(mylist)
thelast = mylist.pop() # pop(): removing the last item of the list
print(thelast)
print(mylist)
print("--------------------------------------------------")
mylist.index("course")
print("--------------------------------------------------")
print(mylist.index(4))
print("--------------------------------------------------")
mylist.count("course")
print("--------------------------------------------------")
list2 = ["Python","Java","R","JavaScript","Ruby","Python","Python"]
print(list2.count("Python"))
print("--------------------------------------------------")
mylist.remove("course")
print(mylist)
print("--------------------------------------------------")
list3 = [100,23,87,13,1000]
list3.sort()
print(list3)
print("--------------------------------------------------")
list4 = [41,23,78,99,37,2.9,2.8]
list4.sort()
print(list4)
print("--------------------------------------------------")
#mylist.remove("course")
#mylist.remove("python")
print(mylist)
print("--------------------------------------------------")
mylist = [3,4,5,6,7]
mylist.reverse()
print(mylist)
print("--------------------------------------------------")
print(mylist[::-1])
print("--------------------------------------------------")
mylist2 = ["python", "course", "hello"]
mylist2.sort()
print(mylist2)
print("--------------------------------------------------")
mylist3 = [1, 11, 111, 1111]
mylist.extend(mylist3)
print(mylist)
print("--------------------------------------------------")
mylist4 = [1, 11, 111, 1111]
mylist.append(mylist4)
print(mylist)
print("--------------------------------------------------")
list_in_list = ["python","Java",3.2, 4, 11, [5,65,7,8,9]]
print(list_in_list[5])
print("--------------------------------------------------")
print(list_in_list[-1])
print("--------------------------------------------------")
mylist = [2, 3, 4, 5, 6, 'python', 'flutter', 'Android', 'JavaScript', 'dart', 3.2, 5.0]
print(mylist)
print("--------------------------------------------------")
mylist.insert(5,55) # insert(x,y) --> adding x th index the y value but don't change the x th value, it remains the same.
print(mylist)
print("--------------------------------------------------")
liste1 = list()
numbers = list(range(8))
print(numbers)
print(liste1)
print("--------------------------------------------------")
numbers2 = list(range(2,15,3)) #range(start, stop, step)
print(numbers2)
numbers2.reverse()
print(numbers2)
print("--------------------------------------------------")
print(numbers[2:5])
print("--------------------------------------------------")
numbers[5:8] = [10,11,12]
print(numbers)
print("--------------------------------------------------")
print(12 in numbers)
print(15 in numbers)
print("--------------------------------------------------")
print([1,2,3] + [4,5])
print("--------------------------------------------------")
print([1,2,3] * 3)
print("--------------------------------------------------")
list1 = [[1,2], 3, [4,5,6]]
print(list1[1])
print("************************************************************")
#Conditional Statements
num = int(input("Please enter a number: "))
if num < 0:
    number = num*(-1)  #num = num*-1
    print("Result: ", number)
print("--------------------------------------------------")
score = int(input("Please enter your score: "))
if score <= 40:
    print("Very bad, you should work hard..")
elif score <= 60:
    print("Nice but you should work more..")
elif score <= 100:
    print("Congratulation!")
else:
    print("Invalid score!!!")
print("--------------------------------------------------")
x = 8
if x > 4:
    x = x+1
elif x > 5:
    x = x+2
elif x > 7:
    x = x+3
print ("x, ", x)
print("--------------------------------------------------")
x = 5
if x > 4:
    x = x+1
if x > 5:
    x = x+2
if x > 7:
    x = x+3
print ("x, ", x)
print("--------------------------------------------------")
print("**************ATM Giriş Paneli**************")
kullanici_adi = "Nurhayat"
parola ="HELLO"
kullanici_adi1 =input("Lütfen kullanıcı adınızı giriniz")
parola1= input("Lütfen Parolanızı giriniz.")
if (kullanici_adi != kullanici_adi1 and parola == parola1):
    print("Kullanıcı adınız hatalı")
elif (kullanici_adi==kullanici_adi1 and parola != parola1):
    print("Parolanız hatalı")
elif (kullanici_adi != kullanici_adi1 and parola!= parola1):
    print("Kullanıcı adınız ve parolanız hatalıdır.")
else:
    print("Tebrikler, Başarıyla giriş yaptınız")
print("--------------------------------------------------")
x = 10
if x > 5:
    if x >7:
        print("İlker and Eylül")
print("--------------------------------------------------")

