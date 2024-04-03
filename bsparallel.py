import time
import builtins
import traceback
import multiprocessing

arguments = multiprocessing.Queue()
dead = multiprocessing.Event()


def timestamp():
    return time.strftime("%H:%M ")


def work(identifier, task):
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
                "\n".join(f"{ts}{identifier}: {line}" for line in stacktrace), flush=True
            )
            dead.set()
            builtins.print(ts + "END WITH ERROR", identifier, flush=True)
            return


workers = []


def run(num_workers, task, inputs):
    for x in inputs:
        if not isinstance(x, tuple):
            x = (x,)
        arguments.put(x)

    for i in range(num_workers):
        arguments.put(None)
        workers.append(multiprocessing.Process(target=work, args=(f"WORKER-{i}", task)))

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()


__all__ = ["run"]
