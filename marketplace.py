import zerorpc

class Marketplace(object):
    def cekSaldoBerow(self):
        cekDuit = zerorpc.Client()
        cekDuit.connect('tcp://127.0.0.1:5000')
        keret = cekDuit.cekSaldo()
        return (keret)
        
    def tambahUang(self, uang):
        cekDuit = zerorpc.Client()
        cekDuit.connect('tcp://127.0.0.1:5000')
        keter = cekDuit.inkrisUang(uang)
        return(keter)

    def kurasUang(self, uang):
        cekDuit = zerorpc.Client()
        cekDuit.connect('tcp://127.0.0.1:5000')
        keter = cekDuit.dikrisUang(uang)
        return(keter)

market = zerorpc.Server(Marketplace())
market.bind("tcp://0.0.0.0:6000")
market.run()