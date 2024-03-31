#WAP to calculate the mean, variance and std. deviation of given list of numbers
print("Name:Bharati Raja Swami\nRoll No: 2210997058")

import statistics

new_list = [ 30, 40, 10, 20, 50, 60, 90]

mean = statistics.mean(new_list)
variance = statistics.variance(new_list)
std_dev = statistics.stdev(new_list)

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")