###Print Normal###
    # name = input('What is your name?\n') #เป็นคำสั่ง input แต่จะเป็นคำถามก่อน, \n เป็นการแสดงผลในการขึ้นบรรทัดใหม่
    # print ('Hi, %s.' % name)  # %s การแสดงผลเป็น String , ตามด้วยตัวแปรที่ input เข้าไป (## %s=String,%f=float,%=integer)
    # print ('Welcome to Python')
        #print 
    ##What is your name?
    # bell (ค่าที่ input)
    # Hi, bell.
    # Welcome to Python


###print Array###
    # var_list = [ 'abcd', 123 , 1.23, 'Mindphp.com', 20.2 ]
    # var_tinylist = [123, 'mindphp']

    # print (var_list[0])       # แสดงรายการแรกของตัวแปร var_list (abcd)
    # print (var_list[1:3])     # แสดงรายการที่ สอง ถึงสามรายการถัดไป ([123, 1.23])
    # print (var_list[2:])      # แสดงรายการที่สามถึง สุดท้าย ([123, 'mindphp', 123, 'mindphp'])
    # print (var_tinylist * 2)  # แสดงรายการทั้งหมดของตัวแปร var_tinylist สองครั้ง ([123, 'mindphp', 123, 'mindphp'])
    # print (var_list + var_tinylist) # แสดงรายการทั้งหมดของ var_list, var_tinylist ร่วมกัน (['abcd', 123, 1.23, 'Mindphp.com', 20.2, 123, 'mindphp'])


###key,values###
    # var_tinydict = {'one': 'This is one ของ var_tinydict', 2:'This is two ของ var_tinydict', 'dept': 'sales'} 
    #คือ['one']=key , "This is one ของ var_tinydict"=values


###for_loop###
    # for str in 'Mindphp.com':     
    # print ('Current Letter :', str)
    # #จะ print ตัวอักษรที่ละตัว ดูจะfor

    # list = ['http', 'mindphp',  'com']
    # for l in list:   # ตัวอย่างที่สอง
    # print('Current L is :',l)   #จะ print ธรรมดา เพราะได้กำหนดข้างบนเเล้ว 
    # print ('จบการทำงาน')

    #print ให้มันเรียงลำดับ
    # for i in range(len(a_var)):
    #     print(i, a_var[i])


###while_loop###
    # x=0
    # while x <5:
    #     print('Loop ที่ ', x)
    #     x +=1


###function###
    # def myfunc(): #def ตามด้วย function
    #     print ("สวัสดี สร้างฟังก์ชั่น Mindphp.com");
    # myfunc();


###loop(continue)###
    # for str in 'Mindphp.com':    
    #     if str=='d':
    #         print('ข้ามการทำงาน')
    #         continue
    #           print('การทำงานที่ถูกข้าม')
    #     print ('Current Letter :', str)
    #print#
    # Current Letter : M
    # Current Letter : i
    # Current Letter : n
    # ข้ามการทำงาน
    # Current Letter : p
    # Current Letter : h
    # Current Letter : p
    # Current Letter : .
    # Current Letter : c
    # Current Letter : o
    # Current Letter : m

    # i = 5
    # def f(j, arg="Mindphp.com"):
    #     print(arg);
    #     print(j);
    # i = 6
    # f(i)
    # f(i, "สวัสดี")


###Variable-length arguments###
    # def f_vl( arg, *vartuple ): #vartuple คืด การกำหนดตัวแปรของ f_vl( 'Mindphp.com' );
    #    "This prints a variable passed arguments"
    #    print ("Output is: ")
    #    print ("arg: ", arg)
    #    for v in vartuple:
    #        print("vartuple:" , v)
        
    # f_vl( 'Mindphp.com' );
    # f_vl( 'Mindphp.com', 'เว็บสอนเขียนโปรแกรม', 'หัดเขียนโปรแกรม' );

    # #print#
    # Output is:
    # arg:  Mindphp.com
    # Output is:
    # arg:  Mindphp.com
    # vartuple: เว็บสอนเขียนโปรแกรม
    # vartuple: หัดเขียนโปรแกรม


###หาขนาดตัวแปร โดยใช้ sys###
    # import sys

    # a = 8
    # b = 13.4
    # c = "Python"
    # d = [1, 2, 3, 4]

    # print('Size of a = ', sys.getsizeof(a))
    # print('Type of a = ', type(a))

    # print('Size of b = ', sys.getsizeof(b))
    # print('Type of b = ', type(b))

    # print('Size of c = ', sys.getsizeof(c))
    # print('Type of c = ', type(c))

    # print('Size of d = ', sys.getsizeof(d))
    # print('Type of d = ', type(d))

    # del a
    # del b, c, d

    # if 'a' in locals():
    #     print("a is exist")
    # else:
    #     print("a is not exist")


###function len() ใช้นับจำนวนคำใน word###
    # s1 = 'Mountain'
    # print('length of s1 =', len(s1))
    # length of s1 = 8


###String methods(Find and search)###
    # s = 'mountain'

    # print(s.startswith('moun'))  ##ตรวจสอบว่า คำขึ้นต้นตรงไหม
    # print(s.endswith('in'))  ##ตรวจสอบว่าคำลงท้าน ตรงกันไหม
    # print(s.find('n'))  ##ค้นหาตัวอักษรจากข้างหน้า
    # print(s.rfind('n'))  ##ค้นหาตัวอักษรจากข้างหลัง
    # print(s.replace('moun', 'con'))  ##การแทนที่คำ
    # print(s.count('a'))  ##การนับตัวอักษรที่กำหนดในประโยค

###Formatting string###
    # s = 'Python'
    # print(s.center(40))  #ตัวอักษรให้อยู่ตรงกลาง เลือกเลขเว้นตัวอักษร
    # print(s.ljust(10))  #ตัวอักษรให้อยู่ตรงขวา เลือกเลขเว้นตัวอักษร
    # print(s.rjust(10))  #ตัวอักษรให้อยู่ตรงซ้าย เลือกเลขเว้นตัวอักษร
    # print(s.center(10, '*'))  #ตัวอักษรให้อยู่ตรงกลาง เลือกเลขเว้นตัวอักษร แล้วเพิ่ม #

    # number = '83'
    # print(number.zfill(6)) #เติม 0 ข้างหน้าตัวเลข
    # print('-1.32'.zfill(8))


###Key and Value###
    # countries = {'de': 'Germany', 'ua': 'Ukraine',
    #              'th': 'Thailand', 'nl': 'Netherlands'}

    # for k, v in countries.items():
    #     print(k, v)

    # #print key only
    # print('Key:', end = ' ')
    # for k in countries.keys():
    #     print(k, end = ' ')

    # #print value only
    # print('\nValue:', end = ' ')
    # for v in countries.values():
    #     print(v, end = ' ')


###Python Dictionary methods###
    # countries = {'de': 'Germany', 'ua': 'Ukraine',
    #              'th': 'Thailand', 'nl': 'Netherlands'}

    # print(countries.get('Germany')) # equal to countries['de'] #print
    # countries.setdefault('tr', 'Turkey')

    # print(countries.popitem()) #print ('tr', 'Turkey')
    # print(countries.popitem()) #print ('nl', 'Netherlands')

    # print(countries.items() #print ('de', 'Germany'), ('ua', 'Ukraine'), ('th', 'Thailand')



###Exception###
    # ถ้ามีclass มันจะดักการแสดง error เอง พวก password จะโดนปิดไว้
    # class UsernameError(Exception):

    #     def __init__(self, message, error):
    #         super().__init__(message)
    #         self.message = message
    #         self.error = error

    #     def getMesssage(self):
    #         return self.message + ' \'' + self.error  + '\''

    # class PasswordError(Exception):

    #     def __init__(self, message, error):
    #         super().__init__(message)
    #         self.message = message
    #         self.error = error

    #     def getMesssage(self):
    #         return self.message + ' \'' + ('*' * len(self.error))  + '\''

    # โปรแกรมเริ่มการทำงาน
    # try:
    #     print('Login')
    #     username = input('Username: ')
    #     password = input('Password: ')

    #     if (username != 'mateo'):
    #         raise UsernameError('Invalid username', username)

    #     if (password != '1234'):
    #         raise PasswordError('Invalid password', password)

    #     print('Login success')

    # except UsernameError as e:
    #     print('Exception: ', e.getMesssage())

    # except PasswordError as e:
    #     print('Exception: ', e.getMesssage())


###การสร้างคลาสและออบเจ็ค###
    # class Person:

    #     def __init__(self, firstName, lastName):
    #         self.firstName = firstName
    #         self.lastName = lastName

    #     def getName(self):
    #         return self.firstName + ' ' + self.lastName

    # p = Person('Chase', 'Rice')
    # p.career = 'Singer'
    # p.country = 'USA'

    # print('Name: ' + p.getName())
    # print('Career: ' + p.career)
    # print('Country: ' + p.country)

    # p2 = Person('Max', 'Graham')
    # p2.genres = ['Electronica', 'trance', 'tech house', 'techno']

    # print('Name: ' + p2.getName())
    # print('Genres: ', p2.genres)


###function หาพื้นที่###
    # def rectangle (w,h) : 
    #             area = w * h
    #             return area
        
    # def triangle(w,h) :
    #         area1 = (w * h) * 0.5
    #         return area1

    # w = int(input("width = "))
    # h = int(input("height ="))
    # # print(rectangle(w, h))
    # print(triangle(w, h), rectangle(w, h))


###if else###
    # score = 75
    # if score > 70:
    #     print("good")
    # else:
    #     print("no")

    # def greeting(lang):
    #     if lang == "th":
    #         ("sawadee")
    #     else:
    #         print("Hello")
    # greeting("th")

    # def ticket(age, is_local):
    #     if (age <=5 or age >= 60) and is_local:
    #         return 0
    #     else:
    #         return 100

    # print(ticket(70, True))


###tuple###ไม่ต้องตั้งตัวแปรหลายตัว
    # point = 1, 7 #x=1 , y=7
    # print(point[0])

    # pointB = (1, 7)
    # print(pointB[1])

    # th = "thailand", 5, 2, 4
    # print(th[1] + th[2] + th[3])


###ส่งกลับมาเป็น tuple###
    # def price_with_vat(amount):
    #     vat = amount * 7 / 107
    #     price = amount - vat
    #     # t = price, vat 
    #     return price, vat 

    # print(price_with_vat(107))
    # a = price_with_vat(200)
    # print(type(a))
    # print(a)
    # print("price = ", a[1])
    # p,v = price_with_vat(200)
    # print("p = ", p)
    # print("v = ", v)

    # def thai_area(sqwa):
    #     rai = sqwa // 400
    #     ngan = (sqwa - (rai * 400)) // 100
    #     wa = sqwa % 100
    #     return rai, ngan, wa

    # a = 956
    # print(thai_area(a))
    # r, n, w = thai_area(a)
    # print(r, n, w, sep="-")
 
###loop###
    # def tem_table ():
    #      for i in range(101):
    #          f = (i * 9 / 5) + 32
    #         #  print(i, "=", f)
    #          print("{}C = {:.2f}F".format(i, f))

    # tem_table()

    # def mult_table(from_n, to_n):
    #         for i in range(from_n, to_n + 1):
    #             for j in range(1, 13):
    #                 print("{} x = {} = {}".format(i, j, i * j))

    # mult_table(2,3)

