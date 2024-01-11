import random
from random import randint
import pandas as pd
from pandas import DataFrame
import bokeh
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import threading


#range limit for collisions XY
rng = 10
#amounts of iterations
amnt = 10

def event(suc_x, suc_y, x, y):
    state = False
    if suc_x == x and suc_y == y:
        state = True
    else:
        state = False
    return state

data_x = []
data_y = []
data_x2 = []
data_y2 = []

def shoot():
    data = pd.DataFrame({'tryout':[], 'x':[], 'y':[], 'time':[]})
    for i in range(1,amnt):
        start_time = time.time()
        step = 0

        suc_x = random.randint(1,rng)
        suc_y = random.randint(1,rng)

        x = random.randint(1,rng)
        y = random.randint(1,rng)

        data_x.append(suc_x)
        data_y.append(suc_y)
        data_x2.append(x)
        data_y2.append(y)

        while True:
            step += 1


            yes = event (suc_x=suc_x,suc_y=suc_y, x=x, y=y)
            if yes == True:
                print(f'Num of try: {step}')
                print(f'Collision X: {x}')
                print(f'Collision Y: {y}')

                end_time = time.time()
                result_time = end_time - start_time
                print(result_time)

                new_row = pd.DataFrame({'tryout':[step], 'x':[x], 'y':[y], 'time': [result_time]})
                data = pd.concat([data, new_row], ignore_index=True)
                break
    data = data.round(0).astype(int)
    return data


def absolute_rand():
    data = pd.DataFrame({'tryout':[], 'x':[], 'y':[], 'time':[]})
    for i in range(1,amnt):
        start_time = time.time()
        step = 0

        while True:
            step += 1

            suc_x = random.randint(1,rng)
            suc_y = random.randint(1,rng)

            x = random.randint(1,rng)
            y = random.randint(1,rng)

            data_x.append(suc_x)
            data_y.append(suc_y)
            data_x2.append(x)
            data_y2.append(y)

            yes = event (suc_x=suc_x,suc_y=suc_y, x=x, y=y)
            time.sleep(1)

            if yes == True:
                print(f'Num of try: {step}')
                print(f'Collision X: {x}')
                print(f'Collision Y: {y}')

                end_time = time.time()
                result_time = end_time - start_time
                print(result_time)

                new_row = pd.DataFrame({'tryout':[step], 'x':[x], 'y':[y], 'time': [result_time]})
                data = pd.concat([data, new_row], ignore_index=True)
                break

    data[['tryout','x','y']] = data[['tryout','x','y']].round(0).astype(int)
    data['time'] = data['time'].round(3)
    return data


# data visual params

fig, ax = plt.subplots()
xdata1, ydata1 = [], []
xdata2, ydata2 = [], []
ln1, = plt.plot([], [], 'ro')  
ln2, = plt.plot([], [], 'bo')


def init():
    ax.set_xlim(0, rng)
    ax.set_ylim(0, rng)
    return ln1, ln2

def update(frame):
    if data_x and data_y and data_x2 and data_y2:
        
        x1 = frame, data_x[-1]
        y1 = frame, data_y[-1]
        x2 = frame, data_x2[-1]
        y2 = frame, data_y2[-1]

        xdata1.append(x1)
        ydata1.append(y1)
        xdata2.append(x2)
        ydata2.append(y2)

        ln1.set_data(xdata1, ydata1)
        ln2.set_data(xdata2, ydata2)
    return ln1, ln2

#########################################INIT###############################

data_thread = threading.Thread(target=absolute_rand)
data_thread.daemon = True 
data_thread.start()

data_thread = threading.Thread(target=shoot)
data_thread.daemon = True 
data_thread.start()


ani = FuncAnimation(fig, update, frames=np.arange(10), init_func=init, blit=False)

plt.show()

df = absolute_rand()
df.to_csv('results.csv')
print(df)
