import pandas as pd
import os

# a = pd.read_csv("2004.csv")
# a["idx"] = a.index
# a["idx"] = a["idx"].apply(lambda x: x+1)
# a.drop("ACVIEW", axis=1, inplace=True)
# a["year"] = [2004 for i in range(len(a))]
# a = a[["idx", "PC Name","No","Type","State","Winning Candidate","Party","Electors","Votes","Turnout","Margin","Margin %"]]
# a.to_csv("2004.csv", index=False)

# l = [i for i in os.listdir(".") if i.endswith(".csv")]
# for i in l:
#     a = pd.read_csv(i)
#     a.drop("year", axis=1, inplace=True)
#     a.to_csv(i, index=False)

a = pd.read_csv("2024.csv")
