# Define new function called 'uloha'. Accepts 1 input parameter 'n'.
def uloha(n):

    # print("DEBUG: Function 'uloha' called with parameter n =",n,"working with array",n,"x",n)
    
    # Define empty array called 'dicta'.
    dicta = {}
    
    # Starts a for loop based on range(n). For n=7, range(n) = 0,1,2,3,4,5,6 (7 iterations of the loop).
    # This loop creates a multi-dimensional array of size n x n. For n=7 the array is 7x7.
    # Array example for n=7
    # 0: ['0', '1', ' ', ' ', ' ', ' ', ' ']
    # 1: [' ', ' ', '0', '1', ' ', ' ', ' ']
    # 2: [' ', ' ', ' ', ' ', '0', '1', ' ']
    # 3: ['1', ' ', ' ', ' ', ' ', ' ', '0']
    # 4: [' ', '0', '1', ' ', ' ', ' ', ' ']
    # 5: [' ', ' ', ' ', '0', '1', ' ', ' ']
    # 6: [' ', ' ', ' ', ' ', ' ', '0', '1']
    for i in range(n):
        # print(" DEBUG: For loop where i =",i)
        # print(" DEBUG: Filling array index",i,"with value =",[""]*n)
        dicta[i] = [""]*n
        # print(" DEBUG: Filling array index",i,(2*i)%n,"with value =",str(0))
        dicta[i][(2*i)%n] = str(0)
        # print(" DEBUG: Filling array index",i,(1+(2*i))%n,"with value =",str(1))
        dicta[i][(1+(2*i))%n] = str(1)   
        # print("DEBUG: Array dicta contains:",dicta)
    # print("DEBUG: Array dicta contains:",dicta)

    # If we are looking for binary numbers that can be divided by 1, we can allow all binary numbers.
    # This condition captures if n=1 and hardcodes regex into '^(0|1)+$':
        # ^...$   => matching from beginning of the line till the end
        # (0|1)+  => Match one or more combination of 0 or 1 (which effectively matches all binary numbers)
        # Explanation & example: https://regex101.com/r/bkWlW8/1
    if n==1:
        return False,str("^(0|1)+$")
    
    # If however we do not have n==1, we need to start more complex regex creation
    else:
        # Starts a for loop based on range(n-1). For n=7 it will be 6 iterations of the loop.
        for q in range(n-1):
            # print(" DEBUG: LOOP 'q' >> Iteration ", q)
            # print("  DEBUG: n =",len(dicta),", x = ",n+1,", y = ",n-1)

            # Get current length of our dicta array.
            n = len(dicta)
            # Setting variable x to n+1. For n=7 variable x will have value of 8.
            x = n+1
            # Setting variable y to n-1. For n=7 variable y will have value of 6.
            y = n-1

            # Starts a for loop based on range(n). For n=7 it will be 7 iterations
            for i in range(n):
                # print("   DEBUG: LOOP 'i' >> Iteration",i, "working with dicta with index[",i,"][",y,"] = ",dicta[i][y])
                
                # Condition - checks if array dicta on index [i][y] is 0 (0 = false). Skips this loop iteration (continue) if it equals 0.
                if not dicta[i][y]:
                    # print("    DEBUG: dicta[",i,"][",y,"] is empty - skip this iteration")
                    continue

                # Starts a for loop based on range(n). For n=7 it will be 7 iterations
                for j in range(n):
                    # print("    DEBUG: LOOP 'j' >> Iteration",j, "working with dicta with index[",y,"][",j,"] = ",dicta[y][j])

                    # In this inner-most loop, we start a set of conditions, as soon as first is a match, it will override specific value in dicta array and end current loop iteration.

                    # Condition - checks if array dicta on index [y][j] is 0 (0 = false). Skips this loop iteration (continue) if it equals 0.
                    if not dicta[y][j]: 
                        # print("    DEBUG: dicta[",y,"][",j,"] is empty - skip this iteration")
                        continue

                    # Condition - checks if array dicta on index[i][j] has value 0 (False) AND at the same time dicta on index[y][y] has value 0 (False).
                    # If this condition check is matched, it will overwrite dicta value on index[i][j] with string created by str("(?:"+dicta[i][y]+")(?:"+ dicta[y][j]+")").
                    # Example: Lets consider dicta[i][y] == 0, dicta[y][j] == 1, the final regex will be: '(?:0)(?:1)'.
                    if  dicta[i][j] == False  and dicta[y][y] == False:
                        dicta[i][j] = str("(?:"+dicta[i][y]+")(?:"+ dicta[y][j]+")")
                        continue

                    # Condition - checks if array dicta on index[i][j] has value 0 (False).
                    # If this condition check is matched, it will override dicta value on index[i][j] with string created by str("(?:" + dicta[i][y] + ")(?:"+ dicta[y][y] +")*(?:"+dicta[y][j]+")").
                    # Example: Lets consider dicta[i][y] == 0, dicta[y][y] == 1, dicta[y][j] == 0, the final regex will be: '(?:0)(?:1)*(?:0)'
                    elif not dicta[i][j] :  
                        dicta[i][j] = str("(?:" + dicta[i][y] + ")(?:"+ dicta[y][y] +")*(?:"+dicta[y][j]+")")
                        continue

                    # Condition - checks if array dicta on index[y][y] has value 0 (False).
                    # If this condition check is matched, it will override dicta value on index[i][j] with string created by str("(?:" + dicta[i][j] + ")|(?:"+ dicta[i][y]  +")(?:" + dicta[y][j] + ")").
                    # Example: Lets consider dicta[i][j] == 0, dicta[i][y] == 1, dicta[y][j] == 0, the final regex will be: '(?:0)|(?:1)(?:0)'
                    elif not dicta[y][y]:
                        dicta[i][j] = str("(?:" + dicta[i][j] + ")|(?:"+ dicta[i][y]  +")(?:" + dicta[y][j] + ")")
                        continue

                    # Condition - last condition that is always True. This is a specific "catch-all" condition that is used if none of the above are matched.
                    # If the code reaches this condition, it means none of the above were match.
                    # Array dicta on index [i][j] will be overriden by value generate by str(("(?:"+dicta[i][j]+")|(?:(?:" + dicta[i][y]+")(?:" + dicta[y][y]+ ")*(?:"+ dicta[y][j]+ "))")).
                    # Example: Lets consider dicta[i][j] == 0, dicta[i][y] == 1, dicta[y][y] == 0, dicta[y][j] == 1 the final regex will be: '(?:0)|(?:(?:1)(?:0)*(?:1))'
                    elif True:
                        dicta[i][j] = str(("(?:"+dicta[i][j]+")|(?:(?:" + dicta[i][y]+")(?:" + dicta[y][y]+ ")*(?:"+ dicta[y][j]+ "))"))
                        continue

            # After every iteration of 'for j in range(n):' loop, we are removing the last index from our dicta array.
            # In first iteration, variable y equals to number 6, which points to last index number in our array.
            # With every other iteration, variable y is counted again from current length of dicta array, therefore this always removes last index.
            del dicta[y]

            # print("  DEBUG: Array dicta contains:",dicta)

        # Now that we finished all 'j' and 'i' and 'q' loops, we should have just single value in our array dicta, on index [0][0].
        # This value of dicta[0][0] contains raw regex that finds binaries divisable by value n.
        # Last 'return' line just adds '^' and '+$' characters to ensure the regex is taking whole line (^..$), and also allows one or more repetitions of the whole regex (+).
        return False,str("^("+dicta[0][0]+")+$")
        
# Testy:
# Importing function match() from library 're'.
# Details about the function: https://www.educative.io/courses/python-regular-expressions-with-data-scraping-projects/m2NwY5zJ4xE
from re import match

# Setting variable correct to False by default.
correct = True

# This basically calls the 'uloha' function with n=7.
# Variable is_automation is not used anywhere in this code, so I assume this is used by lector who verifies those scripts.
is_automaton, reg = uloha(7)

# This whole condition is checking whether is_automation is True.
# If so, it prints a sentence and sets variable testy to False.
# Both variables is_automation and testy are not used in this code, so I assume this is used by lector who verifies those scripts.
if is_automaton:
    print("Na toto sú len skryté testy pri odovzdaní")
    testy = False
# If is_automation is False (I would assume this is false by default), starts normal validation.
else:
    # Starting for loop with 100 iterations.
    for i in range(100):
        # Using match() function to check whether result returned from 'uloha' function (variable reg) is correctly finding binary number divisable by 7.
        # Variable 'reg' contains the regex expression, code bin(i * 7)[2:].
        # First iteration of this loop will test number 700 in binary (1010111100).
        # Since we are multiplying by 7, result numbers are allways divisible by 7 as well.
        # This test will work only if n=7, and will test 100 example binary numbers.
        if not match(reg, bin(i * 7)[2:]):
            # Prints message only if it finds some binary that is divisible by 7, but our regex from uloha() will not find it.
            print("Chyba, false positive pre hodnotu: ", bin(i * 7))
            # Sets variable correct to False (this will make the last condition on this script fail).
            correct = False
            # Break means we want to jump out of current loop. 
            # Since we already found at least 1 binary that is not matched by our regex, we can consider the regex as failed and end current loop.
            break

    # Starting for loop with 100 iterations.
    for i in range(100):
        # Using match() function to check whether result returned from 'uloha' function (variable reg) is correctly finding binary number NOT divisable by 7.
        # Variable 'reg' contains the regex expression, code bin(i * 7 + 3)[2:].
        # First iteration of this loop will test number 703 in binary (1010111111).
        # Since we are multiplying by 7 and adding extre 3, result numbers are never divisible by 7.
        # This test will work only if n=7, and will test 100 example binary numbers.
        if match(reg, bin(i * 7 + 3)[2:]):
            # Prints message only if it finds some binary that is NOT divisible by 7, but our regex from uloha() finds it.
            print("Chyba, false negative pre hodnotu: ", bin(i * 7 + 3))
            # Sets variable correct to False (this will make the last condition on this script fail).
            correct = False
            # Break means we want to jump out of current loop. 
            # Since we already found at least 1 binary that is not matched by our regex, we can consider the regex as failed and end current loop.
            break

# Last condition, depends on the above 2 for loops, if any problem was found in above loops, variable correct will be set to False and this condition will not match.
# If no issues were found during above 2 for loop runs, this will be True and final message is printed.
if correct:
    print("Zadanie spĺňa základné testy")
