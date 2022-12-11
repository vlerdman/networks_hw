# Вторая лабораторная работа

## Описание

Решение использует утилиту _ping_, пробуем отсылать пакеты разного размера, пока не найдём максимальный допустимый размер (при помощи бин поиска), в конце не забываем прибавить 28 к полученному значению (длина заголовков IP и ICMP).
Скрипт тестировался на _Ubuntu_, для запуска можно использовать Dockerfile.

## Запуск в Docker

```bash
docker build -t lab2_img .
docker run -i -t lab2_img
python3 script.py yandex.ru
```

## Параметры скрипта
```bash
python3 script.py --help
usage: script.py [-h] [-c C] [-v V] destination

positional arguments:
  destination  dns name or ip address

optional arguments:
  -h, --help   show this help message and exit
  -c C         ping counter
  -v V         verbose output
```

## Примеры запуска
```bash
python3 script.py yandex.ru
Result mtu: 1500 bytes
```
```bash
python3 script.py stackoverflow.com -v true -c 1
Ping exit code: 0
Ping stdout:
PING stackoverflow.com (151.101.129.69) 0(28) bytes of data.
8 bytes from 151.101.129.69 (151.101.129.69): icmp_seq=1 ttl=55

--- stackoverflow.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms


Ping stderr:

Ping exit code: 1
Ping stdout:
PING stackoverflow.com (151.101.129.69) 5000(5028) bytes of data.

--- stackoverflow.com ping statistics ---
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms


Ping stderr:
ping: local error: message too long, mtu=1500

Ping exit code: 1
Ping stdout:
PING stackoverflow.com (151.101.129.69) 2500(2528) bytes of data.

--- stackoverflow.com ping statistics ---
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms


Ping stderr:
ping: local error: message too long, mtu=1500

Ping exit code: 0
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1250(1278) bytes of data.
1258 bytes from 151.101.129.69 (151.101.129.69): icmp_seq=1 ttl=55 time=50.3 ms

--- stackoverflow.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 50.317/50.317/50.317/0.000 ms

Ping stderr:

Ping exit code: 1
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1875(1903) bytes of data.

--- stackoverflow.com ping statistics ---
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms


Ping stderr:
ping: local error: message too long, mtu=1500

Ping exit code: 1
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1562(1590) bytes of data.

--- stackoverflow.com ping statistics ---
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms


Ping stderr:
ping: local error: message too long, mtu=1500

Ping exit code: 0
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1406(1434) bytes of data.
1414 bytes from 151.101.129.69 (151.101.129.69): icmp_seq=1 ttl=55 time=52.5 ms

--- stackoverflow.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 52.499/52.499/52.499/0.000 ms

Ping stderr:

Ping exit code: 1
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1484(1512) bytes of data.

--- stackoverflow.com ping statistics ---
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms


Ping stderr:
ping: local error: message too long, mtu=1500

Ping exit code: 0
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1445(1473) bytes of data.
1453 bytes from 151.101.129.69 (151.101.129.69): icmp_seq=1 ttl=55 time=42.8 ms

--- stackoverflow.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 42.836/42.836/42.836/0.000 ms

Ping stderr:

Ping exit code: 0
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1464(1492) bytes of data.
1472 bytes from 151.101.129.69 (151.101.129.69): icmp_seq=1 ttl=55 time=45.6 ms

--- stackoverflow.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 45.612/45.612/45.612/0.000 ms

Ping stderr:

Ping exit code: 1
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1474(1502) bytes of data.

--- stackoverflow.com ping statistics ---
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms


Ping stderr:
ping: local error: message too long, mtu=1500

Ping exit code: 0
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1469(1497) bytes of data.
1477 bytes from 151.101.129.69 (151.101.129.69): icmp_seq=1 ttl=55 time=44.2 ms

--- stackoverflow.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 44.176/44.176/44.176/0.000 ms

Ping stderr:

Ping exit code: 0
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1471(1499) bytes of data.
1479 bytes from 151.101.129.69 (151.101.129.69): icmp_seq=1 ttl=55 time=44.6 ms

--- stackoverflow.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 44.554/44.554/44.554/0.000 ms

Ping stderr:

Ping exit code: 0
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1472(1500) bytes of data.
1480 bytes from 151.101.129.69 (151.101.129.69): icmp_seq=1 ttl=55 time=44.7 ms

--- stackoverflow.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 44.663/44.663/44.663/0.000 ms

Ping stderr:

Ping exit code: 1
Ping stdout:
PING stackoverflow.com (151.101.129.69) 1473(1501) bytes of data.

--- stackoverflow.com ping statistics ---
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms


Ping stderr:
ping: local error: message too long, mtu=1500

Result mtu: 1500 bytes
```
