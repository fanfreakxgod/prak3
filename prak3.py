import serial # Импорт модуля для работы с последовательным портом.
import time # Импорт модуля для работы со временем.
import serial.tools.list_ports # Импорт инструментов для работы с последовательными портами.
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200'] # Определение списка скоростей порта.
ports = [p.device for p in serial.tools.list_ports.comports()] # Получение списка доступных последовательных портов.
port_name = ports[0] # Выбор первого доступного порта.
port_speed = int(speeds[-1]) # Выбор максимальной скорости порта из списка.
port_timeout = 10 # Установка таймаута порта.
ard = serial.Serial(port_name, port_speed, timeout=port_timeout) # Инициализация последовательного порта.
time.sleep(1) # Пауза 1 секунда.
ard.flushInput() # Очистка буфера входных данных порта.
try: # Начало блока обработки исключений.
    msg_bin = ard.read(ard.inWaiting()) # Чтение данных из порта.
    msg_bin += ard.read(ard.inWaiting()) # Дополнительное чтение данных из порта.
    msg_bin += ard.read(ard.inWaiting()) # Ещё дополнительное чтение данных из порта.
    msg_bin += ard.read(ard.inWaiting()) # Ещё больше чтения данных из порта.
    msg_str_ = msg_bin.decode() # Декодирование бинарных данных в строку.
    print(len(msg_bin)) # Вывод длины полученных данных.
except Exception as e: # Обработка исключений.
    print('Error!') # Вывод сообщения об ошибке.
ard.close() # Закрытие последовательного порта.
time.sleep(1) # Пауза 1 секунда.
print(msg_str_) # Вывод строки с данными.
