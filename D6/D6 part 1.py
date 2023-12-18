import math

Time = []
Distance = []
solcount = 1
with open("newinput.text", "r") as f:
    for line in f.readlines():
        if "Time:" in line:
            Time = line.split("Time:")[1].split()
        else:
            Distance = line.split("Distance:")[1].split()
    for i in range(len(Time)):
        data1 = math.floor(
            (int(Time[i]) + math.sqrt(int(Time[i]) ** 2 - 4 * (int(Distance[i]) + 1))) / 2
        )
        data2 = math.ceil(
            (int(Time[i]) - math.sqrt(int(Time[i]) ** 2 - 4 * (int(Distance[i]) + 1))) / 2
        )
        solcount *= data1 - data2 +1
print(solcount)
