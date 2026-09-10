from pathlib import Path

BASE_FOLDER = Path(__file__).parent

#Logers
JS_LOGER_FOLDER = BASE_FOLDER/'js_log.log'
XML_LOGER_FOLDER = BASE_FOLDER/ 'xml_log.log'
CSV_LOGER_FOLDER = BASE_FOLDER/ 'csv_log.log'

#folders with files for testing

JS_TEST_FOLDER = BASE_FOLDER/"work_with_json"

# _______________________________________________________________________


CSV_FILE_FOR_TESTING = BASE_FOLDER/"Poliezhaiev_CSV.csv"

CSV_FOLDER = BASE_FOLDER/"work_with_csv"


# _______________________________________________________________________

XML_FOLDER = BASE_FOLDER/"work_with_xml"




# print(BASE_FOLDER)
# print(JS_LOGER_FOLDER)