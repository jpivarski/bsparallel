### Copy-paste:

```bash
wget https://raw.githubusercontent.com/jpivarski/bsparallel/main/bsparallel.py
```

### Reminder of how to use it:

```python
import time

import bsparallel

def task(i):
    print(i)
    time.sleep(1)
    if i == 8:
        raise Exception

bsparallel.run(5, task, range(20))
```

### And what it does:

```
18:44 BEGIN WORKER-0
18:44 WORKER-0: 0
18:44 BEGIN WORKER-1
18:44 WORKER-1: 1
18:44 BEGIN WORKER-2
18:44 WORKER-2: 2
18:44 BEGIN WORKER-3
18:44 WORKER-3: 3
18:44 BEGIN WORKER-4
18:44 WORKER-4: 4
18:44 FINISHED 5% (1/20)
18:44 WORKER-0: 5
18:44 FINISHED 10% (2/20)
18:44 WORKER-1: 6
18:44 FINISHED 15% (3/20)
18:44 WORKER-2: 7
18:44 FINISHED 20% (4/20)
18:44 WORKER-3: 8
18:44 FINISHED 25% (5/20)
18:44 WORKER-4: 9
18:44 FINISHED 30% (6/20)
18:44 WORKER-0: 10
18:44 FINISHED 35% (7/20)
18:44 WORKER-1: 11
18:44 FINISHED 40% (8/20)
18:44 WORKER-2: 12
18:44 FINISHED 45% (9/20)
18:44 WORKER-4: 13
18:44 WORKER-3: Traceback (most recent call last):
18:44 WORKER-3:   File "/tmp/bsparallel/bsparallel.py", line 35, in work
18:44 WORKER-3:     task(*args)
18:44 WORKER-3:   File "<stdin>", line 5, in task
18:44 WORKER-3: Exception
18:44 WORKER-3:
18:44 END WITH ERROR WORKER-3
18:44 FINISHED 50% (10/20)
18:44 END BECAUSE DEAD WORKER-0
18:44 FINISHED 55% (11/20)
18:44 END BECAUSE DEAD WORKER-1
18:44 FINISHED 60% (12/20)
18:44 END BECAUSE DEAD WORKER-2
18:44 FINISHED 65% (13/20)
18:44 END BECAUSE DEAD WORKER-4
```

### Why?

Too many fresh, unconfigured VMs; no time to set up and use a proper parallel framework.
