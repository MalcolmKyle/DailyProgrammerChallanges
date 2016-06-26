from operator import itemgetter
import sys
#Malcolm McCullum created for r/dailyprogrammer
# 6_25_2015
#Scrabble is a popular word game where players remove tiles with letters on them from a bag and use them to create words on a board. The total number of tiles as well as the frequency of each letter does not change between games.
#The tiles already in play are inputted as an uppercase string. For example, if 14 tiles have been removed from the bag and are in play, you would be given an input like this:
#AEERTYOXMCNB_S
#You should output the tiles that are left in the bag. The list should be in descending order of the quantity of each tile left in the bag, skipping over amounts that have no tiles.
#In cases where more than one letter has the same quantity remaining, output those letters in alphabetical order, with blank tiles at the end.
#10: E
#9: I
#8: A
#7: O
#5: N, R, T
#4: D, L, U
#3: G, S
#2: F, H, P, V, W
#1: B, C, J, K, M, Q, Y, Z, _
#0: X
#Source: https://www.reddit.com/r/dailyprogrammer/comments/4oylbo/20160620_challenge_272_easy_whats_in_the_bag/

letterBag = {'A':9, 'B':2,'C':2,'D':4,'E':12,'F':2,'G':3,'H':2,'I':9,'J':1,'K':1,
           'L':4,'M':2,'N':6,'O':8,'P':2,'Q':1,'R':6,'S':4,'T':6,'U':4,'V':2,'W':2,
           'X':1,'Y':2,'Z':1,'_':2}
lettersInPlay = input("Enter letters already in play: ")
index = 0
while index < len(lettersInPlay):
    key = lettersInPlay[index]
    #print("key: "+key)
    if key in letterBag:
        #print("key found in letter bag")
        if letterBag[key] > 0:
            letterBag[key] -=1
        else:
            print("ERROR: More "+key+"'s have been taken from the bag than possible")
            sys.exit()
    else:
        print("ERROR: not a valid input: "+key)
        sys.exit()
    index+=1
            
sortedBag = sorted(letterBag.items(), key=itemgetter(1), reverse=True)
# sort the list of items by the value instead of the key

for key,value in sortedBag:
    print(value,key)
