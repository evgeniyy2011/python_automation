from Lesson_15.definition import XML_LOGER_FOLDER
import  xml.etree.ElementTree as ET
import logging
from Lesson_15.definition import XML_FOLDER

logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename=XML_LOGER_FOLDER)
loger = logging.getLogger(__name__)
file_log = logging.FileHandler(XML_LOGER_FOLDER)
loger.addHandler(file_log)
formater = logging.Formatter("%(levelname)s - %(message)s")
file_log.setFormatter(formater)
loger.addHandler(file_log)

def check_xml(group_number):
    tree = ET.parse(XML_FOLDER/"groups.xml")
    root = tree.getroot()
    for i in root.findall("group"):
        number = i.find("number")
        if number.text == str(group_number):
            incoming = i.find("timingExbytes/incoming")
            if incoming is not None:
                return incoming.text
            else: return None
loger.info(check_xml(2))
