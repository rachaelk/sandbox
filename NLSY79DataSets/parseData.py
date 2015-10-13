import pandas as pd
import numpy as np

#Key: for race/ethnicity, 1 = Hispanic, 2 = black, 3 = nonblack, nonhispanic (predominantly white)
# 	  for gender: 1 = male, 2 = female
#	  AFQT is used by armed forces in MOS selection; so-called "g-loaded"; numeric value represents
#     the testers position relative to the population of test-takers (not limited to the sample)


print "\nReading data...........\n\n"
NLYSData = pd.read_csv('NLSY79DataSets/NLSY79Data1/NLSY79Data1.csv', na_values = [-4])

NLYSData.columns = ["Subject", "IQ79" , "Ethnicity", "Gender", "Employment79", 
"FamilySize79",  "AFQT \'80", "AFQT '89", "AFQT '06", "Income84", "FamilySize86", 
"FamilySize90", "Employment90", "Income94", "FamilySize96", "FamilySize00", "Income04", 
"Income06","FamilySize06", "Employment06", "Income10", "Income12", "FamilySize12"]

NLYSData.to_csv("NLSY79DataSets/NLSY79Data1/NLSY79Data1_nice.csv",index = False)

print "........Successfully exported to file.\n"

############
## If we wanted to make this more flexible..
## Need to include error handling in case user doesn't input enough column names (or an actual file).
# file = raw_input("\nName of file: >> ")
# columns = raw_input("\nName of columns (separated by comma, please!) >> ")
# name = raw_input("\nName for output file >> ")
# cols = columns.Split(',').ToList();
#
# NLYSData = pd.read_csv('NLSY79DataSets/' + file)
# NLYSData.columns = cols
# NYLSData.to_csv(name + '.csv')

