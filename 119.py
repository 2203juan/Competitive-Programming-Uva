from sys import stdin
"""
119
Greedy Gift Givers - Uva online judge - Juan José Hoyos
python 3

"""
def main():
    line = stdin.readline()
    while line!=0 and line!="" and line!="\n":
        n = int(line)
        group = stdin.readline().split()
        personas = {}
        for m in group:
                personas[m] = 0
        #print(group,personas)
        for j in range(len(group)):
            tmp = stdin.readline().split()
            if len(tmp)>3:
                if int(tmp[2])!=0:
                    actual = (int(tmp[1])//int(tmp[2]))*int(tmp[2])
                    personas[tmp[0]] -=actual
                    suma = int(tmp[1])//int(tmp[2])
                    x = 3
                    while x<len(tmp):
                        personas[tmp[x]] += suma
                        x+=1
                elif int(tmp[1])!=0 and int(tmp[2])==0:
                    personas[tmp[0]] += int(tmp[1])                
            else:
                personas[tmp[0]] = personas[tmp[0]]
                                
        for h in personas:
            print(h,personas[h])
        
        line = stdin.readline()
        if line!=0 and line!="" and line!="\n":
            print()
            
main()
