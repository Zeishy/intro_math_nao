import random

def random_dataset(n):
    dataset = {}
    for i in range(n):
        dataset[f'Expérience {i + 1}'] = [random.random() for _ in range(400)]
    return dataset

result = random_dataset(20)
print(result)