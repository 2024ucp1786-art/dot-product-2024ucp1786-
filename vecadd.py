
from multiprocessing import Pool

def dot_product(a, b):
    with Pool() as p:
        result = sum(p.starmap(lambda x, y: x*y, zip(a, b)))
    return result

print("Running stable + parallel merged version best")
print(dot_product([1, 2, 3], [4, 5, 6]))


