# pandas_investigation.py

import pandas as pd

sales_records = pd.read_json("https://api.acodingtutor.com/sales")

print (sales_records.head())

pt = pd.pivot_table(sales_records, 
                    values="Quantity", 
                    index="Product", 
                    columns="Colour", 
                    aggfunc="sum")
pt.fillna(0, inplace=True)

# create a total column which adds the values in a row
pt["Total"] = pt.sum(axis=1)
print (pt)

# .T transposes the dataframe from rows to a single column
totals_row = pt.sum(axis=0).to_frame().T
totals_row.index = ["Total"]
print (totals_row)

# combine the pivot table with the totals_row
pt_with_totals = pd.concat([pt, totals_row])#

print ("*" * 50)
print (pt_with_totals)


