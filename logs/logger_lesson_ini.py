import logging.config

import logs.logging_lesson2

# main 処理なので、__name__ には、root が入る
logging.config.fileConfig('logging.ini')
logger = logging.getLogger('__name__')

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

logs.logging_lesson2.do_something()