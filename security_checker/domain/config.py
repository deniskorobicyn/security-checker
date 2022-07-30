import threading


class Config:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            pass
        return _missing
