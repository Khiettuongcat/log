from .logs import Log

error = Log.error
info = Log.info
warn = Log.warn
success = Log.success
debug = Log.debug
log_file = Log.log_file
log_custom = Log.log_custom

__all__ = ['error', 'info', 'warn', 'success', 'debug', 'log_file', 'log_custom']