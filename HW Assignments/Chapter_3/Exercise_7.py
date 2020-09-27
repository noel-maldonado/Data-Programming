#(Random character) Write a program that displays a random uppercase letter
#using the time.time() function.
import time

currentTime = int(time.time())
randomCharacter = chr(ord('A') + currentTime % (ord('Z') - ord('A') + 1))
print(randomCharacter)