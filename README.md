# Cyclist Bike-Sharing Case Study
In 2016, Cyclistic launched a successful bike-share offering. Since then, the program has grown to a fleet of 5,824 bicycles that are geotracked and locked into a network of 692 stations across Chicago. The bikes can be unlocked from one station and returned to any other station in the system anytime.

Until now, Cyclistic’s marketing strategy relied on building general awareness and appealing to broad consumer segments. One approach that helped make these things possible was the flexibility of its pricing plans: single-ride passes, full-day passes, and annual memberships. Customers who purchase single-ride or full-day passes are referred to as casual riders. Customers who purchase annual memberships are Cyclistic members.

***
## Problem Statement

The director of marketing believes the company’s future success depends on maximizing the number of annual memberships. Therefore, your team wants to understand how casual riders and annual members use Cyclistic bikes differently.

## Preparing and Processing the Data

The data has been taken from [here](https://divvy-tripdata.s3.amazonaws.com/index.html) - 'Divvy_Trips_2019_Q1.csv', 'Divvy_Trips_2019_Q2.csv', 'Divvy_Trips_2019_Q3.csv' and 'Divvy_Trips_2019_Q4.csv'. (Create `./data/` directory and download files into `./data/quarterly_data` directory and run `data_merging.py` to get the `final_data.csv`)

The files are located Quarter wise in the directory `./data/quarterly_data`. The script `data_merging.py` has the code for renaming the column headers for all files to make them consistent accross all files, it also then merges the files together to create a CSV file located in `./data/final_data.csv`.

**Feature Engineering - Created the following features:**
- *year*: Year of travel
- *month*: Month of travel
- *day*: Day of the week (Monday, Tuesday...)
- *is_weekend*: 1 if weekend, 0 otherwise
- *day_of_month*: What day of the month it is (1st, 2nd...31st)
- *quarter*: Which quarter? (1st, 2nd, 3rd or 4th)
- *period*: Part of day - morning, afternoon, evening, etc.
- *hour_of_day*: hour of the day (12am, 1am ...., 11pm)
- *age*: Age of the user.

**Data Cleaning**:
- Removed records where `start_time` is after the `end_time`.
- Removed users whos age at the time of the ride is above 90.
- Removed Testing stations from the records.
- Removed outliers from `tripduration`


## Analyzing the Data (EDA)
After Analyzing the data and visualizing it, the summary of the findings are:
- We found that on an average the ride time for Customers is around 26 minutes whereas the Subscribers have an average ride time of 12 minutes. This might be due to short ride transit from train stations to their offices / home for Subscribers.
- We also see an interesting trend, Subscribers have higher number of rides on weekdays as compared to weekends, whereas we see the opposite in the case of Customers who have higher number of rides on weekends than on weekdays. The reason can be because Subscribers mainly use the bikes for their commute to work whereas Customers generally ride for their leisure.
- Ridership for Customers starts to pick up from the month of April peaks from June through to October and then again drops back in November, December, January and February. We see a similar trend for Subscribers as well.
- We also found that Customers generally ride more in the Afternoon and Evening compared to morning and nights, whereas the Subcribers travel more during the Morning and Evening, more specifically, busiest periods during the day are between 7am to 9am and 4pm to 6pm for Subscribers, which suggest that mostly Subscribers use the bikes for commute to work. Whereas for Customers, we can see from 12pm to 8pm with the peak at around 5pm.
- We also found a huge gender gap in Subscribers with almost around 66% more Male users than Females, the gender gap in Customers was relatively much lower.
- We found that the average age of a Subscriber is 38 years whereas the average age of a Customer is 33. Interestingly, the minimum age of the Subscribers is 8 years but for Customers we found the minimum age to be 19 years.
- We found the most visited Stations by Customers:
	- Streeter Dr & Grand Ave
	- Lake Shore Dr & Monroe St
	- Lake Shore Dr & Noth Blvd
	- Michigan Ave & Oak St
	- Millennium Park
- A more detailed list of the Stations and other findings can be found with visualization in the file - `cyclist_bike-sharing_case_study.ipynb`

## Recommendations
***The recommendations that I would like to propose based on the above findings are as follows:***
- Based on the trips made, we can start the marketing campaigns and advertisements from Febraury till the month of November as the number of trips made by Customers are relatively higher in these months.
- As we observed that Customers ridership often peak at the weekends, so the company can start a Weekend Exclusive subscriptions at a lower price to convert Customers into Subscribers.
- I also obversed that the minimum age of Customers is 19 whereas Subscribers are as low as 8 years old, so the company can launch a program or subcription targetting school going kids and teenagers.
- The Marketing team can target the above mentioned stations more frequently and focus on these stations as a huge number of Customers visit and start their trips from these stations.
- Promoting cycling as a means of their fitness as well as for the well being of our planet - encouraging Customers to start commuting to work on bikes as most of the Subcribers do so.
- We can also share a couple of Stories of Subscribers, who often use bikes to travel to work, on how cycling to work helped them beat the traffic as well as stay fit.