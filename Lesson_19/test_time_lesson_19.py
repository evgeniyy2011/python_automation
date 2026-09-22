import logging
from datetime import datetime


logging.basicConfig(filename="hb_test.log", force=True)
logger = logging.getLogger(__name__)

def test_find_data_in_file():
    new_file = []
    tim = []
    with open("hblog.txt", "r") as f:
        for i in f:
            if "Key TSTFEED0300|7E3E|0400" in i:
                new_file.append(i)
    for q in new_file:
        start = q.find("Timestamp ")
        t = start + len("Timestamp ")
        res = q[t:t+8]
        new = datetime.strptime(res, "%H:%M:%S")
        tim.append(new)
        for i in range(len(tim)-1):
            heart_beat = (tim[i] - tim[i+1]).total_seconds()
            print(heart_beat)
            if 31<heart_beat<33:
                logger.warning(f"WARNING in {tim[i].time()}")
            elif heart_beat>= 33:
                logger.error(f"ERROR in {tim[i].time()}")






