# 5_3 외계인 색깔

enemy=["green","yellow","red"]
point=0
sumpoint=0
cycle=len(enemy)  

if cycle > 1:
    killed=input("enter enemy color you bursted!!")
    if killed in enemy:
        if killed == "green":
            point = 5
            sumpoint=sumpoint+point
            print(f"You Kill {killed} enemy. You got {point} point!! Your total Point is {sumpoint}")
            enemy.remove(killed)
        else:
            print(f"You Kill {killed} enemy. You connot get point. Your total Point is {sumpoint}")    
else :
    print("You are die.")
    
