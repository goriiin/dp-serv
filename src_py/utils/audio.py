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

# Импортируем модуль wave для работы с аудио
import wave

# Получаем данные из общей памяти с помощью атрибута buf ()
data = shm.buf

# Создаем объект Wave_write (), который представляет собой файл для записи аудио
# Указываем имя файла, например, audio.wav
wf = wave.open("audio.wav", "wb")

# Устанавливаем параметры аудио, такие как количество каналов, частота дискретизации и глубина бита
# Эти параметры должны соответствовать параметрам аудио, которое мы получили от сокета
# Например, если мы ожидаем получить моно аудио с частотой дискретизации 44100 Гц и глубиной бита 16 бит, то мы можем указать так:
wf.setnchannels(1)
wf.setframerate(44100)
wf.setsampwidth(2)

# Записываем данные в файл с помощью метода writeframesraw ()
wf.writeframesraw(data)

# Закрываем файл с помощью метода close ()
wf.close()
