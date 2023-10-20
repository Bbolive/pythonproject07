#character in string has index number
    # 0123456789123
infoA = 'Hello SAU 2023'
    # 43240987654321 คือ ติด -

print(infoA[6]) # 5
print(infoA[-8]) #5

# เข้าถึงตัวอักษรหลายๆตัวใน sring เราจะใช้วิธี Slicing ด้วย index number
# SAU
print(infoA[6:9])
print(infoA[-8:-5])

# 0 SAU 20
print(infoA[4:12])

# String Method
print( infoA.upper() ) #ตัวพิมพ์ใหญ์
print( infoA.lower() ) #ตัวพิมพ์เล็ก
print( infoA.capitalize() )#
print( infoA.count('l') )#นับจำนวนตัวอักษรหรือ
print( infoA.isdigit() )#นับว่ามีตัวเลขไหม
print( infoA.islower() )#นับว่ามีพิมพ์เล็กกี่ตัว
infoB = infoA.replace('SAU','IoT')
print(infoA)
print(infoB)
print(infoB.replace('Hello','Hi....'))


#String String
print(len(infoA))