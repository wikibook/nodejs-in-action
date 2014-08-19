def remove_neg(num_list):
  '''Remove the negative numbers from the list num_list.'''
  for item in num_list:
    if item < 0:
      num_list.remove(item)

