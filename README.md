# TestProject
"Телеком-Инжиниринг" Тестовое задание

TCP сервер.  
Подключение осуществляется через клиент **Telnet** на порт **50007**.  
Ожидаемая строка ввода: `"BBBB NN HH:MM:SS.sss GG"`, где   
  - BBBB - 4 цифры (нагрудный номер)  
  - NN - буква и цифра (идентификатор отсечки)  
  - HH:MM:SS.sss - время с точностью до миллисекунд  
  - GG - 2 цифры (номер группы)  
  - Пример: **"0002 C1 01:13:02.877 00"**  
  - Строка должна оканчиваться символом возврата каретки  
Ожидаемый вывод: *"Спортсмен, нагрудный номер BBBB прошёл отсечку NN в «время»"*.  
Данные записываются в лог-файл "log.txt", клиенту выводятся только данные по группе "00"  
