import plotly.express as px
import plotly.figure_factory as ff 
import statistics
import pandas as pd

raw_data = pd.read_csv("data.csv")
data = raw_data["reading score"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
stdev = statistics.stdev(data)

stdev1_start, height_stdev1_end = mean-stdev, mean+stdev
stdev2_start, height_stdev2_end = mean-(2*stdev), mean+(2*stdev)
stdev3_start, height_stdev3_end = mean-(3*stdev), mean+(3*stdev)

stdev1_percent = [result for result in data if result > stdev1_start and result < height_stdev1_end] 
stdev2_percent = [result for result in data if result > stdev2_start and result < height_stdev2_end] 
stdev3_percent = [result for result in data if result > stdev3_start and result < height_stdev3_end] 

print("Mean = ", str(mean), ", Median = ", str(median),", Mode = ", str(mode), ", Standard Deviation = ", str(stdev))

print("{}% of data lies within stdev 1".format(len(stdev1_percent)*100.00/len(data)))
print("{}% of data lies within stdev 2".format(len(stdev2_percent)*100.00/len(data)))
print("{}% of data lies within stdev 3".format(len(stdev3_percent)*100.00/len(data)))