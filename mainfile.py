
definitions = {"een":"a",
               "twee":"b",
               "drie":"c",
               "vier":"d"}

items = []
for i in definitions:          #a list with only the items, so that they can be indexed and called
    items.append(i)

temp = items[::]               #creating a temporal storage so the list can be alterd for the next round without intervering with the current round
while True:       
    items = temp[::]        
    for i in items:         
        print(i)
        answer = input("definition : ")
        if answer == definitions[i]:
            print("correct")
            temp.remove(i)     #if answerd correctly, it wil be removed from the temporal storage used for the next round
        else:
            print('incorrect, the right definition was {0}'.format(definitions[i]))
        print("")
    
    if len(temp) == 0:         #checking if al words have been correctly answerd, else continue to the next round
        break
    else:
        print("next round :") 
        print("")

print("good job!")
exit()
