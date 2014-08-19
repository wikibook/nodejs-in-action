time = 0
population = 1000   # 1000 bacteria to start with
growth_rate = 0.21 # 21% growth per minute
while population < 2000:
    population = population + growth_rate * population
    print population
    time = time + 1
print "It took %d minutes for the bacteria to double." % time
print "...and the final population was %6.2f bacteria." % population
