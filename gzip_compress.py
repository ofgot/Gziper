import gzip
import shutil
import os
import schedule
import time

# file <gzip_compress.py>

directory = '/var/log'


def step():
    for filename in os.listdir(directory):
        with open('/var/log/' + filename, 'rb') as f_in:
            with gzip.open('/var/log/' + filename + '.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


schedule.every(30).days.do(step)


while True:
    schedule.run_pending()
    time.sleep(1)





