import time
import builtins
import traceback
import multiprocessing

arguments = multiprocessing.Queue()
counter = multiprocessing.Value("i", 0)
dead = multiprocessing.Event()


def timestamp():
    return time.strftime("%H:%M ")


def work(identifier, task, total):
    def modified_print(*args, **kwargs):
        args = (timestamp() + identifier + ":",) + args
        kwargs["flush"] = True
        return builtins.print(*args, **kwargs)

    task.__globals__["print"] = modified_print

    builtins.print(timestamp() + "BEGIN", identifier, flush=True)
    while True:
        if dead.is_set():
            builtins.print(timestamp() + "END BECAUSE DEAD", identifier, flush=True)
            return

        args = arguments.get()
        if args is None:
            builtins.print(timestamp() + "END", identifier, flush=True)
            return

        try:
            task(*args)

        except Exception:
            stacktrace = traceback.format_exc().split("\n")
            ts = timestamp()
            builtins.print(
                "\n".join(f"{ts}{identifier}: {line}" for line in stacktrace),
                flush=True,
            )
            dead.set()
            builtins.print(ts + "END WITH ERROR", identifier, flush=True)
            return

        else:
            ts = timestamp()
            with counter.get_lock():
                counter.value += 1
                counter_now = counter.value
            builtins.print(
                ts + f"FINISHED {100*counter_now/total:.0f}% ({counter_now}/{total})"
            )


workers = []


def run(num_workers, task, inputs):
    total = 0
    for x in inputs:
        if not isinstance(x, tuple):
            x = (x,)
        arguments.put(x)
        total += 1

    for i in range(num_workers):
        arguments.put(None)
        workers.append(
            multiprocessing.Process(target=work, args=(f"WORKER-{i}", task, total))
        )

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()


__all__ = ["run"]
