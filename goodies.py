
fd = open(r'c:\Users\Karthik T\Desktop\High\input.txt', "r")
data = fd.readlines()#reading the contents of file into a list

emp = 1#to get no of employees
n = -3#to ignore lines until goodies names and cost
goodies = []

#making a list of lists,[[int(cost),str(goody name)]]
for each_line in data:
    if(emp):
        m = int(each_line.split(":")[1])
        emp = 0
    if(n>0):
        val = each_line.split(":")
        goodies.append([int(val[1]), val[0]])
    n+=1

goodies.sort()

#function to get N goodies with least cost difference
def indDif(goodies, m):
    i = 0
    j = m-1
    ind = i
    ans = float('inf')
    while(j<len(goodies)):
        diff = goodies[j][0] - goodies[i][0]
        if(diff < ans):
            ans = diff
            ind = i
        i+=1
        j+=1
    return (ans, ind)
ans, ind = indDif(goodies, m)

#making a list of outputs
output = ["The goodies selected for distribution are:\n", "\n"]
#adding all goodies to output list
for i in range(ind, ind+m):
    val = goodies[i][1] + ": " + str(goodies[i][0]) + "\n"
    output.append(val)

diff = "\n" + "And the difference between the chosen goodie with highest price and the lowest price is " + str(ans) + "\n"
output.append(diff)
opFile = open("output.txt", "w")
opFile.writelines(output)#writing the output to output file
opFile.close()
