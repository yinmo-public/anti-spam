# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("2分鐘內輸入此PIN碼 '" + pin + "'在您手機的LINE上")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='或掃描此QR'
        else:
            notice=''
        self.callback('複製此網址 ' + notice + '2分鐘內在您手機的LINE上登入\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
