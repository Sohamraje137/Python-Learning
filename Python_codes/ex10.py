import random

def randwalk(n):
	x,y=0,0
	for i in range(n):
		(dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)])
		x+=dx
		y+=dy
	return (x,y)

number=70000

for walk_length in range(1,31):
	no_transport=0
	for i in range(number):
		(x,y)=randwalk(walk_length)
		distance= abs(x)+abs(y)
		if distance<=4:
			no_transport+=1
	no_transport_percent= 100*(no_transport /number)

	print("Walk size = ", walk_length, "/% of no transport = ",no_transport_percent)