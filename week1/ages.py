age = int(input("age > "))

if age > 0 and age < 13:
    print("เด็ก")
elif age >= 13 and age <= 19:
    print("วัยรุ่น")
elif age >= 20 and age <= 59:
    print("ผู้ใหญ่")
elif age >= 60 :
    print("ผู้สูงอายุ")
else:
    print("ไม่ทราบ")
