import logging
import json

from Lesson_15.definition import JS_LOGER_FOLDER, JS_TEST_FOLDER
from Lesson_15.definition import XML_FOLDER


logging.basicConfig(filename=JS_LOGER_FOLDER, level=logging.ERROR)
logger = logging.getLogger(__name__)

for i in JS_TEST_FOLDER.iterdir():
    if i.suffix == ".json":
        try:
            with open(i) as file:
                json_obj = json.load(file)
                print(json_obj)
        except json.JSONDecodeError:
            logger.error(f"{i.name} is invalid JSON")

