# Импортируем модуль socket для работы с сокетами
import socket

# Импортируем модуль multiprocessing.shared_memory для работы с общей памятью
import multiprocessing.shared_memory

# Создаем сокет, который будет слушать порт 8080 и принимать входящие соединения
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8080))
s.listen()
print("Waiting for connection...")

# Принимаем соединение от клиента
conn, addr = s.accept()
print(f"Connected by {addr}")

# Создаем объект SharedMemory, который будет хранить данные в общей памяти
# Указываем параметр create=True, чтобы создать новую общую память
# Указываем параметр size=1024, чтобы выделить 1024 байта памяти
shm = multiprocessing.shared_memory.SharedMemory(create=True, size=1024)

# Объявляем переменную total_size, которая будет хранить общий размер данных, которые мы получим
total_size = 0

# Читаем данные из сокета по частям, пока не получим все данные или не встретим конец потока
while True:
    # Читаем 1024 байта данных из сокета и сохраняем их в переменную chunk
    chunk = conn.recv(1024)

    # Если мы не получили никаких данных, то это означает, что поток закончился
    # Выходим из цикла while
    if not chunk:
        break

    # Получаем размер данных, которые мы получили, и добавляем его к общему размеру данных
    chunk_size = len(chunk)
    total_size += chunk_size

    # Проверяем, не превышает ли общий размер данных размер общей памяти
    # Если да, то увеличиваем размер общей памяти на нужное количество байтов с помощью метода resize ()
    if total_size > shm.size:
        shm.resize(total_size)

    # Записываем данные в общую память с помощью атрибута buf (), который является байтовой строкой или байтовым массивом
    # Используем срезы для указания места, куда записать данные
    shm.buf[total_size-chunk_size:total_size] = chunk

# Получаем данные из общей памяти с помощью атрибута buf ()
data = shm.buf

# Закрываем соединение с клиентом
conn.close()

# Закрываем объект SharedMemory
shm.close()

# Удаляем объект SharedMemory из системы с помощью метода unlink ()
shm.unlink()

# Закрываем сокет
s.close()
