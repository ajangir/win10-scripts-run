import argparse
import random
import time

import pyautogui
import datetime

START_WEEK_NO=39
PRESS_COUNT = 0

def write(text):
    print(text)
    pyautogui.write(text)
    time.sleep(1)
def press(key,presses=1):
    global PRESS_COUNT
    PRESS_COUNT += 1
    if PRESS_COUNT > 5:
        scroll_mouse_randomly()
        time.sleep(5)
        PRESS_COUNT = 0
    
    for _ in range(presses):
      pyautogui.press(key)
      time.sleep(2)
  
def get_week_number_and_days(year, week_number):
    # Get the first day of the week
    first_day_of_week = datetime.date.fromisocalendar(year, week_number, 1)
    # Calculate the other days in the week
    week_days = [first_day_of_week + datetime.timedelta(days=i) for i in range(7)]
    return week_days


def simulate_keystrokes(year,week_number=START_WEEK_NO):
    #print(week_string)
    week_days = get_week_number_and_days(year,week_number)
    start_date = week_days[0]
    end_date = week_days[-1]

    # Go key up * weeks_to_print
    start_date_str = f"{start_date.day:02d}{start_date.month:02d}"
    end_date_str = f"{end_date.day:02d}{end_date.month:02d}"
    week_string = f"24{week_number}={start_date_str}-{end_date_str}"

    write(week_string)
    # Press shift+enter and print week numbers
    pyautogui.hotkey('shift', 'enter');time.sleep(1)
    
    for day in week_days:
      week_number_str = f"{day.day:02d}{day.month:02d} {day.month}-{day.day}"
      write(week_number_str)
      press('enter')
      if day != week_days[-1]:
          press('enter')
      
    #press('up',presses=len(week_days)-1)
    time.sleep(3)
    #press('end')
      # For each day, press shift+enter and print 0=, 1=, 2=
    for day in week_days:
      pyautogui.hotkey('shift', 'enter')
      time.sleep(1)
      str1 = f"0= {day.month}-{day.day} 06:00-12:00"
      str2 = f"1= {day.month}-{day.day} 12:00-18:00"
      str3 = f"2= {day.month}-{day.day} 18:00-23:00"
      write(str1)
      press('enter');press('enter')
      write(str2)
      press('enter');press('enter')
      write(str3)
      press('enter')
      press('down')
      #press('end')
      
      #press('down')
      #press('end')
def scroll_mouse_randomly():
    #screen_width, screen_height = pyautogui.size()
    SCROLL_LINES = 5  # Number of lines to scroll
    scroll_amount = random.choice([SCROLL_LINES, -SCROLL_LINES])
    pyautogui.scroll(scroll_amount)
    time.sleep(1)

def main():
    # Generate week strings
    year = datetime.date.today().year
    
    time.sleep(5.0)
    # Simulate keystrokes
    simulate_keystrokes(year)
    

if __name__ == "__main__":
    main()
