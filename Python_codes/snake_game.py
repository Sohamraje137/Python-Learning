import random
import curses

s = curses.initscr()
curses.start_color()

curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)
#w.box(100,100)
w.border("|","|","-","-")

score=0
#w.bgcolor("white")
snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
curses.init_color(0, 224, 224, 224)
food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
w.addch(snake[0][0], snake[0][1], curses.ACS_BLOCK)
# s.getcsh()
print(sh)
print(sw)

while True:
    w.border(0)
    w.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
    w.addstr(0, 27, ' SNAKE GAME ')                                   # 'SNAKE' strings
    w.addstr(0, 50, 'Soham ') 
    w.timeout(50 - (len(snake)//3)%120)          # Increases the speed of Snake as its length increases
    
    next_key = w.getch()
    if next_key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
        next_key = -1                                                   # one (Pause/Resume)
        while next_key != ord(' '):
            next_key = w.getch()
        next_key = key
        continue
    if next_key not in [curses.KEY_LEFT, curses.KEY_RIGHT,curses.KEY_UP, curses.KEY_DOWN]:     # If an invalid key is pressed
        next_key = key
    if key == curses.KEY_DOWN and next_key==curses.KEY_UP :
        curses.beep()
        key=key
    elif key == curses.KEY_UP and next_key==curses.KEY_DOWN :
        curses.beep()
        key=key
    elif key == curses.KEY_RIGHT and next_key==curses.KEY_LEFT :
        curses.beep()
        key=key
    elif key == curses.KEY_LEFT and next_key==curses.KEY_RIGHT :
        curses.beep()
        key=key
    elif (next_key == -1 or next_key==key) :
        key = key 
    else :
     key= next_key

    if snake[0] in snake[1:]:
        curses.beep()
        curses.endwin()
        break
    else:
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0][0] == 0: snake[0][0] = sh-2
        if snake[0][1] == 0: snake[0][1] = sw-2
        if snake[0][0] == sh-1: snake[0][0] = 1
        if snake[0][1] == sw-1: snake[0][1] = 1

        if snake[0] == food:
            curses.flash()
            food = None
            score+=1;
            while food is None:
                nf = [
                    random.randint(1, sh-2),
                    random.randint(1, sw-2)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')
        
        w.addch(snake[0][0], snake[0][1], curses.ACS_BLOCK)
# s.refresh()
# print(sh)
# print(sw)
print("Your score is :" +str(score))
