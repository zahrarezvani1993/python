# name = input("please your name: ")
# hwork = int(input("Hours of work: "))
# hsalary= int(input("Salary for one hour of work: "))

# def salary(hwork,hsalary):
#     salary = hwork*hsalary
#     return salary

# print("%s aziz... hoghoghe shoma %s toman ast."%(name,salary(hwork,hsalary)))


# print(type(3))

# print(max(1,5))



# n = 15
# while n>0:
#     print(n)
#     n=n+1
#     if n==100:
#         break


        


# count = 0
# name = ["zahra","moien","ghasem"]
# for i in name:
#     print(i)
#     count = count+1
# print(count)




# import random
# javab = random.randint(1,100)
# hads = int(input("ye adad bein 1 to 100 vared kon"))
# print("javab:",javab," hadse:",hads)

# while hads != javab:
#     if hads > javab:
#         print("javab kochictare")
#     else:
#         print("javab bozorgtare")
#     hads = int(input("ye adad bein 1 to 100 vared kon"))

# print("hadse shoma doroste")





# name = "moein"
# name2 = "M" + name[1:]
# print(name2)
# count = 0

# for harf in name:
#     print(harf)
#     count = count+1
# print(count)
# print(name[-3])
# print(name[2])
# print(name2[0])
# print(len(name2))

# for i in range(0,len(name)):
#     print(i,name[i])


# string="asdfhjkl. sfjkl.sfjk 23456"
# counter = dict()
# for letter in string:
#     if letter in counter:
#         counter[letter]+=1
#     else:
#         counter[letter] =1
# for i in list(counter.keys()):
#     print("tedad harf %s barabar %s"%(i,counter[i]))


# def xxx(n):
#     num=5
#     while(n>num):
#         yield num
#         num +=1


# for i in xxx(20):
#     print(i)

# class ensan():
#     def __init__(self,name,sen):
#         self.name=name
#         self.sen=sen

#     def get_name(self):
#         print("name shoma %s hast"%(self.name))

#     def get_sen(self):
#         print("sen shoma %s hast"%(self.sen))


# class ensan2(ensan):
#     def __init__(self,name,sen,cod):
#         ensan.__init__(self,name,sen)
#         self.cod=cod

#     def get_cod(self):
#         print("%s aziz code shoma %s hast" %(self.name,self.cod))

# user1=ensan("zahra",29)
# user1.get_name()
# user1.get_sen()

# user2=ensan2("moein",4,50)
# user2.get_cod()



# import re

# email="zahrafjkh@ads.com"

# result= re.search(r'.+\@.+\..{2,3}',email)
# print(result)




# str="the price 200$ for 2 boshke today. the price 350$ for 3 boshke manday. the price 450$ for 4 boshke saterday."

# import re

# result=re.findall(r"the price (\d+\$) for (\d+) boshke (\w+)\.",str)
# print(result)
# print(type(result))

# for price,boshke,roz in result:
#     print(price,boshke,roz)

# import re
# str=re.sub(r'today\.','sunday.',str)




# import requests
# response= requests.get("https://divar.ir")
# print(response)
# print(response.text)
# print(response.status_code)



# myList=[print(x+2) for x in range(1,10) if x%2==0]




# from timeit import timeit
# def loop1():
#     [x+1 for x in range(100) if x>10]

# def loop2():
#     mylist=[]
#     for x in range(100):
#         if (x>10):
#             mylist.append(x+1)

# def loop3():
#     mylist=[]
#     for x in range(100):
#         if (x>10):
#             pass

# print(timeit("loop1()",setup="from __main__ import loop1"))
# print(timeit("loop2()",setup="from __main__ import loop2"))
# print(timeit("loop3()",setup="from __main__ import loop3"))



# a=[s.upper() for s in "salam. khobi ? chetorii ?"]

# b=[w.strip(",") for w in "sfa , sjasah, sjaj , ,czdf, asdngsf, d ,"]

# jomle="salam. khobi ? chetorii ?"
# print(jomle.split())

# print("*".join(sorted(jomle.split())))

# lista=[x if x in "aeoiu" else "-" for x in "apple , orang"]
# print(lista)

# def loop(x):
#     return (x,x+10)

# a=[x+1 for x in range(5) for x in loop(x)]
# print(a)

# az=[x for x in sorted([[3,8],[2,7],[1,6]])]
# print(az)

# names=["zahra","moein","ghasem"]
# mapa=map(len,names)
# print(list(mapa))
# print(mapa)
# print([len(name) for name in names])

# numbers=[1,2,46,73,12,37]
# print([number*0.01 for number in numbers])

# lista=[10,20,59]
# listb=[12,14,43]
# listc=[30,5,22]
# def avarage(*args):
#     return(sum(args)/len(args))
# print(list(map(avarage,lista,listb,listc)))

# names=["zahra","moein","ghasem"]
# def salam(name):
#     return ("salam "+name)

# def salammm(*args):
#     for item in args:
#         return("salammm "+item)

# print(list(map(salammm,names)))

# names=["zahra","sara","moein","ghasem","amir"]
# def lon_name(name):
#     return(len(name)>4)
# print(list(map(lon_name,names)))
# print(list(filter(lon_name,names)))
# print(map(lon_name,names))

# numbers=[1,2,46,73,12,37]
# def zoj(num):
#     if num%2==0:
#         return("zoj")
# print(list(map(zoj,numbers)))
# print(list(filter(zoj,numbers)))



# dicta={x:x**2 for x in [1,2,3,4]}
# print(dicta)
# print(dict((x,x**2) for x in [1,2,3,4] if (x<4)))

# gen1=(x*2 for x in range(10))
# print(gen1)
# print(type(gen1))
# for i in gen1:
#     print(i)


# def disable1(f):
#     pass

# @disable1
# def func1():
#     print("kljsfj")

# func1()



# import json
# dict ={
#     "car":"trr",
#     "color":"fjk",
#     "model":"hft"
#     }
# with open("cartable.json","w") as f:
#     json.dump(dict,f)

# with open("cartable.json","r") as f:
# print(json.dumps(dict,indent=5))



# class err1(Exception):
#     pass

# try:
#     raise err1("sfasjf")
# except err1 as e:
#     print("513456")

# def negativ_err(adad):
#     if adad<0:
#         raise ValueError("adad shoma manfi ast.")
#     return(adad)

# print(negativ_err(33))

# try:
#     a=2/0
#     print(a)
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("jsh")
# finally:
#     print("12456")

# def fard_be_zoj(adad):
#     if adad%2==0:
#         raise ValueError("adad shoma zoj ast")
#     return (adad+1)
# print(fard_be_zoj(3))