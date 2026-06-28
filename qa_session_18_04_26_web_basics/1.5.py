# QA сесія 18.04.26 | Основи веб
# Тема: 1.5
# Розглянуто:
# -----------------------------------------------

#Як впливає  Gil на потоки в прикладі з факторіалом?

import threading
import time


def work():
    count = 0
    for _ in range(10_000_000):
        count += 1


start = time.time()

threads = [threading.Thread(target=work) for _ in range(2)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("time:", time.time() - start)