## Main
![bigO Cheatsheet](https://www.bigocheatsheet.com/)

## Good code property
- Readability
- Scalability

![bigO complexity chart](../reference-img/bigO-complexity-chart.png)


## BIG O --> Worst case
The code always assumes worst case, meaning it will run till the end of the loop.

In the below example, you can notice that even though we found nemo on 1 index, still the code is executed till the last element of the array.

```
def findNemo(arr):
    for i in range(len(arr)):
        print('Running: ', i)
        if arr[i] == 'nemo':
            print('Nemo Found :D')
        else:
            print('Nemo not found :(')


animals = ['fish', 'nemo', 'lion', 'cheetah', 'monkey', 'crocodile', 'lizard']

findNemo(animals)
```

```
>python bigO_linear.py
Running:  0
Nemo not found :(
Running:  1
Nemo Found :D
Running:  2
Nemo not found :(
Running:  3
Nemo not found :(
Running:  4
Nemo not found :(
Running:  5
Nemo not found :(
Running:  6
Nemo not found :(
```

We can handle this by using **break** statement and make our code effient and this is a **good code** now.