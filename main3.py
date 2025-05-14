class TuppleSumFinder:
    def __init__(self, data):
        self.data = data
        def find_sum_indices(self, target_sum):
            for i in range(len(self.data)):
                for j in range(i + 1, len(self.data)):
                    if self.data[i] + self.data[j] == target_sum:
                        return(i, j)
            return None
data_tuple = (10, 20, 30, 40, 50, 60, 70)
target = int(input("Enter the target sum: "))
finder = TuppleSumFinder(data_tuple)
result = finder.find_sum_indices(target)
if result:
    print(f"Indicies of elements that add up to {target}: {result}")
else:
    print(f"No elements found in the tuple in the tuple that add up to {target}.")