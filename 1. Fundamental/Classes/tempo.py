# ANALISE DE PERFORMANCE

import time 

start = time.time()

# BLOCO DE CODIUGO


for c in range(100_000_000):
    pass


end = time.time()


print(f"Levou {end - start:.1f}s para ser executado.")



current_time = time.time()
local_time_struct = time.localtime(current_time)
year = time.localtime(current_time)[0]
month = time.localtime(current_time)[1]
day = time.localtime(current_time)[2]
print(local_time_struct)
