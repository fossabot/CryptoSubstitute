
from model.clipboard_data import ClipboardData
from model.crypto_types import BitcoinCrypto

#TODO Class take copy and send it to verify

class ClipboardController:
    def __init__(self):
        self.clipboard_content = ClipboardData().clipboard_content()

    def print_clipboard_content(self):#TODO This has to be moved to View
        print(self.clipboard_content) #

    def check_wallet_format(self, wallet_to_check):
        return BitcoinCrypto().recognize_format(wallet=wallet_to_check)