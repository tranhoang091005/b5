print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

from sort_module import bubbleSort
n = int(input("Nhập số lượng phần tử trong danh sách: "))
nlist = []
for i in range(n):
  value = float(input(f"Nhập phần tử thứ {i+1}: "))
  nlist.append(value)

sorted_list = bubbleSort(nlist)

print("Danh sách sau khi sắp xếp:", sorted_list)
