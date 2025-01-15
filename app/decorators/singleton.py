import threading


def singleton(cls):
    instances = {}
    lock = threading.Lock()  # Asegura acceso seguro en entornos multi-hilo

    def get_instance(*args, **kwargs):
        with lock:  # Bloquea el acceso mientras se crea la instancia
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
