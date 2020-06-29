from pyperclip import copy, paste

paste_text = paste()

class ClipboardData:
    def __init__(self):
        self.clipboard_text_content = paste_text

    def copy_wallet(self, wallet):
        copy(wallet)

    def clipboard_content(self):
        return self.clipboard_text_content