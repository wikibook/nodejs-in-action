# The model.
counter = IntVar()
counter.set(0)
# One controller with parameters.
def click(variable, value):
    variable.set(variable.get() + value)
