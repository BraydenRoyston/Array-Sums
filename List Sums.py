# Practice Problem
# You are given a list of numbers in descending order, assume at least one positive and one negative number.
# Find the sum of all negative numbers, and the sum of all positive numbers in said list.

given_array = []            #Enter array here.
sumOfNegatives = 0
sumOfPositives = 0
i = 0

while i < len(given_array):
    if given_array[i] < 0:
        sumOfNegatives += given_array[i]
        i += 1
    else:
        sumOfPositives += given_array[i]
        i += 1
    

print(sumOfNegatives)
print(sumOfPositives)