import numpy as np

# Fungsi untuk menghitung probabilitas new state diterima sebagai current state
def _prob_acc(a, b, T):
    return np.exp(-(a-b)/T) # p = exp(-(new_cost - current_cost)/T)

# Fungsi untuk mencari nilai x yang baru dengan cara menggeser nilai current x
def _rand(x):
    x += np.random.uniform(-1,1)     # X = X + (random antara -1 sampai 1) 
    while x<-10 or x>10:             # Dibatasi agar nilai X tetap dalam rentang -10 sampai 10
        if x<-10:
            x += np.random.uniform(0,1)
        elif x>10:
            x += np.random.uniform(-1,0)
    return x

# Fungsi yang dicari nilai minimumnya
def _func(a, b):
    return -(np.absolute(np.sin(a) * np.cos(b) * np.exp(np.absolute(1-np.sqrt((np.power(a,2))+(np.power(b,2)))/np.pi))))

T = 100         # T awal 
T_final = 0.001 # T akhir
CR = 0.97       # Cooling rate (Delta T), fungsinya untuk menurunkan suhu

crt_x1 = np.random.uniform(-10,10) # Current X1 dirandom antara range -10 sampai 10
crt_x2 = np.random.uniform(-10,10) # Current X2 dirandom antara range -10 sampai 10
crt_cost = _func(crt_x1, crt_x2)   # Current Cost

# Best-so-far diinisiasi dengan Current State
best_x1 = crt_x1
best_x2 = crt_x2
best_cost = crt_cost