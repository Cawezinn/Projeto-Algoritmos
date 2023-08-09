def selection_sort(array):
  n = len(array)
  for i in range(0, n):
    index = i
    for j in range(i + 1, n):
      if array[j] < array[index]:
        index = j
    array[i], array[index] = array[index], array[i]
    
def shell_sort(array):
  n = len(array)
  mid = n // 2
  while mid > 0:
    for i in range(mid, n):
      change = array[i]
      j = i
      while j >= mid  and array[j - mid] > change:
         array[j] = array[j - mid]
         j = j - mid
      array[j] = change
    mid = mid // 2    