import pandas as pd
import plotly.graph_objects as go
import csv
df=pd.read_csv('data3.csv')
student_df=df.loc[df['student_id']=='TRL_987']
print(student_df.groupby('level')['attempt'].mean())
fig=go.Figure(go.Bar(
    x=student_df.groupby('level')['attempt'].mean(),
    y=['level1','level2','level3','level4'],
    orientation='h'
))
fig.show()