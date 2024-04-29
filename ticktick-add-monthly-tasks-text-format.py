'''
count = 0
month = 4
date_start = 1
date_end = 30
for date in range(date_start,date_end+1):
    print(f"{date:02d}{month:02d} {month}-{date}")
    count += 1
    if count == 7:
        count = 0
        print()

0=
1=
2=

'''
import datetime

def print_dates():
    # Get current date
    today = datetime.date.today()
    # Get the start of the current week (Monday)
    start_of_week = today - datetime.timedelta(days=today.weekday())
    weeks_to_print = 10
    # Print dates in batches of 7 days per week
    for i in range(weeks_to_print):
        week_dates = [start_of_week + datetime.timedelta(days=j)for j in range(i*7, (i+1)*7)]
        #print(f"Week {i+1}:")
        for date in week_dates:
            # Extract day and month
            day = date.day
            month = date.month
            # Print date in the specified format
            print(f"{day:02d}{month:02d} {month:02d}-{day:02d}")
        print("\n")

if __name__ == "__main__":
    print_dates()
