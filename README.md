# Data Wrangling
Here I will post some data wrangling techniques that might be useful for data preprocessing


1. remove duplicated rows
remove duplicates rows according to selected column

There were a few csv files with possible duplicate contract number. I need to remove rows that with the same contract number and only keep one.
My approach was to conbine all files and check for duplicate contract number and keep the first one.

I used functions in pandas library: .append() for conbining multiple csv files; .drop_duplicates() for remove duplicate rows


