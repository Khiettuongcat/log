import time

from log import log

log.debug('hhehehehhe')
log.info('hhehehehhe')
log.warn('hhehehehhe')
log.success('hhehehehhe')
log.error('hhehehehhe')


name_file = 'data/data_test.log ' # model log_file it will log all fill text or log file .log
data = 'log data check'

log.log_file(name_file, data, level='info')
log.log_file(name_file, data, level='success')
log.log_file(name_file, data, level='warn')
log.log_file(name_file, data, level='error')
log.log_file(name_file, data, level='debug')
log.log_file(name_file, data, level='')

#  in file log

"""
 2025-06-14  09:45:20 | INFO log data check
 2025-06-14  09:45:20 | OK log data check
 2025-06-14  09:45:20 | WARN log data check
 2025-06-14  09:45:20 | ERROR log data check
 2025-06-14  09:45:20 | 🐞 log data check
 2025-06-14  09:45:20 | LOG log data check
"""