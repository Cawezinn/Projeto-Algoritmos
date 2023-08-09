class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        if len(self.arr) <= 1:
            return self.arr

        mid = len(self.arr) // 2
        left_half = self.arr[:mid]
        right_half = self.arr[mid:]

        left_sorter = MergeSort(left_half)
        right_sorter = MergeSort(right_half)

        left_sorted = left_sorter.sort()
        right_sorted = right_sorter.sort()

        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        merged = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged += left[left_index:]
        merged += right[right_index:]

        return merged

lista_1 = input('').split(',')
lista_2 = input('').split(',')
for filme in lista_2:
  lista_1.append(filme)

merge_sort = MergeSort(lista_1)
lista_ordenada = merge_sort.sort()

index = len(lista_ordenada) // 2
print(f'Os amigos decidiram assistir a {lista_ordenada[index]} que estava na posição {index + 1} da lista.')
