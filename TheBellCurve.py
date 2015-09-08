import pandas as pd
import numpy as np

#Key: for race/ethnicity, 1 = Hispanic, 2 = black, 3 = nonblack, nonhispanic (predominantly white)
# 	  for gender: 1 = male, 2 = female
#	  AFQT is used by armed forces in MOS selection; so-called "g-loaded"; numeric value represents
#     the testers position relative to the population of test-takers (not limited to the sample)

NLYSData = pd.read_csv('C:\Users\Charmander\Downloads\NLSY79DataSet\NLSY79DataSet.csv', na_values = [-4])

NLYSData.columns = ["Subject", "Ethnicity", "Gender", "AFQT \'79", "AFQT '90", "AFQT '99"]

NLYSData = NLYSData.set_index("Subject")

BCData = NLYSData[["Ethnicity", "AFQT '90"]].dropna()

BCData.to_csv("BellCurveData.csv")






