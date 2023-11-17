n = int(input("enter numbers :"))
normal_n = n
n = n **2

counter = 1      

temp = 0
print(f"{normal_n}**2 = ",end="")

while temp !=n:

   
    temp += counter
    print(f"{counter}+",end="",flush=True)
        
    counter += 2 
    
    

print(f"={temp}")