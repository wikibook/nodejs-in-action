entry_number = 1
file = open("data.txt", "r")
for line in file :
    line = line.strip()
    if not line.startswith("#"):
      if line == "Earth":
          break
      entry_number = entry_number + 1
print "Earth is the %dth-lightest planet." % (entry_number)
