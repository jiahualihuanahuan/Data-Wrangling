
import os
cwd = os.path.abspath('')
cwd

import os
os.chdir('/Users/jiahuali1991/Dropbox/Machine Learning/Data/Bensi/20200804/csv')
cwd = os.path.abspath('')
files = os.listdir(cwd)
print(cwd)
print(files)

'''
# combine all .csv file in a folder
import pandas as pd
df = pd.DataFrame()
for file in files:
    if file.endswith(".csv"):
           df = df.append(pd.read_csv(file, header=None))
df.shape
'''

# combine 202 and 917 by row
import pandas as pd
df202 = pd.read_csv('202.csv', header=0)
df202.columns
df202.shape

df917 = pd.read_csv('917.csv', header=0)
df917.columns
df917.shape

df = pd.concat([df202, df917], axis=0)
df.columns
df.shape



# checking missing data and drop

#df['Product'].notnull()

df202_product_dropna = df202.dropna(subset=['Product'])
df202.shape
df202_product_dropna.shape # 2 rows missing 'Product' in 202

df917_product_dropna = df917.dropna(subset=['Product'])
df917.shape
df917_product_dropna.shape # 2 rows missing 'Product' in 917

df_product_dropna = df.dropna(subset=['Product'])
df.shape
df_product_dropna.shape # 4 rows missing 'Product' in 202 and 917 combined




# DataFrame.str.contains('strings')
# return rows that contins certain strings
df202_3cuts = df202_product_dropna[df202_product_dropna['Product'].str.contains('Frozen pork sides in 3 cuts')]
df202_3cuts.shape

df917_3cuts = df917_product_dropna[df917_product_dropna['Product'].str.contains('Frozen pork sides in 3 cuts')]
df917_3cuts.shape

df_3cuts = df_product_dropna[df_product_dropna['Product'].str.contains('Frozen pork sides in 3 cuts')]
df_3cuts.shape



# Remove Duplicates: 1 dataframe.drop_duplicates(); 2 dataframe.duplicated()
# remove duplicates in dataframes
df202_3cuts_remove_duplicates = df202_3cuts.drop_duplicates(subset=['Contract', 'Product'], keep = 'first')
df202_3cuts_remove_duplicates.shape

df917_3cuts_remove_duplicates = df917_3cuts.drop_duplicates(subset=['Contract', 'Product'], keep = 'first')
df917_3cuts_remove_duplicates.shape

df_3cuts_remove = df_3cuts.drop_duplicates(subset = ['Contract','Product'], keep = 'first') 
df_3cuts_remove.shape

df_3cuts_remove = df_3cuts.drop_duplicates(subset = ['Contract', 'Product','Weight'], keep = 'first') 
df_3cuts_remove.shape
df_3cuts_remove.iloc[:,[3]]


'''
# duplicated() function return bool for each value
df_duplicates = df.duplicated(subset = ['Contract', 'Product','Weight'], keep = 'first') 
df.shape
df_duplicates.shape
df_duplicates[df_duplicates=='True']
'''


# Export dataframe to csv file
df_remove.to_csv('/Users/jiahuali1991/Dropbox/Machine Learning/Data/Bensi/20200804/remove_duplicates/remove_duplicates_202_917.csv', header=None)

df_remove.tail(10)

df = df[df[8] == 202]
print(df.shape)
df.to_csv('/Users/jiahuali1991/Dropbox/Machine Learning/Data/Bensi/20200804/remove_duplicates/202_remove_duplicates.csv', header=None)

df801 = df[df[7]==801]
print(df801.shape)
df801.to_csv('/Users/jiahuali1991/Dropbox/Machine Learning/Data/Bensi/20200804/remove_duplicates/801_remove_duplicates.csv', header=None)


df338 = df[df[6]==338]
print(df338.shape)
df338.to_csv('/Users/jiahuali1991/Dropbox/Machine Learning/Data/Bensi/20200804/338_remove_duplicates.csv', header=None)






