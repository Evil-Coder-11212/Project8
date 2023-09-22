import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


meanList = []
for i in range(0,100):
    setOfMeans= random_set_of_mean(30)
    meanList.append(setOfMeans)

sd = statistics.stdev(meanList)
mean = statistics.mean(meanList)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", sd)

first_std_deviation_start, first_std_deviation_end = mean-sd, mean+sd
second_std_deviation_start, second_std_deviation_end = mean-(2*sd), mean+(2*sd)
third_std_deviation_start, third_std_deviation_end = mean-(3*sd), mean+(3*sd)
mean_of_sample = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample)
fig = ff.create_distplot([meanList], ["student marks"], show_hist=False)
fig.show()
z_score = (mean - mean_of_sample)/sd
print("The z score is = ",z_score)