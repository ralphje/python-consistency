from logging import _checkLevel
from logging import *


Logger.set_level = Logger.setLevel
Logger.is_enabled_for = Logger.isEnabledFor
Logger.effective_level = property(Logger.getEffectiveLevel)
Logger.child = Logger.getChild
Logger.add_filter = Logger.addFilter
Logger.remove_filter = Logger.removeFilter
Logger.add_handler = Logger.addHandler
Logger.remove_handler = Logger.removeHandler
Logger.find_caller = Logger.findCaller
Logger.make_record = Logger.makeRecord
Logger.has_handlers = property(Logger.hasHandlers)


def __handler_get_level(obj):
    # May have been instantiated with a level attribute, so we access it here
    # explicitly
    if not hasattr(obj, '_level'):
        return obj.__dict__['level']
    return obj._level


def __handler_set_level(obj, level):
    obj._level = _checkLevel(level)

Handler.create_lock = Handler.createLock
Handler.level = property(__handler_get_level, __handler_set_level)
Handler.setLevel = __handler_set_level
# setFormatter is useless
Handler.add_filter = Handler.addFilter
Handler.remove_filter = Handler.removeFilter
Handler.handle_error = Handler.handleError


Formatter.format_time = Formatter.formatTime
Formatter.format_exception = Formatter.formatException
Formatter.format_stack = Formatter.formatStack


LogRecord.get_message = LogRecord.getMessage  # not a property due to conflict
# TODO: attributes


logger = getLogger
get_logger_class = getLoggerClass
get_log_record_factory = getLogRecordFactory
add_level_name = addLevelName
get_level_name = getLevelName
make_log_record = makeLogRecord
basic_config = basicConfig
set_logger_class = setLoggerClass
set_log_record_factory = setLogRecordFactory
last_resort = lastResort  # TODO
capture_warnings = captureWarnings
