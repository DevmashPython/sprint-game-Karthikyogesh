import msvcrt
import time
finish=10
count=0
n=0
print "press enter key to get started"
raw_input()
s_time=time.time()
while(1):
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		print "-->",
		if count==finish:
			break
	else:
		print "GAME OVER,TRY AGAIN"
		raw_input("Press enter to close")
		quit()
print "MOVE DOWN"
finish=10
count=0		
while(1):
	key=msvcrt.getch()
	if key=='s':
		count=count+1
		print "\t\t\t\t\t|"
		if count==finish:
			break
	else:
		print "GAME OVER,TRY AGAIN"
		raw_input("Press enter to close")
		quit()
print "\t\t\tMOVE RIGHT",			
finish=10
count=0
while(1):
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		if n==0:
			print "\t ",
			n=1
		print "-->",
		if count==finish:
			time_elapsed=time.time()-s_time
			print ""
			print "\nTIME TAKEN IS %s"%str(time_elapsed)
			raw_input("Press enter to close")
			break	
	else:
		print "GAME OVER,TRY AGAIN"	
		raw_input("Press enter to close")
		quit()
	
'''
1. Mention controls for the game.

'''
