from sys import stdin
"""
11586
Train Tracks - Uva online judge - Juan José Hoyos
python 3
"""
def main():
    tc = int(input())
    for i in range(tc):
        words = {"M":0,"F":0}
        line = stdin.readline().split()
        for i in line:
            for j in range(len(i)):
                if i[j]=="M":
                    words["M"]+=1
                else:
                    words["F"]+=1


        if words["M"]==words["F"] and len(line)>1:
            print("LOOP")
        else:
            print("NO LOOP")
main()
