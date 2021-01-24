# -*- coding: utf-8 -*-
"""
Created on Tue Jan 9 22:52:59 2021

@author: TCALKARAASLAN
"""
## this project script is controlled with git and published to 
## https://github.com/karaaslanali/pdsnd_github/ 

## refactoring branch changes are at this file

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
        city = input('Input the city that you want to  explore US bike share data.\n ' +
                     'Data is available for below cities\n' + 'Chicago, New York City, or Washington?\n').lower()
					 ## city is made lower case during entry
        if city.lower()  in  ('chicago' ,  'new york city', 'washington'):
              
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input ('Input the  month for which the data to be analyzed\n' +
                       'data is available for below months\n'+
                      'all,january ,february,march,april,may,june?\n').lower()
					  ## After project review, to handle upper case "JUNE" , modified as month= input("...").lower() 
        if month.lower() in ['all', 'january', 'february', 'march',
                             'april', 'may', 'june']:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Input the  day of week for which data to be analyzed\n' +
                    'all, monday, tuesday,wednesday,thursday,friday,saturday,sunday\n')
        if day.lower() in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
                           'friday', 'saturday']:
            
            break
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
        df - pandas DataFrame containing city data filtered by month and day
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

    ##pandas.DataFrame.mode
    ##The mode of a set of values is the value that appears most often. It can be multiple values
    # TO DO: display the most common month
    
    print('The Most Common Month Travelled:')
    print(df['month'].mode()[0])


    # TO DO: display the most common day of week

    print('The Most Common Day Travelled :')
    print(df['day_of_week'].mode()[0])
    
    
    # TO DO: display the most common start hour
    
    #pandas.Series.dt.hour
    #Series.dt.hour
    #The hours of the datetime.

    print('The Most Common Start Hour of Travels:')
    print(df['Start Time'].dt.hour.mode()[0])


    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    ##pandas.DataFrame.mode
    ##The mode of a set of values is the value that appears most often. It can be multiple values
    # TO DO: display the most common month
    
    # TO DO: display most commonly used start station
    print('The Most Common Start Station:')
    
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The Most Common End Station:')
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    
    ''' ## pandas.DataFrame.nlargest
    DataFrame.nlargest(n, columns, keep='first')[source]
    Return the first n rows ordered by columns in descending order.'''
   
    print('The Most Frequency Start & Stop Combination of Stations')
    print(df.groupby(['Start Station' , 'End Station']).size().nlargest(1))
    


    print("\nThis took %s seconds." % (time.time() -  start_time))
    
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    sum_seconds = df['Trip Duration'].sum()
    sum_minutes = sum_seconds / 60
    sum_hours = sum_minutes / 60
    sum_days=sum_hours/24
    
    print(f' Total travel time is:\n  {sum_minutes:.0f} minutes ||  {sum_hours:.0f} hours ||  {sum_days:.0f} days')
    # TO DO: display mean travel time
    
    mean_seconds = df['Trip Duration'].mean()
    mean_minutes = mean_seconds / 60
    
    print(f' Mean travel time is:\n {mean_seconds:.0f} seconds || {mean_minutes:.0f} minutes  ')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('counts of genders:')
    try:
        print(df['Gender'].value_counts())
    except:
        print('Data does not include genders for  {} city'.format(city))
        
    # TO DO: Display earliest, most recent, and most common year of birth
    print('Analyzing earliest, most recent and most common year of birth among bike users')
    try:
        print('Earliest Birth Year: {}\nLatest Birth Year: {} \nMost Common Birth Year: {}'.format(df['Birth Year'].min(), df['Birth Year'].max(),df['Birth Year'].mode()[0]))    
    except:
        print('Data does not include date of birth for {} city'.format(city))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def show_data(df):
     """
     Iterate through 5 entries at a time.
     Returns:
        Print five row entries of data to terminal
     """
     
     view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no :  ")
     start_loc = 0
     while (True):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue? yes or no :  ").lower()
    
        if view_display.lower() in ('no'):
                 break
    
              

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


 
 
if __name__ == "__main__":
	main()
