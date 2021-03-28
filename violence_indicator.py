with open(r"C:\Bojan\violence.txt", "r") as violence, open(r"C:\Bojan\moj_text.txt", "r") as text,\
open(r"C:\Bojan\safe_tales.txt", "a") as safe_tales:
    clean_list = []
    for line in violence.read().splitlines():
        clean_list += line[3:].split(", ")
        
    violence_indicator = 0
    test = text.read()
    
    for x in clean_list:
        
        if x.lower() in test:
            
            violence_indicator += 1
    print(violence_indicator)
    
    if violence_indicator <= 10:
        print("This is under age of 10")
        print(test.splitlines()[0], violence_indicator, file = safe_tales )
    elif violence_indicator >10 and violence_indicator <=15:
        print("This is under age of 12")
    elif violence_indicator > 15 and violence_indicator <=20:
        print("This is under age of 16")
    elif violence_indicator > 20 and violence_indicator <=30:
        print("This is under age of 16 - 18")
    
    else:
        print("This is 18. plus")
        
        
   
    
    
    
        
    
        
    

        
    
