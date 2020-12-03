# pivot_table
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html

table5=clean.pivot_table(clean,index = None,columns=None)  # columns 是Key只能有一個  #本來的 index=[''],columns=[''],fill_value=0,aggfunc=len
#values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False
print(table4)
