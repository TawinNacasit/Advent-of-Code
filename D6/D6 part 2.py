import math

Time = 0
Distance = 0
solcount = 1
with open("newinput.text", "r") as f:
    for line in f.readlines():
        if "Time:" in line:
            Time = ''.join(line.split("Time:")[1].split())
        else:
            Distance = ''.join(line.split("Distance:")[1].split())
    
    data1 = math.floor(
        (int(Time) + math.sqrt(int(Time) ** 2 - 4 * (int(Distance) + 1))) / 2
    )
    data2 = math.ceil(
        (int(Time) - math.sqrt(int(Time) ** 2 - 4 * (int(Distance) + 1))) / 2
    )
    solcount = data1 - data2 +1
print(solcount)
