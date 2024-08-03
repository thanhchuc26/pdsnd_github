import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """Asks user to specify a city, month, and day to analyze."""
    print('Hello! Let\'s explore some US bike share data!')
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter Chicago, New York City, or Washington.")
            # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? (all, january, february, ... , june)\n").lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print("Invalid input. Please enter a valid month or 'all'.")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of week? (all, monday, tuesday, ... sunday)\n").lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print("Invalid input. Please enter a valid day or 'all'.")
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable."""
    try:
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError:
        print(f"File '{CITY_DATA[city]}' not found.")
        return None

    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month.title()]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    month_name = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"}
    print("Most Common Month:", common_month)

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("Most Common Day of Week:", common_day)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_start_hour = df["hour"].mode()[0]
    print("Most Common Start Hour:", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("Most Commonly Used Start Station:", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("Most Commonly Used End Station:", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["trip"] = df["Start Station"] + " to " + df["End Station"]
    common_trip = df["trip"].mode()[0]
    print("Most Frequent Combination of Start Station and End Station Trip:", common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total Travel Time:", total_travel_time, "seconds")

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean Travel Time:", mean_travel_time, "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("User Types:\n", user_types)

    # TO DO: Display counts of gender
    if "Gender" in df:
        gender_counts = df["Gender"].value_counts()
        print("\nGender Counts:\n", gender_counts)
    else:
        print("\nGender data not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_birth_year = df["Birth Year"].min()
        recent_birth_year = df["Birth Year"].max()
        common_birth_year = df["Birth Year"].mode()[0]
        print("\nEarliest Year of Birth:", int(earliest_birth_year))
        print("Most Recent Year of Birth:", int(recent_birth_year))
        print("Most Common Year of Birth:", int(common_birth_year))
    else:
        print("\nBirth year data not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


#TO DO: Display raw data in chunks of 5 rows
def display_raw_data(df):
    row_start = 0
    while True:
        show_data = input("Do you want to check the first 5 rows of the dataset? (yes/no)\n").lower()
        if show_data == 'yes':
            print(df.iloc[row_start : row_start + 5]) #Display the next 5 rows
            row_start += 5
            show_more = input("Do you want to check another 5 rows? (yes/no)\n").lower()
            if show_more != 'yes':
                break
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        if df is not None: #Check if data was loaded successfully
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
