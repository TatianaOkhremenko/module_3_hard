data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
  "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    sum_all = 0
    for i in data_structure:
        if isinstance(i, list | tuple | set):
          sum_all += calculate_structure_sum(i)
        if isinstance(i, dict):
          for j in i:
            sum_all += len(j)
          sum_all += sum(i.values())
        if isinstance(i, int):
          sum_all += i
        if isinstance(i, str):
          sum_all += len(i)

    return sum_all


result = calculate_structure_sum(data_structure)
print(result)
