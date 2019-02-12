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

while(T > T_final):
    for i in range(50):
        new_x1 = _rand(crt_x1)           # X1 yang baru (digeser dari current X1)
        new_x2 = _rand(crt_x2)           # X2 yang baru (digeser dari current X2)
        new_cost = _func(new_x1, new_x2) # Cost yang baru
        if new_cost < crt_cost:
            # Current State <- New State
            crt_x1 = new_x1
            crt_x2 = new_x2
            crt_cost = new_cost
            
            # Best-so-far <- New State
            best_x1 = new_x1
            best_x2 = new_x2
            best_cost = new_cost
            
            # T optimum <- T
            best_T = T
        else:
            apt = _prob_acc(new_cost, crt_cost, T) # Menghitung nilai Probabilitas
            rand = np.random.uniform(0,1)          # random bilangan real antara 0 sampai 1
            if apt > rand:
                # Current State <- New State
                crt_x1 = new_x1
                crt_x2 = new_x2
                crt_cost = new_cost
    T*=CR
print("Best T = ",best_T)       # T Optimum
print("Best X1 = ",best_x1)     # X1 Terbaik
print("Best X2 = ",best_x2)     # X2 Terbaik
print("Best Cost = ",best_cost) # Cost terbaik