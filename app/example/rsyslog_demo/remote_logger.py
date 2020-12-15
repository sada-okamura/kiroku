import logging

logger = logging.getLogger('remote')


def info(message, tag: str = None):
    logger.info(_to_syslog_format(message, tag))


def _to_syslog_format(message, tag: str = None):
    return '%s: %s' % (tag, message) if tag else message
