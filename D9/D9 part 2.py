def solve(seq):
    ls = []
    count = 0
    for i in range(len(seq)-1) :
        diff = seq[i+1] - seq[i]
        ls.append(diff)
        if diff == ls[0] :
            count += 1
    if count == len(ls) :
        return seq[0] - ls[0]

    return seq[0] - solve(ls) 
    
        
result = 0
with open("text",'r') as f :
    for line in f.readlines() :
        seq = []

        for number in line.split():
            seq.append(int(number))
        
        result += (solve(seq))
print(result)