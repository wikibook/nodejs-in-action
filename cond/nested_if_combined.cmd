if ph_reliable and ph < 7.0:
    print "%s is acidic." % (ph)
elif ph_reliable and ph > 7.0:
    print "%s is basic." % (ph)
elif ph_reliable:
    print "%s is neutral." % (ph)
else:
    print "That pH reading isn't reliable!"
