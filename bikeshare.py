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
    while True: 
        city = input('Would you like to see data for Chicago, New York City or Washington?\n ').lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington': break
        print(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month = input("Select the month you would like to filter by: January, February, March, April, May, June or type all for no filter.\n ").lower()
        if month == 'all' or month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june': break
        print(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("If you would like to see data for a particular day of the week please specify below (eg. Monday, Tuesday... etc.) or use all for no filter.\n ").lower()
        if day == 'all' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday': break
        print(day)

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
   
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+ 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    print('The most common month: ', months[popular_month])
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of the week: ', popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular start hour: ', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts()
    print('Most commonly used start station: ', start_station.index[0], ' Count: ', start_station[0])

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts()
    print('Most commonly used end station: ', end_station.index[0], ' Count: ', end_station[0])

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = ('Start station: ' + df['Start Station'] +', End station: '+ df['End Station']).value_counts()
    print('Most frequent combination: ', combination_start_end.index[0], ' Count: ', combination_start_end[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time/3600, 'hours')
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time/60, 'min')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nWhat is the breakdown of users?')
    while True:
        try:
            user_types = df['User Type'].value_counts()
            print(user_types)
            break
        except:
            print('Data not avaliable')
            break
            
    # TO DO: Display counts of gender
    print('\nWhat is the breakdown of gender?')
    while True:
        try: 
            gender = df['Gender'].value_counts()
            print(gender)
            break
        except:
            print('Data not avaliable')
            break

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nYear of birth stats')
    
    while True:
        try:
            earliest_year = df['Birth Year'].min()
            recent_year = df['Birth Year'].max()
            most_com_year = df['Birth Year'].mode()[0]
            print('Earliest year of birth: ', int(earliest_year))
            print('Most recent year of birth: ', int(recent_year))
            print('Most common year of birth: ', int(most_com_year))
            break
        except:
            print('Data not avaliable')
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input('Would you like to see individual trip data? Enter yes or no.\n')
        start_loc = 0
        end_loc = 5
      
        while raw_data == 'yes':
            print(df.iloc[start_loc:end_loc])
            raw_data = input("Would you like to continue? Enter yes or no.\n").lower()
            start_loc += 5    
            end_loc += 5 
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
