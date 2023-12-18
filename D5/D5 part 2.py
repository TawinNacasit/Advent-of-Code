seeds = ''
SeedToSoil      = []
SoilToFerti     = []
FertiToWater    = []
WaterToLight    = []
LightToTemp     = []
TempToHumidity  = []
HumidityToLocal = []
allseed = []
val = ''
mylist          = None
def findlocation(listall,val):
    for i in range(len(listall)) :
        if val in range(listall[i][1],listall[i][1]+listall[i][2]) :
            res = val-listall[i][1]+listall[i][0]
            return res
    return val
with open("input.txt","r") as f:
    
    for line in f.readlines():
        line = line.strip()
        if line == '':
            continue
        elif 'seeds:' in line :
            seeds = [int(x) for x in line.split('seeds: ')[1].split()]

        elif 'seed-to-soil map:' in line:
            mylist = SeedToSoil
        elif 'soil-to-fertilizer map:' in line :
            mylist = SoilToFerti
        elif 'fertilizer-to-water map:' in line:
            mylist = FertiToWater
        elif 'water-to-light map:' in line :
            mylist = WaterToLight
        elif 'light-to-temperature map:' in line:
            mylist = LightToTemp
        elif 'temperature-to-humidity map:' in line :
            mylist = TempToHumidity
        elif 'humidity-to-location map:' in line:
            mylist = HumidityToLocal
        
        else:
            mylist.append([int(x) for x in  line.split()])
lowest = 10**100
for i in range(0,len(seeds),2) :
    c = seeds[i]
    v = seeds[i+1]
    for a in range(v) :
        res = findlocation(SeedToSoil,c+a     )
        res = findlocation(SoilToFerti,res    )
        res = findlocation(FertiToWater,res   )
        res = findlocation(WaterToLight,res   )
        res = findlocation(LightToTemp,res    )
        res = findlocation(TempToHumidity,res )
        res = findlocation(HumidityToLocal,res)
        
        if res < lowest :
            lowest = res

            
        
            
print(lowest)