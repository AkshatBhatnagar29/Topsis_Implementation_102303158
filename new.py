import pandas as pd

data = {
    'Model': ['M1', 'M2', 'M3', 'M4', 'M5'],
    'Storage': [16, 32, 16, 32, 16],
    'Camera': [12, 16, 8, 20, 16],
    'Price': [250, 300, 200, 400, 280],
    'Looks': [5, 4, 3, 5, 3]
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
print("data.csv created successfully!")