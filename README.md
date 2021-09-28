# TravellingSalesman

# Some ressources

## Visualizations

### All
https://www.youtube.com/watch?v=SC5CX8drAtU

### Annealing
https://www.youtube.com/watch?v=NPE3zncXA5s
https://www.fourmilab.ch/documents/travelling/anneal/
https://codecapsule.com/2010/04/06/simulated-annealing-traveling-salesman/
^ Negative exponential as probability distribution (Kirkpatrick, 1984) ??
^ Pseudocode used
```
temperature = temperature_start
while temperature > temperature_end:
    compute cost values and update optimal solution
    temperature = temperature * cooling_factor
```
```
costnew = cost_function(...)
difference = costnew - costprevious
if difference < 0 or  e(-difference/temperature) > random(0,1):
    costprevious = costnew
```
```
costprevious = infinite
temperature = temperature_start
while temperature > temperature_end:
    costnew = cost_function(...)
    difference = costnew - costprevious
    if difference < 0 or  e(-difference/temperature) > random(0,1):
        costprevious = costnew
    temperature = temperature * cooling_factor
```

### 2-opt/3-opt swap
https://www.youtube.com/watch?v=UGGPZnAUjPU
https://www.youtube.com/watch?v=fByHMYjx1Gg

### Greedy solution
Pretty self explanatory
