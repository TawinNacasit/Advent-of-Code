direction = None
network = {}
i = 0
with open("newest.txt", "r") as f:
    for line in f.readlines():
        if i == 0:
            direction = line.strip()

        elif line.strip() == "":
            pass

        else:
            line = line.strip()
            pos1 = line.split(" = ")[1].strip("()").split(", ")[0]
            pos2 = line.split(" = ")[1].strip("()").split(", ")[1]
            original = line.split(" = ")[0]
            network[original] = {
                "name": line.split(" = ")[0],
                "L": line.split(" = ")[1].strip("()").split(", ")[0],
                "R": line.split(" = ")[1].strip("()").split(", ")[1],
            }

            # print(pos1,pos2,original)

        i += 1


pointer = network["AAA"]

count = 0
found = False
while not found :
   
    for Direc in direction:

        pointer = network[pointer[Direc]]
        count += 1
        if pointer['name'] == 'ZZZ' :
            found = True
            break 
print(count) 
