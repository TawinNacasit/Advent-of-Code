with open("input.txt","r") as f:
    i = 1
    Text = ''
    realText = ''
    Original = ''
    random = ''
    count  = 0
    nabcard = {}
    result = 0
    for line in f.readlines():
        
        Text = line.split(': ')[1]
        Ncard = int(line.split(': ')[0].split('Card ')[1])
        if nabcard.get(Ncard,None) == None :
            nabcard[Ncard] = 0
        nabcard[Ncard] +=  1
        realText = Text.split('| ')
        Original = realText[0] 
        random   = realText[1]
        for sett in random.strip().split() :
            
            if sett in Original.strip().split() : 
                count += 1 
        if count == 0 :
            continue
        for x in range(1,count+1) :
            if nabcard.get(Ncard+x,None) == None :
                nabcard[Ncard+x] = 0
            nabcard[Ncard+x] += nabcard[Ncard]
        count = 0
    for key, value in nabcard.items() :
        print(key,value)
        result += value
    print(result)
