import pandas as pd
import plotly.express as px
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
from progressbar import ProgressBar
pbar = ProgressBar()

df = pd.read_csv('StudentsPerformance.csv')
print(df)
results = df.math_score + df.reading_score + df.writing_score
diceMean = statistics.mean(results)
diceMode = statistics.median(results)
diceMedian = statistics.mode(results)
diceStandardDev = statistics.stdev(results)

first_std_dev_start, first_std_dev_end = diceMean-diceStandardDev, diceMean+diceStandardDev
second_std_dev_start, second_std_dev_end = diceMean-(2*diceStandardDev), diceMean+(2*diceStandardDev)
third_std_dev_start, third_std_dev_end = diceMean-(3*diceStandardDev), diceMean+(3*diceStandardDev)

fig = ff.create_distplot([results], ["Result"], show_hist = False)
fig.add_trace(go.Scatter(x=[diceMean,diceMean], y=[0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start],
                         y=[0,0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end],
                         y=[0,0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start],
                         y=[0,0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end],
                         y=[0,0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start],
                         y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end],
                         y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()

list_of_data_1_std_dev = [result for result in df.math_score if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_2_std_dev = [result for result in df.math_score if result > second_std_dev_start and result < second_std_dev_end]
list_of_data_3_std_dev = [result for result in df.math_score if result > third_std_dev_start and result < third_std_dev_end]

print("mean of this data is {}".format(diceMean))
print("median of this data is {}".format(diceMedian))
print("mode of this data is {}".format(diceMode))
print("standard dev of this data is {}".format(diceStandardDev))

print("{}% of data lies within 1 std dev".format(len(list_of_data_1_std_dev)*100.0/len(results)))
print("{}% of data lies within 2 std dev".format(len(list_of_data_2_std_dev)*100.0/len(results)))
print("{}% of data lies within 3 std dev".format(len(list_of_data_3_std_dev)*100.0/len(results)))

