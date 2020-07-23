from datetime import datetime, timedelta
from threading import Thread
from time import sleep
from uuid import uuid4


class Scheduler:

    def __init__(self, sleep_time=1):
        self.tasks = {}
        self.kill = False
        self.sleep = sleep_time
        Thread(target=self.counter).start()

    def counter(self):
        while not self.kill:
            tmp_tasks = self.tasks.copy()
            for k, v in tmp_tasks.items():
                if v['time'] <= datetime.utcnow():
                    v['thread'].start()
                    self.tasks.pop(k)
            sleep(self.sleep)

    def add(self, time: (int, datetime, timedelta), func, *args, **kwargs):
        if isinstance(time, int):
            time = datetime.utcnow() + timedelta(seconds=time)

        elif isinstance(time, timedelta):
            time = datetime.utcnow() + time

        elif isinstance(time, datetime):
            pass

        else:
            return AttributeError

        self.tasks.update({str(uuid4()): {'time': time,
                                          'thread': Thread(target=func, args=(*args,), kwargs={**kwargs})}})
