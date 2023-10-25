import openai
import itertools
import logging
import time
import sys

logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO
    )
logger = logging.getLogger(__name__)


with open("tokens.txt", "r") as f:
    keys = f.readlines()
    keys = [key.strip() for key in keys]

all_keys = itertools.cycle(keys)
openai.api_base = ""

def create(**args):
    global all_keys
    openai.api_key = next(all_keys)
    logger.log(logging.INFO, openai.api_key)

    try:
        result = openai.ChatCompletion.create(**args)
    except openai.error.ServiceUnavailableError:
        logger.info('ServiceUnavailableError')
        result = create(**args)
    except openai.error.RateLimitError:
        logger.info('RateLimitError')
        result = create(**args)
    except openai.error.APIConnectionError:
        logger.info('APIConnectionError') 
        result = create(**args)
    except openai.error.APIError:
        logger.info('APIError')
        time.sleep(2)
        result = create(**args)
    except openai.error.Timeout:
        logger.info('Timeout')
        time.sleep(2)
        result = create(**args)
    # except Exception as e:
    #     print(type(e))

    return result
    
def generate_answer(messages):
    completion = create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
    res_msg = completion.choices[0].message
    return res_msg["content"].strip()


in_file = sys.argv[1]
out_file = sys.argv[2]

prompt = '根据以下文档生成一段对话：\n\n'

with open(in_file, 'r', encoding='utf-8') as fin,\
    open(out_file, 'w', encoding='utf-8') as fout:
    doc = fin.read()
    input = prompt + doc
    messages = [{"role": "user", "content":input}]
    response = generate_answer(messages)
    fout.write(response)

