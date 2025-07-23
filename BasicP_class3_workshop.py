monster = 999
arrow = 100
bomb = 500
sword = 250

while True:
    print("1.สู้ต่อ")
    print("2.ยอมแพ้")
    option = input("number :")
    if option == "1":
        times = int(input("times : "))
        for i in range(times):
            print("พิมพ์ 1 เพื่อใช้ธนู พิมพ์ 2 เพื่อใช้ระเบิด พิมพ์ 3 เพื่อใช้ดาบ")
            T = int(input("ใช้อะไรตี : "))
            if T == 1 :
                monster = monster - arrow
                print("ใช้ธนูพลังโจมตี 100")
                print("เหลือ",monster)
            elif T == 2 :
                monster = monster - bomb 
                print("ใช้ระเบิดพลังโจมตี 500")
                print("เหลือ",monster)
            elif T == 3 :
                monster = monster - sword
                print("ใช้ดาบพลังโจมตี 250")
                print("เหลือ",monster)
            if monster == 0:
                print("ตายแล้วจ้าแม่")
                break
            elif monster <0:
                monster = 20
                print("monster กลับมาเลือด+20")
        print("lose")
        print("HP: ", monster)
        break
    
    if option == "2":
        break

        