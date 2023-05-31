import threading
import time

def worker():
    """Função executada pela thread"""
    print("Thread iniciada:", threading.current_thread().name)
    time.sleep(2)
    print("Thread finalizada:", threading.current_thread().name)

# Cria duas threads
t1 = threading.Thread(target=worker, name='Thread 1')
t2 = threading.Thread(target=worker, name='Thread 2')

# Inicia as threads
t1.start()
t2.start()

# Espera as threads terminarem
t1.join()
t2.join()

print("Programa finalizado.")
