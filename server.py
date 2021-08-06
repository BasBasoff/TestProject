import logging
import datetime
import socket
import re

HOST = ''   
PORT = 50007
MAX_CONNECTIONS = 1
PACKET_SIZE = 1024

#recognize patterns
request_pattern = r'\d{4}\s[A-Z][0-9]\s[0|1][0-9]:[0-6][0-9]:[0-6][0-9].\d{3}\s\d{2}'
bib_number_pattern = r'^\d{4}\b'
channel_id_pattern = r'\b[A-Z][0-9]\b'
time_pattern = r'\b[0|1][0-9]:[0-6][0-9]:[0-6][0-9].\d{1}'
group_pattern = r'\d{2}$'

#logging settings
logging.basicConfig(filename='log.txt', level=logging.INFO, encoding='utf-8')

print(f'Server listening on localhost:{PORT}')
logging.info(f'{datetime.datetime.now()}:Socket was binded by {HOST}:{PORT}. Listen {MAX_CONNECTIONS} connections')

def encode_response_string(bib_number, channel_id, time):
    response_string = f'Cпортсмен, нагрудный номер {bib_number} прошел отсечку {channel_id} в {time}'
    return bytes(response_string, encoding='utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(MAX_CONNECTIONS)
    conn, addr = sock.accept()    
    decode_data = ''
    with conn:
        print('Connected by', addr)
        logging.info(f'{datetime.datetime.now()}:Connected by {addr}')
        while True:
            data = conn.recv(PACKET_SIZE) 
            if not data == b'\r\n' or data == b'\r':
                decode_data += data.decode('utf-8')
                continue            
            
            if not re.fullmatch(request_pattern, decode_data): 
                print('Not valid data')
                logging.error(f'Not valid data: "{decode_data}"')
                break

            bib_number = re.search(bib_number_pattern, decode_data)[0]
            channel_id = re.search(channel_id_pattern, decode_data)[0]
            time = re.search(time_pattern, decode_data)[0]
            group = re.search(group_pattern, decode_data)[0]            
            
            if bib_number and channel_id and time:
                response = encode_response_string(bib_number, channel_id, time)
                if group == '00':
                    conn.sendall(response) 
                decode_data = ''
                logging.info(f'{datetime.datetime.now()}:{response.decode("utf-8")}')           
