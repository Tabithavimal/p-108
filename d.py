import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("d.csv")
fig=ff.create_distplot([df["Mobile Brand"].tolist()],["Avg Rating"],show_hist=False)
fig.show()