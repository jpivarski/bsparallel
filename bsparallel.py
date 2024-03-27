import builtins
import traceback
import multiprocessing

arguments = multiprocessing.Queue()
dead = multiprocessing.Event()


def work(identifier, task):
    def modified_print(*args, **kwargs):
        args = (identifier + ":",) + args
        kwargs["flush"] = True
        return builtins.print(*args, **kwargs)

    task.__globals__["print"] = modified_print

    builtins.print("BEGIN", identifier, flush=True)
    while True:
        if dead.is_set():
            builtins.print("END BECAUSE DEAD", identifier, flush=True)
            return

        args = arguments.get()
        if args is None:
            builtins.print("END", identifier, flush=True)
            return

        try:
            task(*args)
        except Exception:
            stacktrace = traceback.format_exc().split("\n")
            builtins.print(
                "\n".join(f"{identifier}: {line}" for line in stacktrace), flush=True
            )
            dead.set()
            builtins.print("END WITH ERROR", identifier, flush=True)
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
