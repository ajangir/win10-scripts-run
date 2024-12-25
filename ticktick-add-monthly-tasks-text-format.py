'''
go to last done week
and run script and whenever one week is done
click on the last done week on left panel
'''
import random
import time

import pyautogui
import datetime

SINGLE_WEEK_NO=50
PRESS_COUNT = 0
PRESS_DELAY=1
WRITE_DELAY=1
HOTKEY_DELAY=2

def write(text):
    pyautogui.write(text)
    time.sleep(WRITE_DELAY)
    return

def press(key,presses=1):
    global PRESS_COUNT
    PRESS_COUNT += 1
    if PRESS_COUNT >= 10:
        scroll_mouse_randomly()
        time.sleep(PRESS_DELAY)
        PRESS_COUNT = 0
    
    for _ in range(presses):
      pyautogui.press(key)
      time.sleep(PRESS_DELAY)
    
    return
  
def get_week_number_and_days(year, week_number):
    # Get the first day of the week
    first_day_of_week = datetime.date.fromisocalendar(year, week_number, 1)
    # Calculate the other days in the week
    week_days = [first_day_of_week + datetime.timedelta(days=i) for i in range(7)]
    return week_days

def createNewWeekToGo():
    pyautogui.hotkey('shift','enter')
    time.sleep(HOTKEY_DELAY)
    press('up')
    pyautogui.click(1400, 260)

    
def simulate_keystrokes(year,week_number=SINGLE_WEEK_NO):
    
    week_days = get_week_number_and_days(year,week_number)
    start_date = week_days[0]
    end_date = week_days[-1]
    

    # Go key up * weeks_to_print
    start_date_str = f"{start_date.day:02d}{start_date.month:02d}"
    end_date_str = f"{end_date.day:02d}{end_date.month:02d}"
    week_string = f"24{week_number}={start_date_str}-{end_date_str}"
    
    write(week_string)
    #make task medium priroty
    pyautogui.hotkey('alt','3');time.sleep(1)
    createNewWeekToGo()
    # Press shift+enter and print week numbers
    time.sleep(1)

    for day in week_days:
      week_number_str = f"{day.day:02d}{day.month:02d} {day.month}-{day.day}"
      write(week_number_str)
      #make task low priroty
      pyautogui.hotkey('alt','2');time.sleep(1)
      press('enter')
      if day != week_days[-1]:
          press('enter')
    
    press('up',7)
    # For each day, press shift+enter and print 0=, 1=, 2=
    for day in week_days:
        pyautogui.hotkey('shift', 'enter')
        time.sleep(1)
        
        str1 = f"0= {day.month}-{day.day} 06:00-12:00"
        str2 = f"1= {day.month}-{day.day} 12:00-18:00"
        str3 = f"2= {day.month}-{day.day} 18:00-20:00"
        
        
        write(str1)
        press('enter');press('enter')
        write(str2)
        press('enter');press('enter')
        write(str3)
        press('enter')
        press('down')

    return

def scroll_mouse_randomly():
    #screen_width, screen_height = pyautogui.size()
    SCROLL_LINES = 20  # Number of lines to scroll
    MAX_SCROLL_DOWN = -999
    scroll_amount = random.choice([SCROLL_LINES, -SCROLL_LINES])
    pyautogui.scroll(scroll_amount)
    pyautogui.scroll(MAX_SCROLL_DOWN)
    time.sleep(1)
    return

def removeDateTask():
    for _ in range(3):
        pyautogui.hotkey('ctrl','0')
        time.sleep(2)
        press('down')
    return

#remove all task date from 0,1 and 2 task under daily tikcontroller
def removeDamage():
    time.sleep(5)
    for _ in range(7):
        press('down')
        removeDateTask()
    return

def main():
    # Generate week strings
    year = datetime.date.today().year
    year = 2025

    # Simulate keystrokes
    START_WEEK = 1
    END_WEEK = 10
    for i in range(START_WEEK,END_WEEK+1):
        time.sleep(5.0)
        press('enter')
        simulate_keystrokes(year,i)
    return
    

if __name__ == "__main__":
    main()
    #removeDamage()
#1400, 260