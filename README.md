# cow-scheduler

```python

from scheduler import Scheduler

scheduler = Scheduler()

def function(x, y):
    print(x + y)

scheduler.add(5, function, x=5, y=7)


# After 5 seconds function will be completed

>>> 12
```

