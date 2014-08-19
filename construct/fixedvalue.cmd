>>> SECONDS_PER_DAY = 24 * 60 * 60
>>> instant = 10**3
>>> while instant <= 10**7:
...     print "%10d seconds is %8.2f days" % \
...           (instant, (1.0 * instant / SECONDS_PER_DAY))
...     instant *= 10
      1000 seconds is     0.01 days
     10000 seconds is     0.12 days
    100000 seconds is     1.16 days
   1000000 seconds is    11.57 days
  10000000 seconds is   115.74 days