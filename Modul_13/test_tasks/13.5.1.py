values = [-7, -7, 7, 7]
std = 42

def count_std():
    mean = sum(values)/len(values)
    std = (sum([(values-mean) ** 2 for value in values]) / len(values)) ** 0.5
    return std

def normalize(value):
    result = value / std
    return result

print(normalize(21))

