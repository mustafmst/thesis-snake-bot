from multiprocessing import Process, Queue


def start_session():
    return dict(
        queue=Queue(),
        processes=[]
    )


def run_function_in_process(func, args, session):
    process = Process(target=func, args=(args, session["queue"]))
    process.start()
    session["processes"].append(process)
    return session


def wait_for_all(session):
    for process in session["processes"]:
        process.join()
    result = []
    queue: Queue = session["queue"]
    while(not queue.empty()):
        result.append(queue.get())
    return result
