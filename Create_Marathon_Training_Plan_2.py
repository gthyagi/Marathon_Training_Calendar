# ## Create Marathon Training Calendar
#
# *Author: [Thyagarajulu Gollapalli](https://github.com/gthyagi)*

from icalendar import Calendar, Event
from datetime import datetime, timedelta


# ### Count Weeks

def weeks_between_dates(start_date_str, end_date_str):
    # Convert date strings to datetime objects
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    # Calculate the difference in days
    delta_days = (end_date - start_date).days

    # Calculate the number of weeks
    weeks = (delta_days+1) // 7 # plus 1 to include start and end dates 

    return weeks


# +
# Example usage:
start_date_str = "2024-02-05" # "%Y-%m-%d"
end_date_str = "2024-05-19"

weeks = weeks_between_dates(start_date_str, end_date_str)

print(f"Weeks between {start_date_str} and {end_date_str}: {weeks} weeks")
# -

# ### Training Events Name
# Marathon plan source: [GTN](https://www.globaltrinetwork.com/)

# event name
event_name = [
              ['Easy Run', 'Easy Run', 'Easy Run', 'Intervals', 'Rest Day', 'Long Run', 'REST DAY'], # week1
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Rest Day', 'Long Run', 'REST DAY'], # week2
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week3
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week3_1
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week4
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week5
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week6
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week6_1
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week7
              ['Easy Run', 'Pyramid Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week8
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week9
              ['Easy Run', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Long Run', 'REST DAY'], # week9_1
              ['Time Trial', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Rest Day', 'REST DAY'], # week10
              ['Intervals', 'Intervals', 'Rest Day', 'Intervals', 'Rest Day', 'Easy Run', 'REST DAY'], # week11
              ['REST DAY', 'Intervals', 'Easy Run', 'Intervals', 'Easy Run', 'Rest Day', 'Marathon Day',], # week12
             ]

# ### Training Events Details

event_details = [
                 ['6km', '10km', '5km', '10km as 10x20s at 5-10km pace, 40s jog rec', '0km', '16km easy run', '0km'], # week1
                 ['6km', '12km as 5x(2min at MP, 90s rec)', '6km', '12km as 15x30s at 5-10km pace, 40s jog rec', '0km', '18km easy run', '0km'], # week2
                 ['6km', '12km as 3x(800m at MP, 90s rec / 2km at MP, 2min rec)', '6km', '12km as 10x50s at 5-10km pace, 50s jog rec', '6km', '22km easy run', '0km'], # week3
                 ['6km', '12km as 3x(800m at MP, 90s rec / 2km at MP, 2min rec)', '6km', '12km as 10x50s at 5-10km pace, 50s jog rec', '6km', '22km easy run', '0km'], # week3_1
                 ['6km', '12km as 3x(1km at MP, 90s rec / 2km at MP, 2min rec)', '6km', '14km as 15x200m at 10km pace, 45secs rec', '6km', '26km easy run', '0km'], # week4
                 ['6km', '12km as 5x(1.2km at MP, 90s rec)', '8km', '15km as 12x300m at 10km pace, 60s rec', '6km', '28km easy run', '0km'], # week5
                 ['6km', '14km as 4 x (800m at MP, 75s rec / 1600m at MP, 100s rec)', '8km', '12km as 10 x 200m at 10km pace, 55s jog rec', '8km', '30km easy run', '0km'], # week6
                 ['6km', '14km as 4 x (800m at MP, 75s rec / 1600m at MP, 100s rec)', '8km', '12km as 10 x 200m at 10km pace, 55s jog rec', '8km', '30km easy run', '0km'], # week6_1
                 ['6km', '15km as 4 x (1km at MP, 75sec rec / 2km at MP, 100sec rec)', '10km', '12km as 10x55secs at 10km pace, 60s rec', '10km', '30km as 10km easy, 8km at MP+40s/km, 6km at MP+20s/km, 4km at MP+10-15s/km, 2km rec', '0km'], # week7
                 ['6km', '15km as 400-800-400-1000-400-1200-400-1000-400-800-400 at MP (60-80sec rec)', '9km', '14km as 15x200m at 10km pace, 55secs jog rec', '9km', '34km as 12km easy, 8km at MP+40s/km, 6km at MP+20-30s/km, 4km at MP+10-15s/km, Remainder easy', '0km'], # week8
                 ['6km', '12km as 4x(5x300m at 10km pace, 50s rec) with 2min rec between sets', '8km', '15km as 6x800m at MP, 90s rec', '8km', '26-28km as 10km easy, 8km at MP+30-40s/km, 6km at MP+10-15s/km, 2km at MP+5-10s/km', '0km'], # week9
                 ['6km', '12km as 4x(5x300m at 10km pace, 50s rec) with 2min rec between sets', '8km', '15km as 6x800m at MP, 90s rec', '8km', '26-28km as 10km easy, 8km at MP+30-40s/km, 6km at MP+10-15s/km, 2km at MP+5-10s/km', '0km'], # week9_1
                 ['15km with 1.4km MP, 90s rec / 3km MP, 2min rec / 1.2km MP, 90s rec / 3km MP, 2min rec / 1km MP', '10km', '12km with 10x300m at 10km pace, 100m jog recoveries', '6km', 'Good warm-up, followed by an 8km TT. Aiming for Target Marathon Pace, or just faster', '0km', '0km'], # week10
                 ['12km with 3x(3x400m at 10km pace, 60s rec)', '0km', '9km with 4x800m at Target Marathon Pace (or a little quicker), 2min jog recoveries', '0km', '10km with 12x200m at 10km pace, 50s recovery', '14km easy run', '0km'], # week11
                 ['0km', '8km with 8x300m at 10km pace, 100m recovery jog between', '5km', '8km with 8x200m at Target Marathon Pace, 200-400m jog recoveries', '3km', '0km', 'Marathon Day'], # week12
                ]


def flatten(xss):
    # function to flatten list of lists
    return [x for xs in xss for x in xs]


def create_ical_events(summary, start_date, end_date, location=None, description=None, _categories="Marathon_May_2024"):
    cal = Calendar()

    count = 0
    current_date = start_date
    while current_date <= end_date:
        # Create an Event for each day
        event = Event()
        event.add('summary', summary[count])
        event.add('dtstart', current_date)
        event.add('dtend', current_date + timedelta(hours=2))  # Assuming events last for 1 hour
        event.add('categories', _categories)

        if location:
            event.add('location', location)

        if description:
            event.add('description', description[count])

        cal.add_component(event)

        # Move to the next day
        current_date += timedelta(days=1)
        count += 1

    return cal.to_ical()


# +
# Example usage
start_date = datetime(2024, 2, 5, 18, 0)
end_date = datetime(2024, 5, 19, 20, 0)
location = "Clayton"

ical_data = create_ical_events(flatten(event_name), start_date, end_date, location, flatten(event_details))

# Save to a file (optional)
with open('Marathon_May_2024.ics', 'wb') as f:
    f.write(ical_data)
# -


