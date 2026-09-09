import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]

class DatabasePool(metaclass=SingletonMeta):
    def __init__(self):
        self.connection_id = id(self)

def test_worker(results):
    db = DatabasePool()
    results.append(id(db))

if __name__ == '__main__':
    threads = []
    results = []
    for _ in range(10):
        t = threading.Thread(target=test_worker, args=(results,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f'Unique instances created: {len(set(results))}')
    assert len(set(results)) == 1, 'Thread safety failed!'