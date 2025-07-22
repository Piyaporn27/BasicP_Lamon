distance = int(input("ระยะทาง:"))

if distance >= 5 and distance <= 50:
    print("ราคา 10 บาท")
elif distance >= 51 and distance <= 100:
    print("ราคา 15 บาท")
elif distance >= 101 and distance <= 300:
    print("ราคา 25 บาท")
elif distance >= 301 and distance <= 500:
    print("ราคา 35 บาท")
elif distance  > 500:
    print("ราคา 45 บาท") 
else : 
    print("ราคา 0 บาท")
