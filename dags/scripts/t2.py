import os

resultado_path = os.environ.get('RESULTADO_PATH')

with open(resultado_path, 'r') as f:
    resultado = [int(line.strip()) for line in f.readlines()]

for result in resultado:
    print(f't2: {result}')
