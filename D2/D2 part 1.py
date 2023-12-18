result = 0
dod = False
with open("text",'r') as f :
    for line in f.readlines():
        line = line.strip().split(":")
        ngame = int(line[0].split("Game ")[1])
        load = line[1].split(";")
        for n in range(len(load)) :
            touch = load[n].strip().split(',')
            print(touch)
            for i in range(len(touch)) :
                if 'red' in touch[i] :
                    value = int(touch[i].split(" red")[0])
                    if value > 12 :
                        dod = True
                        break
                    
                if 'green' in touch[i] :
                    value = int(touch[i].split(" green")[0])
                    if value > 13 :
                        dod = True
                        break
                if 'blue' in touch[i] :
                    value = int(touch[i].split(" blue")[0])
                    if value >14 :
                        dod = True
                        break
            if dod :
                dod = False
                result -= ngame
                break
        result += ngame
print(result)           
        # print(line)
        # print(load)
        