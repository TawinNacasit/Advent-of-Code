mapp = []
def ii(mapp) :
    doublebreak = False
    for pos1 in range(len(mapp[0])-1) :
        for kayab in range(len(mapp[0])):
            if pos1-kayab+1 < 0 or pos1+kayab >= len(mapp[0]):
                res = pos1+1
                return res
            for line in range(len(mapp)) :
                if mapp[line][pos1-kayab+1] != mapp[line][pos1+kayab] :
                    doublebreak = True
                    break
                
            if doublebreak :
                doublebreak = False
                break
    doublebreak = False
    for pos2 in range(len(mapp)-1) :
        for kayab in range(len(mapp)):
            if pos2-kayab+1 < 0 or pos2+kayab >= len(mapp):
                res = (pos2+1)*100
                return res
            for collum in range(len(mapp[0])) :
                if mapp[pos2-kayab+1][collum] != mapp[pos2+kayab][collum] :
                    doublebreak = True
                    break
                
            if doublebreak :
                doublebreak = False
                break

res = 0
with open("text","r") as f :
    for line in f.readlines() :
        line = line.strip()
        if line == '' :
            res +=ii(mapp)
            
            mapp = []
        else :
            mapp.append(line)
        #print(mapp)
res += ii(mapp)
print('gjggghjfghjnghj ',res)
    