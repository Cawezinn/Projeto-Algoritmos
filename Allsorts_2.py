def selectionsort(array):
  n = len(array)
  for i in range(0, n):
    index = i
    for j in range(i + 1, n):
      if array[j] < array[index]:
        index = j
    array[i], array[index] = array[index], array[i]
    
def shellsort(array):
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
    
def heapify(array, n, i):
  larg = i
  left = 2 * i + 1
  right = 2* i + 2
  
  if left < n and array[i] < array[left]:
    larg = left
  
  if right < n and array[larg] < array[right]:
    larg = right
    
  if larg != i:
    (array[i], array[larg]) = (array[larg], array[i])
    heapify(array, n, larg)

def heapsort(array):
  n = len(array)
  
  for i in range(n//2 - 1, -1, -1):
    heapify(array, n, i)
  
  for i in range(n - 1, 0, -1):
    (array[i], array[0]) = (array[0], array[i])
    heapify(array, i, 0)  
  
def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

    
  
def calc_times(numbers, sort):
  sorted_numbers = sort(numbers.copy())
  comparisons = 0
  swaps = 0

  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      comparisons += 1
      if numbers[i] > numbers[j]:
        swaps += 1

  return comparisons*1 + swaps*2

numbers = input().split()
#calcular tempos
time_isabela = calc_times(numbers, heapsort)
time_mateus = calc_times(numbers, quicksort)
time_joaquim = calc_times(numbers, selectionsort)
time_bianca = calc_times(numbers, shellsort)

#achar vencedores
winners = []
all_times = [time_isabela, time_mateus, time_joaquim, time_bianca]
lowest_time = min(all_times)

for i in range(len(all_times)):
  if all_times[i] == lowest_time:
    winners.append(i)

if len(winners) == 1:
  if winners[0] == 0:
    print(f'Isabela vai assistir o filme da Barbie com seu combo novo após levar {lowest_time} minutos para descobrir o assassino.')
  elif winners[0] == 1:
    print(f'Mateus vai assistir o filme da Barbie com seu combo novo após levar {lowest_time} minutos para descobrir o assassino.')
  elif winners[0] == 2:
    print(f'Joaquim vai assistir o filme da Barbie com seu combo novo após levar {lowest_time} minutos para descobrir o assassino.')
  elif winners[0] == 3:
    print(f'Bianca vai assistir o filme da Barbie com seu combo novo após levar {lowest_time} minutos para descobrir o assassino.')    

  
  
  
  
    