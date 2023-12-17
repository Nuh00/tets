import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the word type game!")
    stdscr.addstr("\nPress any key to start...")                                                
    stdscr.refresh()
    stdscr.getkey()



def overlay_text(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM: {wpm}", curses.color_pair(3))                                             


    for i, char in enumerate(current):
        if char != target[i]:
            stdscr.addstr(0, i, char, curses.color_pair(2))
        else:
            stdscr.addstr(0, i, char, curses.color_pair(1))
 
        
def word_gen():
    with open("text.txt") as f:
        words = f.readlines()
        return random.choice(words).strip()


def wpm_test(stdscr):

    target_text = word_gen()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

                  


    while True:
        current_time = max(time.time() - start_time, 1)
        stdscr.clear()
        overlay_text(stdscr, target_text, current_text, wpm)
        wpm = round((len(current_text)  / (current_time / 60)) / 5)

        stdscr.refresh()
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            time.sleep(0.1)
            continue

        
        if key== '\x1b':
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)












        












def main(stdscr):
    # these vvv are a way to create different color themes 
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0, "Game Over, press any key to play again...")
        key = stdscr.getkey()
        if key != '\x1b':
            wpm_test(stdscr)
        else:
            break


wrapper(main)
