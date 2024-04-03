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
18:34 BEGIN WORKER-0
18:34 WORKER-0: 0
18:34 BEGIN WORKER-1
18:34 WORKER-1: 1
18:34 BEGIN WORKER-2
18:34 WORKER-2: 2
18:34 BEGIN WORKER-3
18:34 WORKER-3: 3
18:34 BEGIN WORKER-4
18:34 WORKER-4: 4
18:34 WORKER-0: 5
18:34 WORKER-1: 6
18:34 WORKER-2: 7
18:34 WORKER-3: 8
18:34 WORKER-4: 9
18:34 WORKER-0: 10
18:34 WORKER-1: 11
18:34 WORKER-2: 12
18:34 WORKER-4: 13
18:34 WORKER-3: Traceback (most recent call last):
18:34 WORKER-3:   File "/home/jpivarski/irishep/bsparallel/bsparallel.py", line 34, in work
18:34 WORKER-3:     task(*args)
18:34 WORKER-3:   File "<stdin>", line 5, in task
18:34 WORKER-3: Exception
18:34 WORKER-3: 
18:34 END WITH ERROR WORKER-3
18:34 END BECAUSE DEAD WORKER-0
18:34 END BECAUSE DEAD WORKER-1
18:34 END BECAUSE DEAD WORKER-2
18:34 END BECAUSE DEAD WORKER-4
```

### Why?

Too many fresh, unconfigured VMs; no time to set up and use a proper parallel framework.
