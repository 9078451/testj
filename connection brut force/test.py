import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="t/mdpUse.txt",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('test')