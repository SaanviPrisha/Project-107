import pandas as pd
import csv
import plotly_express as px

file1 = pd.read_csv("data.csv")

data = file1.groupby(['level', 'student_id'], as_index=False).mean()
graph = px.scatter(data, x="student_id", y="level", color="attempt", size="attempt", title="The Average Attempts of Each Student In Each Level")

graph.show()