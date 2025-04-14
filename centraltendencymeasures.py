#write a python program to compute
#central tendency measures mean, median, mode,
#measure of dispersion variance and standard deviation

import statistics

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:          # n is even
        middle1 = sorted_data[n // 2 - 1]        
        middle2 = sorted_data[n // 2]            
        return (middle1 + middle2) / 2

    else:                   # n is odd
        return sorted_data[n // 2]

def calculate_mode(data):
    return statistics.mode(data)


def calculate_variance(data):
    mean_value = calculate_mean(data)
    squared_diff_sum = sum((x - mean_value) ** 2 for x in data)
    return squared_diff_sum / (len(data))   


def calculate_standard_deviation(data):
    variance_value = calculate_variance(data)
    return variance_value ** 0.5


# Example dataset
dataset = [10, 20, 30, 40, 50]
#dataset = [4, 12, 14, 17, 22, 23, 23, 24, 25]
#dataset = [1, 2, 3, 4 , 2, 2]
#dataset = [2, 4, 4, 4, 5, 5, 7, 9]

# Function Calling 
mean_value = calculate_mean(dataset)
median_value = calculate_median(dataset)
mode_value = calculate_mode(dataset)
variance_value = calculate_variance(dataset)
std_deviation_value = calculate_standard_deviation(dataset)



print("Dataset: ",dataset)
print("Mean: ",mean_value)
print("Median: ",median_value)
print("Mode: ",mode_value)
print("Variance: ", variance_value)
print("Standard Deviation: ",std_deviation_value)

