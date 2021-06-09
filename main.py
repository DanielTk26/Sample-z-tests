import statistics
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

data_frame = pd.read_csv("medium_data.csv")


reading_time_data = data_frame["reading_time"].to_list()
population_mean = statistics.mean(reading_time_data)
print("Mean of population: ", population_mean)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(reading_time_data) - 1)
        value = reading_time_data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)
    
    sample_mean = statistics.mean(mean_list)
    print("Mean of samples: ", sample_mean)
    
    sample_standard_deviation = statistics.stdev(mean_list)
    print("Standard deviation of samples: ", sample_standard_deviation)

    first_std_dev_start, first_std_dev_end = sample_mean - sample_standard_deviation, sample_mean + sample_standard_deviation
    second_std_dev_start, second_std_dev_end = sample_mean - (2 * sample_standard_deviation), sample_mean + (2 * sample_standard_deviation)
    third_std_dev_start, third_std_dev_end = sample_mean - (3 * sample_standard_deviation), sample_mean + (3 * sample_standard_deviation)

    df = pd.read_csv("medium_data.csv")
    data = df["reading_time"].tolist()
    mean_of_sample_1 = statistics.mean(data)

    chart = ff.create_distplot([mean_list], ["Reading Time"], show_hist = False)
    chart.add_trace(go.Scatter(x = [mean_of_sample_1, mean_of_sample_1], y = [0, 1], mode = "lines", name = "Sample Mean"))
    chart.add_trace(go.Scatter(x = [first_std_dev_start, first_std_dev_start], y = [0, 1], mode = "lines", name = "First Standard Deviation Start"))
    chart.add_trace(go.Scatter(x = [first_std_dev_end, first_std_dev_end], y = [0, 1], mode = "lines", name = "First Standard Deviation End"))
    chart.add_trace(go.Scatter(x = [second_std_dev_start, second_std_dev_start], y = [0, 1], mode = "lines", name = "Second Standard Deviation Start"))
    chart.add_trace(go.Scatter(x = [second_std_dev_end, second_std_dev_end], y = [0, 1], mode = "lines", name = "Second Standard Deviation End"))
    chart.add_trace(go.Scatter(x = [third_std_dev_start, third_std_dev_start], y = [0, 1], mode = "lines", name = "Third Standard Deviation Start"))
    chart.add_trace(go.Scatter(x = [third_std_dev_end, third_std_dev_end], y = [0, 1], mode = "lines", name = "Third Standard Deviation End"))

    chart.show()

    z_score = (sample_mean - mean_of_sample_1) / sample_standard_deviation
    print("Z Score is: ", z_score)

setup()