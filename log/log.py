from .setting import Colors as colors
import datetime  as dt
import os
from pathlib import Path

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
        return print(colors.ITALIC + '[debug 🐞]',message + colors.END, sep=" ")

    @staticmethod
    def log_file(link_file, message, level):
        LABELS = {
            "info": "INFO",
            "warn": "WARN",
            "error": "ERROR",
            "success": "OK",
            'debug' : "🐞",
            "default": "LOG",
        }
        label = LABELS.get(level, LABELS['default'])

        time = dt.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        data = f' {time} | {label} {message}'

        with open(link_file, mode='a', encoding='utf-8') as file_note:
            file_note.write(data + '\n')

    @staticmethod
    def log_custom(level,message,color, log_file):
        Colors = {
            # --- Foreground (Text) Colors ---
            "BLACK": "\033[0;30m",
            "RED": "\033[0;31m",
            "GREEN": "\033[0;32m",
            "BROWN": "\033[0;33m",
            "BLUE": "\033[0;34m",
            "PURPLE": "\033[0;35m",
            "CYAN": "\033[0;36m",
            "LIGHT_GRAY": "\033[0;37m",
            "DARK_GRAY": "\033[1;30m",
            "LIGHT_RED": "\033[1;31m",
            "LIGHT_GREEN": "\033[1;32m",
            "YELLOW": "\033[1;33m",
            "LIGHT_BLUE": "\033[1;34m",
            "LIGHT_PURPLE": "\033[1;35m",
            "LIGHT_CYAN": "\033[1;36m",
            "LIGHT_WHITE": "\033[1;37m",

            # --- Bright Foreground Colors ---
            "BRIGHT_BLACK": "\033[90m",
            "BRIGHT_RED": "\033[91m",
            "BRIGHT_GREEN": "\033[92m",
            "BRIGHT_YELLOW": "\033[93m",
            "BRIGHT_BLUE": "\033[94m",
            "BRIGHT_PURPLE": "\033[95m",
            "BRIGHT_CYAN": "\033[96m",
            "BRIGHT_WHITE": "\033[97m",

            # --- Background Colors ---
            "BG_BLACK": "\033[40m",
            "BG_RED": "\033[41m",
            "BG_GREEN": "\033[42m",
            "BG_YELLOW": "\033[43m",
            "BG_BLUE": "\033[44m",
            "BG_PURPLE": "\033[45m",
            "BG_CYAN": "\033[46m",
            "BG_WHITE": "\033[47m",

            # --- Bright Background Colors ---
            "BG_BRIGHT_BLACK": "\033[100m",
            "BG_BRIGHT_RED": "\033[101m",
            "BG_BRIGHT_GREEN": "\033[102m",
            "BG_BRIGHT_YELLOW": "\033[103m",
            "BG_BRIGHT_BLUE": "\033[104m",
            "BG_BRIGHT_PURPLE": "\033[105m",
            "BG_BRIGHT_CYAN": "\033[106m",
            "BG_BRIGHT_WHITE": "\033[107m",

            # --- Text Styles ---
            "BOLD": "\033[1m",
            "FAINT": "\033[2m",
            "ITALIC": "\033[3m",
            "UNDERLINE": "\033[4m",
            "BLINK": "\033[5m",
            "NEGATIVE": "\033[7m",
            "CROSSED": "\033[9m",
        }

        def note_to_file(folder_path, note):



            if not  os.path.join(folder_path): # check seed have folder not
                print('❌ Error: file does not exist:', folder_path)
                return

            try:
                with open(folder_path, mode='a', encoding='utf-8') as files:
                    files.write(note + '\n')
            except Exception as  e:
                print(colors.RED + f'❌ Cannot write to file: {folder_path}\n{e}' + colors.END)


        Cl = Colors.get(color , Colors['BOLD'])
        data = f'{Cl} {level} | {message}  {colors.END}'
        notes = f'{level} | {message}'

        if log_file == '':
            print(data)
        else:
            note_to_file(log_file, notes)