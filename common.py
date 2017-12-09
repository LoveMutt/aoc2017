import logging


def get_logger(name, level='DEBUG'):
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    loglevel = logging.getLevelName(level)
    logging.basicConfig(level=loglevel)
    return logging.getLogger(name)


def read_input(day):
    fn = 'input_day{:02}.txt'.format(day)
    with open(fn) as f:
        return f.read()
