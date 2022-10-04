import math

def sum(list):
    sum = 0;
    for i in list:
        sum += i 
    return sum

def square(list):
    square = []
    for i in list:
        square.append(pow(i, 2))
    return square

def cross_product(list1, list2):
    product = [] 
    for i, j in zip(list1, list2):
        product.append(i * j)
    return product

def count(list1):
    return len(list1)

def square_root(item):
    return math.sqrt(item)

def mean(list):
    #function that calculates the mean of an array
        #step 1: find the sum
        #step 2: divide the sum by the length of array
    sum = 0;
    for i in list:
        sum += i #1
    return round(sum / len(list), 3) #2

def standard_deviation(list):
    """ function to calculate the standard deviation of dataset
    step 1: find the mean
    step 2: for each item, find the square of the distance
    step 3: find the sum of all values in step 2
    step 4: divide by the number of data points
    step 5: take the square root """
    average = mean(list) #1
    difference = []
    for i in list:
        difference.append(pow(abs(average - i), 2)) #2
    return round(math.sqrt(mean(difference)), 3)
    #correct answer verified: https://www.calculator.net/standard-deviation-calculator.html

def correlation_coefficient(list1, list2):
    #function to calculate the correlation coefficient of the dataset
        #step 1: find the cross product between two data sets
        #step 2: find the sum of the two data sets and the sum of the cross product
        #step 3: find the square of all values in the dataset and the sum of the square data
        #step 4: calculate r = (n (∑xy)- (∑x)(∑y))/(√ [n ∑x2-(∑x)2][n ∑y2– (∑y)2 )
    return round((count(list1) * sum(cross_product(list1, list2)) - sum(list1) * sum(list2)) / square_root((count(list1) * sum(square(list1)) - pow(sum(list1), 2)) * (count(list1) * sum(square(list2)) - pow(sum(list2),2))), 3)
    #correct answers verfified: https://www.socscistatistics.com/tests/pearson/default2.aspx
    #formula obtained from: https://www.wallstreetmojo.com/pearson-correlation-coefficient/
