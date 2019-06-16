from multiprocessing import Process, Queue, Pool
from queue import Empty

from geneticAI.geneticAlgorithm.candidate import Candidate


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


def wait_for_all(session, config):
    result = []
    queue: Queue = session["queue"]
    while True:
        try:
            item = queue.get(timeout=1)
            result.append(Candidate(config, item))
        except Empty:
            break
    for p in session["processes"]:
        p.join()
        del p
    return result
