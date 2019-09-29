import pandas as pnd
import numpy as np
from datetime import *
from statistics import mode
import time

CITY_DATA = { 'new york city': 'new_york_city.csv',
              'chicago': 'chicago.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
def get_city():
    city = ''
    while city.lower() not in ['new york city', 'chicago', 'washington', 'new york']:
        city = input('\nHey there! Let\'s explore some US bikeshare data from NYC, Chicago or Washington!\n'
                     'Which city would you like to see data from? You can choose from either New York City, Chicago, or Washington?\n')
        if city.lower() == 'new york city':
            return  'new_york_city.csv'
        elif city.lower() == 'new york':
            return  'new_york_city.csv'
        elif city.lower() == 'chicago':
            return  'chicago.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Whoops, I couldn\'t seem to find the city you were looking for. Please enter New York City, Chicago'
                  'or Washington to continue...')

def get_time_frame():
# User needs to decide how to filter the data (Month, Day, Both or not at all)
    time_frame = ''
    while time_frame.lower() not in ['month', 'day', 'none']:
        time_frame = input('\nHow would you like to filter the data? Please type'
                       ' Month, day - or None for no filtering.\n')
        if time_frame.lower() not in ['month', 'day', 'none']:
            print('I couldn\'t seem to understand your input, could you try again'
                  'and please type Month, day or None.\n')
    return time_frame

    # TO DO: get user input for month (all, january, february, ... , june)
def get_month():
    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    # Create a dictionary for easier handling of later return function
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nPlease type in a month from January until June that you\'d like to take a look at!\n')
        if month_input.lower() not in months_dict.keys():
            print('\nSorry, I couldn\'t understand the month you typed. Please pick a month between January and June and type the full word.\n')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_day_om():
    start_time = time.time()

    this_month = get_month()[0]
    month = int(this_month[5:])
    valid_date = True
    while valid_date:
        day = int(input('\nWhich day should we have a closer look at? Please provide your answer as a whole number (integer)!\n'))
        try:
            start_date = datetime(2017, month, day)
            valid_date = False
        except Exception as e:
            print(e)
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
def common_month(df):
    start_time = time.time()

    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['Start Time'].dt.month.mode())
    most_common_month = months[index - 1]
    print('\nOverall the most common month turns out to be {}.\n'.format(most_common_month))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: display the most common day of week
def common_day(df):
    start_time = time.time()

    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = int(df['Start Time'].dt.weekday.mode())
    most_common_day = week_days[index]
    print('\nOverall the most common day of the week turns out to be {}.\n'.format(most_common_day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: display the most common start hour
def common_hour(df):
    start_time = time.time()

    most_common_hour = int(df['Start Time'].dt.hour.mode())
    print("\nOverall the most common start hour turns out to be {} o'clock.\n".format(most_common_hour))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
def common_start_station(df):
    print('Calculating the most common stations and Trips...\n')
    start_time = time.time()

    common_start = df['Start Station'].mode().to_string(index= False)
    print('\nThe most common Start Station would be {}.\n'.format(common_start))

    # TO DO: display most commonly used end station
def common_end_station(df):
    common_end = df['End Station'].mode().to_string(index= False)
    print('\nThe most common End Station would be {}.\n'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
def common_trip(df):
    most_common_trip = df['trip'].mode().to_string(index = False)
    print('\nThe most common trip would be {}.\n'.format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    def trip_duration(df):
        total_tripduration = df['trip_duration'].sum()
        minutes, seconds = divmod(total_tripduration,60)
        hour,minutes = divmod(minutes, 60)
        print('\nOverall the total trip duration is {} Hour(s), {} minute(s) and {} second(s).\n'.format(hours, minutes, seconds))


    # TO DO: display mean travel time
    def average_duration(df):
        average_tripduration = round(df['Trip Duration'].mean())
        minutes, seconds = divmod(average_duration,60)
        if minutes > 60:
            hours,minutes = divmod(minutes,60)
            print('\nOverall the mean travel time for a trip is {} hour(s){} minute(s) and {} second(s).'.format(hours, minutes, seconds))
        else:
            print('\nOverall the average mean travel time for a trip is {} minute(s) and {} second(s).'.format(minutes, seconds))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
def user_type(df):
    start_time = time.time()

    subscr = df.query('user_type == "Subscriber"').user_type.count()
    custom = df.query('user_type == "Customer"').user_type.count()
    print('\nOverall there are {} Subscribers and {} Customers.\n'.format(subscr, custom))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display counts of gender
def gender_type(df):
    start_time = time.time()

    try:
        male = df.query('gender_type == "Male"').gender.count()
        female = df.query('gender_type == "Female"').gender.count()
        print('\nOverall there are {} users that are male and {} users that are female.\n'.format(male,female))
    except:
        print('There seems to be no gender data in this particular object.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display earliest, most recent, and most common year of birth
def birth_years(df):
    start_time = time.time()
    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode())
        print('\nIn this query the oldest user was born in {} while the youngest was born in {}.'
              ' The most common birthyear is {}.\n'.format(earliest, most_recent,most_common))
    except:
        print('There seems to be no birth year-data in this particular object.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Let the user see five lines of raw data
def display_dataset(df):

    def is_valid(display):
        if display.lower() == 'yes' or display.lower() == 'no':
            return True
        else:
            return False
    start = 0
    end = 5
    counter = True
    while counter:
        display = input('\nDo you want to see the data of individual trips? Type Yes or No to continue.\n')
        counter = is_valid(display)
        if counter:
            break
        else:
            print('\nExcuse me, I didn\'t understand your input. Please only type Yes or No.\n')
    if display.lower() == 'yes':
        print(df[df.columns[0:]].iloc[start:end])

def main():
    # City filter
    city = get_city()
    print('\nWait a second while data is loading...')
    df = pnd.read_csv(city,parse_dates = ['Start Time', 'End Time'])

    # New Trip column, where we can combine common start and end stations
    df['trip'] = df['Start Station'].str.cat(df['End Station'],sep=' to ')

    # Time filter (day, month, none)
    time_frame = get_time_frame()
    if time_frame == 'none':
        df_filtered = df
    elif time_frame == 'month' or time_frame == 'day':
        if time_frame == 'month':
            filter_lower, filter_upper = get_month()
        elif time_frame == 'day':
            filter_lower, filter_upper = get_day_om()
        df_filtered = df[(df['Start Time'] >= filter_lower) & (df['Start Time'] < filter_upper)]

    if time_frame == 'none' or time_frame == 'month':
        common_day(df_filtered)

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender_type(df_filtered)

        birth_years(df_filtered)

    display_dataset(df_filtered)

    restarting = input('\nWould you like to restart and try a different time frame or city? Then please type Yes - Type No to Exit.\n')
    while restarting.lower() not in ['yes', 'no']:
        print('I couldn\'t understand you. Do you wish to continue? Yes or No?\n')
        restarting = input('\nWould you like to restart and try a different time frame or city? Then please type Yes - Type No to Exit.\n')
    if restarting.lower() == 'yes':
        main()

if __name__ == "__main__":
    main()
