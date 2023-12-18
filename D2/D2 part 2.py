result = 0


with open("text",'r') as f :
    for line in f.readlines():
        line = line.strip().split(":")
        ngame = int(line[0].split("Game ")[1])
        load = line[1].split(";")
        red = []
        green = []
        blue = []
        for n in range(len(load)) :
            touch = load[n].strip().split(',')
            #print(touch)
            
            for i in range(len(touch)) :
                if 'red' in touch[i] :
                    value = int(touch[i].split(" red")[0])
                    red.append(value)
                    
                if 'green' in touch[i] :
                    value = int(touch[i].split(" green")[0])
                    green.append(value)

                if 'blue' in touch[i] :
                    value = int(touch[i].split(" blue")[0])
                    blue.append(value)
        red.sort()
        green.sort()
        blue.sort()
        print(red,green,blue)
        result += red[-1] * green[-1] * blue[-1]
            
        
print(result)           
        # print(line)
        # print(load)
        