#-----Tuple คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ แต่แก้ไขไม่ได้ เพิ่ม ลบก็ไม่ได้-------------------
        #   0   1   2   3   4          5    
my_tuple1 = (10, 20, True, 10,'SAU' , (20,'Iot'))
        #   6   5   4    3   2       1     ติด -

# การเข้าถึงข้อมูลใน Tuple เพื่อเอาข้อมูลมาใช้ ห้ามแก้
# เข้าถึงแต่ละข้อมูล

print(my_tuple1[4]) # SAU
print(my_tuple1[-2]) # SAU
print(my_tuple1[5]) # [20, 'IoT]
print(my_tuple1[-1]) # [20, 'IoT]
print(my_tuple1[5][-1]) # IoT
print(my_tuple1[-1][-1]) # IoT

# เข้าถึงทีละหลายข้อมูล เราเรียกการ Slicing ผลลัพท์จะเป็น Tuple
print(my_tuple1[1:4]) #20, True 10
print(my_tuple1[3:]) #10, 'SAU', [20, 'IoT']
print(my_tuple1[:3]) #10, 20, True

# เข้าถึงทุกข้อมูล
for info in my_tuple1 :
        print(info, end=',')

print()

# หากอยากจะแก้ข้อมูลใน Tuple ก็พอทำได้ แต่ต้องอ้อมๆหน่อย
my_list = list(my_tuple1)
print(my_list)
my_list[4]='IoT'
my_tuple1 = tuple(my_list)
print(my_tuple1)

# Tuple Mathod
print(my_tuple1.count(10)) # 2
print(my_tuple1.index(True)) 

#Tuple function 
my_tuple3 = [10, 20 ,10, 30, True]
print(len(my_tuple3))
print(min(my_tuple3))
print(max(my_tuple3))