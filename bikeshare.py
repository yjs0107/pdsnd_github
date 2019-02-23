import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def city_input():
        while True:
            city = input('Please type in one of the cities: Chicago, New York City, Washington\n').lower()
            if city in (CITY_DATA.keys()):
                return city
            else:
                print('You have entered wrong city please enter one of the following cities: Chicago, New York, Washington')
    # TO DO: get user input for month (all, january, february, ... , june)
    def month_input():
        while True:
            month = input('Please choose a month between january and june or all\n').lower()
            if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
                return month
            else:
                print('Please type in valid month from the list')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    def day_input():
        while True:
            day = input('Please choose  a day between monday to sunday or all\n').lower()
            if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturady', 'sunday'):
                return day
            else:
                 print('Please type in valid day from the list')
    print('-'*40)
    city = city_input()
    month = month_input()
    day = day_input()
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = months[month-1]
    print('most common month: {}'.format(common_month))

    # TO DO: display the most common day of week
    def common_day(df):
        day = df['day_of_week'].mode()[0]
        return(day)
    day = common_day(df)
    print('most common day: ' + day)

    # TO DO: display the most common start hour
    def common_hour(df):
        df['hour'] = df['Start Time'].dt.hour
        hour = df['hour'].mode()[0]
        return(hour)
    hour = common_hour(df)
    print('most common hour: ' + str(hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    def common_start_station(df):
        start_station = df['Start Station'].mode()[0]
        return(start_station)
    start_station = common_start_station(df)
    print('most common start station:{}'.format(start_station))

    # TO DO: display most commonly used end station
    def common_end_station(df):
        end_station = df['End Station'].mode()[0]
        return(end_station)
    end_station = common_end_station(df)
    print('most common end station: {}'.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    def frequent_combination(df):
        df['Combination'] = df['Start Station'] + " " + df['End Station']
        frequent_combination = df['Combination'].mode()[0]
        return(frequent_combination)
    frequent_station = frequent_combination(df)
    print('most frequent combination: ' + frequent_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    def total_traveltime(df):
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['Travel Time'] = df['End Time'] - df['Start Time']
        total_traveltime = df['Travel Time'].sum()
        return(total_traveltime)
    total_traveltime = total_traveltime(df)
    print('Total Travel Time: ' + str(total_traveltime))


    # TO DO: display mean travel time
    def mean_traveltime(df):
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['Travel Time'] = df['End Time'] - df['Start Time']
        mean_traveltime = df['Travel Time'].mean()
        return(mean_traveltime)
    mean_traveltime = mean_traveltime(df)
    print('Mean Travel Time: ' + str(mean_traveltime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    def user_types():
        return df['User Type'].value_counts()
    user_types = user_types()
    print(user_types)
    # TO DO: Display counts of gender
    try:
        def gender_count():
            return df['Gender'].value_counts()
        gender_count = gender_count()
        print(gender_count)
    except:
        print('Washington does not have gender count available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        mostrecent_yearofbirth = df['Birth Year'].max()
        mostcommon_yearofbirth = df['Birth Year'].mode()[0]
        earliest_yearofbirth = df['Birth Year'].min()
        print('Earliest Year of Birth: ' + str(earliest_yearofbirth))
        print('Most Recent Year of Birth: ' + str(mostrecent_yearofbirth))
        print('Most Common Year of Birth: ' + str(mostcommon_yearofbirth))
    except:
        print('Washington does not have birth year available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    def display_rawdata():
        i = 5
        while True:
            raw_data = input('Would you like to see the raw data? Select Yes or No\n').lower()
            if (raw_data == 'yes'):
                print(df.iloc[i], '\n')
                i += 5
                continue
            elif (raw_data == 'no'):
                break
    display = display_rawdata()
    print(display)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
