import sys

def money(salary:int, hours:int, bonus:int ) ->int:
    return salary*hours + bonus

print(money(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

