import statistics

# Sample list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Calculate mean
mean_value = statistics.mean(numbers)

# Calculate median
median_value = statistics.median(numbers)

# Calculate mode
mode_value = statistics.mode(numbers)

# Print results using traditional string formatting
print("Mean: {}".format(mean_value))
print("Median: {}".format(median_value))
print("Mode: {}".format(mode_value))