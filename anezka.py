
def uloha(n):                                    #23568 $$
    dicta = {}
    for i in range(n):
        dicta[i] = [""]*n
        dicta[i][(2*i)%n] = str(0)
        dicta[i][(1+(2*i))%n] = str(1)   
    
    if n==1: #1111
        return False,str("^(0|1)+$")
    
    else:
        for q in range(n-1):
            n = len(dicta)
            x = n+1
            y = n-1                             ###!
            for i in range(n):    
                if not dicta[i][y]: 
                    continue
                for j in range(n):
                    if not dicta[y][j]: 
                        continue

                    if  dicta[i][j] == False  and dicta[y][y] == False:
                        dicta[i][j] = str("(?:"+dicta[i][y]+")(?:"+ dicta[y][j]+")")
                        continue

                    elif not dicta[i][j] :  #elif not dicta[i][i] Fa
                        dicta[i][j] = str("(?:" + dicta[i][y] + ")(?:"+ dicta[y][y] +")*(?:"+dicta[y][j]+")")
                        continue

                    elif not dicta[y][y]:
                        dicta[i][j] = str("(?:" + dicta[i][j] + ")|(?:"+ dicta[i][y]  +")(?:" + dicta[y][j] + ")")
                        continue

                    elif True:
                        dicta[i][j] = str(("(?:"+dicta[i][j]+")|(?:(?:" + dicta[i][y]+")(?:" + dicta[y][y]+ ")*(?:"+ dicta[y][j]+ "))"))
                        continue
            del dicta[y]
        return False,str("^("+dicta[0][0]+")+$")

# Testy:
from re import match
correct = True
is_automaton, reg = uloha(3)
if is_automaton:
    print("Na toto sú len skryté testy pri odovzdaní")
    testy = False
else:
    for i in range(100):
        if not match(reg, bin(i * 3)[2:]):
            print("Chyba, false positive pre hodnotu: ", bin(i * 3))
            correct = False
            break

    for i in range(100):
        if match(reg, bin(i * 3 + 3)[2:]):
            print("Chyba, false negative pre hodnotu: ", bin(i * 3 + 3))
            correct = False
            break
if correct:
    print("Zadanie spĺňa základné testy")

