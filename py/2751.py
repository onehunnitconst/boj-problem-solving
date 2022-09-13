def heapify(unsorted_list: list, index: int, heap_size: int): 
  largest = index
  left_index = 2 * index + 1
  right_index = 2 * index + 2
  if left_index < heap_size and unsorted_list[left_index] > unsorted_list[largest]:
    largest = left_index
  if right_index < heap_size and unsorted_list[right_index] > unsorted_list[largest]:
    largest = right_index
  if largest != index:
    unsorted_list[largest], unsorted_list[index] = unsorted_list[index], unsorted_list[largest]
    heapify(unsorted_list, largest, heap_size)

def sort(list: list):
  sorted_list = list.copy()
  length = len(sorted_list)
  for index in range(length // 2 - 1, -1, -1):
    heapify(sorted_list, index, n)

  for index in range(length-1, 0, -1):
    sorted_list[0], sorted_list[index] = sorted_list[index], sorted_list[0]
    heapify(sorted_list, 0, index)

  return sorted_list


n = int(input())
list = []

for index in range(n):
  list.append(int(input()))

print(sort(list))