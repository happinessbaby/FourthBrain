import csv
import numpy as np
import pandas as pd

def csvReader(filename: str):
    # arr = np.loadtxt(f"{filename}", delimiter=" ", dtype=str)
    arr = pd.read_csv(f'{filename}', header=None).values
    
    print(arr)
    return arr

    # with open(f'{filename}', newline='') as file:
    #     reader = csv.read(file, delimiter=' ', quotechar='|')
    #     for row in reader:
    #         res.append(row["first_name"], row["last_name"])
            