import time

def findNemo(arr):
    for i in range(len(arr)):
        t1 = time.time()
        if arr[i] == 'nemo':
            print('Nemo Found :D')
        else:
            print('Nemo not found :(')
    t2 = time.time()
    print('Execution Time: ', (t2-t1) * 1e3, 'ms')


nemo = ['nemo']
animals = ['fish', 'lizard', 'lion', 'cheetah', 'monkey', 'crocodile', 'nemo']
custom = [x for x in range(100000)]

findNemo(custom)