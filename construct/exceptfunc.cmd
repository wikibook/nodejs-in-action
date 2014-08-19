def average(nums):
    sum = 0.0
    for n in nums:
        sum += n
    return sum / len(nums)
...other function definitions skipped...

values = read_values_from_file()
try:
    print 'average:', average(values)
    print 'median:', median(values)
    print 'standard deviation:', std_dev(values)
except ArithmeticError:
    print 'Error in calculations'
