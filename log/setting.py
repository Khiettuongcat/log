class Colors:
    # --- Text Colors (Foreground) ---
    BLACK        = "\033[0;30m"
    RED          = "\033[0;31m"
    GREEN        = "\033[0;32m"
    BROWN        = "\033[0;33m"
    BLUE         = "\033[0;34m"
    PURPLE       = "\033[0;35m"
    CYAN         = "\033[0;36m"
    LIGHT_GRAY   = "\033[0;37m"
    DARK_GRAY    = "\033[1;30m"
    LIGHT_RED    = "\033[1;31m"
    LIGHT_GREEN  = "\033[1;32m"
    YELLOW       = "\033[1;33m"
    LIGHT_BLUE   = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN   = "\033[1;36m"
    LIGHT_WHITE  = "\033[1;37m"

    # --- Bright ANSI Text Colors (90–97) ---
    BRIGHT_BLACK   = "\033[90m"
    BRIGHT_RED     = "\033[91m"
    BRIGHT_GREEN   = "\033[92m"
    BRIGHT_YELLOW  = "\033[93m"
    BRIGHT_BLUE    = "\033[94m"
    BRIGHT_PURPLE  = "\033[95m"
    BRIGHT_CYAN    = "\033[96m"
    BRIGHT_WHITE   = "\033[97m"

    # --- Background Colors ---
    BG_BLACK     = "\033[40m"
    BG_RED       = "\033[41m"
    BG_GREEN     = "\033[42m"
    BG_YELLOW    = "\033[43m"
    BG_BLUE      = "\033[44m"
    BG_PURPLE    = "\033[45m"
    BG_CYAN      = "\033[46m"
    BG_WHITE     = "\033[47m"

    # --- Bright Background Colors (100–107) ---
    BG_BRIGHT_BLACK   = "\033[100m"
    BG_BRIGHT_RED     = "\033[101m"
    BG_BRIGHT_GREEN   = "\033[102m"
    BG_BRIGHT_YELLOW  = "\033[103m"
    BG_BRIGHT_BLUE    = "\033[104m"
    BG_BRIGHT_PURPLE  = "\033[105m"
    BG_BRIGHT_CYAN    = "\033[106m"
    BG_BRIGHT_WHITE   = "\033[107m"

    # --- Text Styles ---
    BOLD       = "\033[1m"
    FAINT      = "\033[2m"
    ITALIC     = "\033[3m"
    UNDERLINE  = "\033[4m"
    BLINK      = "\033[5m"
    NEGATIVE   = "\033[7m"  # Đảo màu
    CROSSED    = "\033[9m"

    # --- Reset all ---
    END = "\033[0m"
