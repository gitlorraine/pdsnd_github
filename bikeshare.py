import time
import pandas as pd
import numpy as np



 # these are the cities and corresponding city data files 
 # processed by this program
  

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' } 



def get_filters():
        
    """   
        Args:
            none for input
        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        
           Module takes no input and prompts user to enter City, Month, and Day 
           Module validates city, month, and day and returns them validated.
           City must be entered.
           Month and day do not have to be entered.  If month is not entered,
           'all' will be returned in month. If day is not entered, 'all' will 
           be returned in day.
           """
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    days   = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    
    print('Hello! Let\'s explore some US bikeshare data!')

    city_is_not_validated = True

    while city_is_not_validated:
        input_city = (input("Would you like to explore Chicago, New York City or Washington:"))
        lower_city = input_city.lower()
        if lower_city in CITY_DATA:
            city = lower_city
            city_is_not_validated = False
        elif lower_city == 'c':
            city = 'chicago'
            city_is_not_validated = False
        elif lower_city == 'w':
            city = 'washington'
            city_is_not_validated = False 
        elif lower_city == 'n':
            city = 'new york city'
            city_is_not_validated = False 
        elif lower_city == 'ny':
            city = 'new york city'
            city_is_not_validated = False 
        elif lower_city == 'n y':
            city = 'new york city'
            city_is_not_validated = False         
        else:
            city_is_not_validated = True
            print('The city you entered is not valid, please enter a valid city')
            print('bad city=', input_city)
    
   
    print('You can filter data by month, by day, by both, or by neither (in addition to City)')

    month_filter_is_not_validated = True

    while month_filter_is_not_validated:
        input_filter_month_Y_N = (input("Would you like to filter data by month, Yes or No:"))
        lower_filter_month_Y_N = input_filter_month_Y_N.lower()
        if lower_filter_month_Y_N == 'yes': 
            filter_by_month = True
            month_filter_is_not_validated = False
        elif lower_filter_month_Y_N == 'y': 
            filter_by_month = True
            month_filter_is_not_validated = False    
        elif lower_filter_month_Y_N == 'no': 
            filter_by_month = False
            month_filter_is_not_validated = False
        elif lower_filter_month_Y_N == 'n': 
            filter_by_month = False
            month_filter_is_not_validated = False    
        else:
            filter_by_month = False
            month_filter_is_not_validated = True
            print('Your response was invalid, please enter either Yes or No')
            print('your invalid response was', input_filter_month_Y_N)
        
    if filter_by_month:
        month_is_not_validated = True
    else:    
        month_is_not_validated = False
        month = 'all'
    
    while month_is_not_validated:
        print('Valid months to filter on are: January, February, March, April, May or June')
        input_month = (input("Please enter a month to filter data on:"))
        lower_month = input_month.lower()
            
        if lower_month in months: 
            month_is_not_validated = False
            month = lower_month
        else:
            month_is_not_validated = True
            print('The month you entered was invalid, you entered:', input_month)
        
      
    day_filter_is_not_validated = True

    while day_filter_is_not_validated:
        input_filter_day_Y_N = (input("Would you like to filter data by day of the week, Yes or No:"))
        lower_filter_day_Y_N = input_filter_day_Y_N.lower()
        if lower_filter_day_Y_N == 'yes': 
            filter_by_day = True
            day_filter_is_not_validated = False
        elif lower_filter_day_Y_N == 'y': 
            filter_by_day = True
            day_filter_is_not_validated = False    
        elif lower_filter_day_Y_N == 'no': 
            filter_by_day = False
            day_filter_is_not_validated = False
        elif lower_filter_day_Y_N == 'n': 
            filter_by_day = False
            day_filter_is_not_validated = False    
        else:
            filter_by_day = False
            day_filter_is_not_validated = True
            print('Your response was invalid, please enter either Yes or No')
           
        
    if filter_by_day:
        day_is_not_validated = True
    else:    
        day_is_not_validated = False
        day = 'all'
    
    while day_is_not_validated:
        print('Valid days are: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday')
        input_day = (input("Please enter a day to filter data on:"))
        lower_day = input_day.lower()
           
        if lower_day in days: 
            day_is_not_validated = False
            day = lower_day
        else:
            day_is_not_validated = True
            print('The day entered was invalid, please enter a valid day')
           
    search_city = city
    
    return city, month, day


            
def load_data(city, month, day): 
                 
    """
   
        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        
            Loads data for the specified city and filters by month and day if applicable.
            creates additional columns as needed for later processing
    """
  
    # load data file into a dataframe for the given city file
    
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # create a new column 'Trip' (route taken) by
    # concatenating the 'Start Station' with the 'End Station
       
    df['Trip'] = df['Start Station'] + df['End Station']

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
    
    """
        Args:
        (df) file to be analyzed
        
        Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)


    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start Day of The Week:', popular_day)

    
    # display the most common start hour
    
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return


def station_stats(df):
    
    """
        Args:
        (df) file to be analyzed
        
        Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # display most popular 'Trip' (route)
    popular_trip = df['Trip'].mode()[0]
    print('The most popular trip is:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return


def trip_duration_stats(df):
    
    """
        Args:
        (df) file to be analyzed
        
        Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return



def user_stats(df, city):
    
    """
        Args:
        (df) file to be analyzed
        (city) city that data is being filtered on
               some user data is not available for Washington
               such as gender and birth year
        
        Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_types_count = df['User Type'].value_counts()
    print('counts of user types:', user_types_count)

    # Display counts of gender for Chicago and New York City
    # Gender data is not available for Washington
    if city == 'washington':
        print('Counts of each gender: NOT AVAILABLE for Washington')
    else:           
        gender_types_count = df['Gender'].value_counts()
        print('Counts of each gender:', gender_types_count)


    # Display earliest, most recent, and most common year of birth
    # for Chicago and New York City.  Birth statistics are not
    # available for Washington
    
    if city == 'washington':
        print('Earliest birth year: NOT AVAILABLE for Washington')
        print('Most recent birth year: NOT AVAILABLE for Washington')
        print('Most popular birth year: NOT AVAILABLE for Washington',)
    else:    
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest birth year:', earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print('Most recent birth year:', most_recent_birth_year)
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most popular birth year:', most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return


def display_rows(df):
        
    """   
        Args:
            (df) file to be displayed
        Returns:
            none
                    
           Module displays 5 rows at a time per continued user request
           
           This allows the user to scroll through raw data
           
           """
    sub1 = 0
    sub2 = 1
    sub3 = 2
    sub4 = 3
    sub5 = 4
    
    scrolling = True
          
    while scrolling:
        
        print('********************* first row of five being displayed ****************')
        print(df.iloc[sub1])
        print('********************* second row of five being displayed ***************')
        print(df.iloc[sub2])
        print('********************* third row of five being displayed ****************')
        print(df.iloc[sub3])
        print('********************* fourth row of five being displayed ***************')
        print(df.iloc[sub4])
        print('********************* fifth row of five being displayed ****************')
        print(df.iloc[sub5])
              
            
        scroll_more = input('\nWould you like to continue scrolling (5 rows at a time)?  Enter yes or no:\n')
       
        if scroll_more.lower() == 'yes':    
            
            scrolling = True
            sub1 += 5
            sub2 += 5
            sub3 += 5
            sub4 += 5
            sub5 += 5  

            print('Here are the next five rows of data:')
            
        elif scroll_more.lower() == 'y': 
            scrolling = True
            sub1 += 5
            sub2 += 5
            sub3 += 5
            sub4 += 5
            sub5 += 5  

            print('Here are the next five rows of data:')
        else:
            
            scrolling = False   
            
    
    return 



def main():

    while True:
        
         # get and validate user input for city, month (optional), and day(optional)  
        city, month, day =  get_filters()
         
        # read in and filter appropriate city data file, filter on month and day if 
        # specified and add a few new columns needed for later statistics
        df = load_data(city, month, day)
        
        # calculate and print time statistics 
        time_stats(df)
        
        # calculate and print station statistics 
        station_stats(df)
        
        # calculate and print trip statistics 
        trip_duration_stats(df)
        
        # calculate and print trip statistics
        # city is needed because gender and birth year are not 
        # available for Washington
        user_stats(df, city)
        
        # display rows of data, 5 rows at a time if the user wants
        # to see 'raw' data
        scroll = input('\nWould you like to view rows (5 at a time)?  Enter yes or no.\n')
        if scroll.lower() == 'yes':
            print('Here are the first five rows of data:')
            display_rows(df)
        elif scroll.lower() == 'y':
            print('Here are the first five rows of data:')
            display_rows(df)
              
        # allow the user to continue the program, enter another city, and get
        # additional statistics if they want to  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'yes':
            continue
        elif restart.lower() == 'y':
            continue
        else:
            break

                

if __name__ == "__main__":
    main()
