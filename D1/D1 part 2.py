import re
with open("input.txt","r") as f:
    result = 0
    digit = {'one': 1,
             'two': 2,
             'three': 3,
             'four': 4,
             'five': 5,
             'six': 6,
             'seven': 7,
             'eight': 8,
             'nine': 9}
    for line in f.readlines():
        ls = (re.findall(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))', line))
        firstnum = (ls[0])
        if firstnum in digit :
            firstnum = digit[firstnum]*10
        else :
            firstnum = int(firstnum)*10
        lastnum  = ls[-1]
        if lastnum in digit :
            lastnum = digit[lastnum]
        else :
            lastnum = int(lastnum)
        result += firstnum+lastnum
    print(result)
