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
BEGIN WORKER-0
WORKER-0: 0
BEGIN WORKER-1
WORKER-1: 1
BEGIN WORKER-2
WORKER-2: 2
BEGIN WORKER-3
WORKER-3: 3
BEGIN WORKER-4
WORKER-4: 4
WORKER-1: 5
WORKER-4: 6
WORKER-0: 7
WORKER-2: 8
WORKER-3: 9
WORKER-4: 10
WORKER-1: 11
WORKER-0: 12
WORKER-3: 13
WORKER-2: Traceback (most recent call last):
WORKER-2:   File "/home/jpivarski/bsparallel.py", line 29, in work
WORKER-2:     task(*args)
WORKER-2:   File "/home/jpivarski/quickie.py", line 9, in task
WORKER-2:     raise Exception
WORKER-2: Exception
WORKER-2: 
END WITH ERROR WORKER-2
END BECAUSE DEAD WORKER-0
END BECAUSE DEAD WORKER-4
END BECAUSE DEAD WORKER-1
END BECAUSE DEAD WORKER-3
```

### Why?

Too many fresh, unconfigured VMs; no time to set up and use a proper parallel framework.
