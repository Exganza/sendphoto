import requests
import time

def sendPhoto():
    # TOKEN = "5078330798:AAEUwMca46y6fcvTAxSI8wERvp5sgfNQJjw"
    # CHAT_ID = "1930387592"
    while True:
        TOKEN = "1333009240:AAEp-n3OhOX007-NKvAVvsJ6Z05M_-1jTlU"
        CHAT_ID = "10055408"

        endpoint = requests.get('https://coffee.alexflipnote.dev/random.json').json()
        img = endpoint['file']

        request = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}&photo={img}'

        requests.post(request)
        time.sleep(5)

if __name__ == "__main__":
    sendPhoto()
