
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

data = pd.read_csv("StudentsPerformance.csv")
dataList = data['reading score'].tolist();

mean = statistics.mean(dataList);
median = statistics.median(dataList);
mode = statistics.mode(dataList);
sd = statistics.stdev(dataList);

print("Mean :",mean);
print("Median :",median);
print("Mode :",mode);
print("Standard Deviation :",sd);

sd1_str,sd1_end = mean - sd,mean+sd
sd2_str,sd2_end = mean - (2*sd),mean+(2*sd)
sd3_str,sd3_end = mean - (3*sd),mean+(3*sd)

fig = ff.create_distplot([dataList],["Reading Score"]);

fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.035]))
fig.add_trace(go.Scatter(x = [sd1_str,sd1_str], y = [0,0.035]))
fig.add_trace(go.Scatter(x = [sd1_end,sd1_end], y = [0,0.035]))
fig.add_trace(go.Scatter(x = [sd2_str,sd2_str], y = [0,0.035]))
fig.add_trace(go.Scatter(x = [sd2_end,sd2_end], y = [0,0.035]))
fig.add_trace(go.Scatter(x = [sd3_str,sd3_str], y = [0,0.035]))
fig.add_trace(go.Scatter(x = [sd3_end,sd3_end], y = [0,0.035]))

fig.show()

ld_1 = [score for score in dataList if score > sd1_str and score < sd1_end];
ld_2 = [score for score in dataList if score > sd2_str and score < sd2_end];
ld_3 = [score for score in dataList if score > sd3_str and score < sd3_end];

print("1st Standard Deviation: ",len(ld_1)*100.0/len(dataList),"%");
print("2nd Standard Deviation: ",len(ld_2)*100.0/len(dataList),"%")
print("3rd Standard Deviation: ",len(ld_3)*100.0/len(dataList),"%")