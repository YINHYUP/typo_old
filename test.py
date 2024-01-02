num=int(input("주민등록번호를 입력해주세요."))
y=num //10000

#


if y>24:
    y=2024-(y+1900)
else :
    y=2024-(y+2000)

if y<12 :
    cost = ("free")
elif y<18:
    cost = ("10 USD")
else:
    cost = ("20 USD")
    
print(f"your age is {y}. your Entrance Fee is {cost}.")
