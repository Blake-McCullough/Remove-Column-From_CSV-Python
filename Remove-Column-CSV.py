#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com

# import pandas with shortcut 'pd'
import pandas as pd  
#removes a column with matching header value
def Column_Remove(filename,column_Value):
  #Lets user know of actions occuring
    print("Removing column with:",column_Value,"\nFrom: ",filename)
  # read_csv function which is used to read the required CSV file
    data = pd.read_csv(filename,header=0)
    # pop function which is used in removing or deleting columns from the CSV files
    data.pop(column_Value)
    #Saves the file with column removed to 'column-removed.csv'
    data.to_csv("column-removed.csv", index=False)
    #Lets user know of actions occuring
    print("\nSuccessfully removed column:",column_Value,"\nFrom:",filename)



#Column_Remove(filename,columnremove)
filename="output.csv"
columnremove = "DIV"
Column_Remove(filename,columnremove)