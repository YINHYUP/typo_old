# 5_3 외계인 색깔

enemy=["green","yellow","red"]
point=0
sumpoint=0
cycle=len(enemy)  
n=0

for n in range(cycle):
    killed=input("enter enemy color you bursted!!")
    if killed in enemy:
        if killed == "green":
            point = 5
            sumpoint=sumpoint+point
            print(f"You Kill {killed} enemy. You got {point} point!! Your total Point is {sumpoint}")
            enemy.remove(killed)
            n=n+1
        elif killed == "yellow":
            point = 3
            sumpoint=sumpoint+point
            print(f"You Kill {killed} enemy. You got {point} point!! Your total Point is {sumpoint}")
            enemy.remove(killed)
            n=n+1
        elif killed == "red":
            point = 1
            sumpoint=sumpoint+point
            print(f"You Kill {killed} enemy. You got {point} point!! Your total Point is {sumpoint}")
            enemy.remove(killed)
            n=n+1        
            
    else :
        print("You are dead.")
        n=n+999

        
    
    
