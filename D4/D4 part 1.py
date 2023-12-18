with open("input.txt","r") as f:
    i = 1
    Text = ''
    realText = ''
    Original = ''
    random = ''
    count  = 0
    result = 0
    for line in f.readlines():
        Text = line.split(': ')[1]
        realText = Text.split('| ')
        Original = realText[0] 
        random   = realText[1]
        for sett in random.strip().split() :
            if sett in Original.strip().split() :
                count += 1
        if count == 0 :
            continue
        result += 2**(count-1)
        count = 0
    print(result)
