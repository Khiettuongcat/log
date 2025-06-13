from .setting import Colors as colors
import datetime  as dt

class Log:

    @staticmethod
    def info(message):
        return print(colors.BLUE + "[info]",message + colors.END, sep=" ")

    @staticmethod
    def success(message):
        return print(colors.GREEN + "[success]",message + colors.END, sep=" ")

    @staticmethod
    def warn(message):
        return print(colors.YELLOW + '[warn]',message + colors.END, sep=" ")

    @staticmethod
    def error(message):
        return print(colors.RED + '[error]',message + colors.END, sep=" ")

    @staticmethod
    def debug(message):
        return print(colors.ITALIC + '[debug]',message + colors.END, sep=" ")

    @staticmethod
    def log_file(link_file, message, level):
        LABELS = {
            "info": "INFO",
            "warn": "WARN",
            "error": "ERROR",
            "success": "OK",
            "default": "LOG",
        }
        label = LABELS.get(level, LABELS['default'])

        time = dt.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        data = f' {time} | {label} {message}'

        with open(link_file, mode='a', encoding='utf-8') as file_note:
            file_note.write(data + '\n')