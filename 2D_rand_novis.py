import random
from random import randint
import pandas as pd
from pandas import DataFrame
import time

#range limit for collisions XY
rng = 1000
#amounts of iterations
amnt = 100

def event(suc_x, suc_y, x, y):
    state = False
    if suc_x == x and suc_y == y:
        state = True
    else:
        state = False
    return state

def shoot():
    data = pd.DataFrame({'tryout':[], 'x':[], 'y':[], 'time':[]})
    for i in range(1,amnt+1):
        start_time = time.time()
        step = 0

        suc_x = random.randint(1,rng)
        suc_y = random.randint(1,rng)

        x = random.randint(1,rng)
        y = random.randint(1,rng)

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
    for i in range(1,amnt+1):
        start_time = time.time()
        step = 0

        while True:
            step += 1

            suc_x = random.randint(1,rng)
            suc_y = random.randint(1,rng)

            x = random.randint(1,rng)
            y = random.randint(1,rng)

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

    data[['tryout','x','y']] = data[['tryout','x','y']].round(0).astype(int)
    data['time'] = data['time'].round(3)
    return data



df = absolute_rand()
df.to_csv('results.csv')
print(df)
