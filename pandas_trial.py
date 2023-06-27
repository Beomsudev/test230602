# Install and import pandas package.
import pandas as pd

# Used titanic csv file from kaggle competition.
# https://www.kaggle.com/competitions/titanic/data

# Change directory to correct location in your computer.
# Read csv file into dataframe. (csv file can be created through excel.)
df = pd.read_csv('train.csv')
# Write dataframe into csv file.
df.to_csv('new.csv')

# 1. Check the csv file read.
print("------------------------------------")
print("--- Original dataframe (Titanic) ---\n")
print(df)

# 2. Check the head of the dataframe (Default 5).
print("\n-------------- HEAD ----------------\n")
print(df.head())

# 3. Check the tail of the dataframe (Default 5).
print("\n-------------- TAIL ----------------\n")
print(df.tail())

# 4. Check the column names of the dataframe.
print("\n---------- COLUMN NAME -------------\n")
print("The name of each column ", df.columns)

# 5. Check the shape (#rows x #columns) and the datatype.
print("\n\nThe shape of the dataframe is ", df.shape)
print("\nThe dataframe type is ", type(df))
print("\nThe data in the dataframe by columns ")
print(df.dtypes)

# # 6. The overall dataframe info.
print("\n\n", df.info())
print("***********")
# 7. Get subset of the dataframe by columns.
subset1 = df[['Survived', 'Name']]
print(subset1)

# 8. Get specific row by index number.
# Note that the name of the columns is not included in the index.
# "loc" can be only used with index above zero.
# While "iloc" can be used with any integer number.
# Indexing
print("INDEXING\n")
print("***************************************")
print(subset1.loc[1]) # 문자로 인덱싱 가능
print("***************************************")

print(subset1.iloc[1]) # 숫자로만 인덱싱
print("***************************************")

print("\n", subset1.iloc[-1])

# [1, 2, 3]
#  0  1  2
#   -3   -2  -1

# Slicing
print("\nSLICING\n")
# Note that the final index is also included for "loc".
# While "iloc" doesn't include the final index.
print("***************************************")
print(subset1.loc[1:4])
print("***************************************")
print(subset1.iloc[1:4]) #range(0, 5)
#                  1 ~ 4-1
print("***************************************")
print("***************************************")
print("***************************************")
# 9. Get specific rows and columns.
# Note that "loc" requires the name of the columns.
# While "iloc" refers the columns with number.
print("***************************************")
print(df.loc[1:4, ['Name', 'Sex']]) # 문자 인덱싱
print("***************************************")
print(df.iloc[1:4, 1:5]) # 숫자 인덱싱 (0~, -1)
#             행1~3 열 1~4
print("\n\n\n\n")


# 10. Define pandas dataframe manually with dictionary data.
new_dict = {'name': ['bob', 'max', 'ted'],
            'age': [21, 23, 20],
            'gender': ['m', 'f', 'f']}

new_df = pd.DataFrame(new_dict)
        # to dataframe
print(new_df)

# 11. Add new column (name: checked).
print("---- new column appended")
new_df = new_df.assign(checked=['checked', 'checked', 'undefined'])

print(new_df)

# 12. Update specific row.
print("---- row 1 updated.")
new_df.loc[1] = ['jay', 24, 'm', 'undefined']
print(new_df)

# 13. Get rows with specific condition.
# Get data that is TRUE for "new_df['age'] > 20" condition.
print(new_df.loc[new_df['age'] > 20])