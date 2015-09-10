import pandas as pd
import numpy as np

#Key: for race/ethnicity, 1 = Hispanic, 2 = black, 3 = nonblack, nonhispanic (predominantly white)
# 	  for gender: 1 = male, 2 = female
#	  AFQT is used by armed forces in MOS selection; so-called "g-loaded"; numeric value represents
#     the testers position relative to the population of test-takers (not limited to the sample)

NLYSData = pd.read_csv('NLSY79DataSets/NLSY79Data0.csv', na_values = [-4])

NLYSData.columns = ["Subject", "Ethnicity", "Gender", "AFQT \'79", "AFQT '90", "AFQT '99"]

NLYSData = NLYSData.set_index("Subject")

BCData = NLYSData[["Ethnicity", "AFQT '90"]].dropna()

BCData.to_csv("BellCurveData.csv")
# Added to check that the same results would be produced using the data set I pulled.
# BCData.to_csv("BellCurveData_trial.csv")






