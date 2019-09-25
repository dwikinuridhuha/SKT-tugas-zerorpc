import zerorpc

class Marketplace(object):
    saldoMarket = 100
    def cekSaldoBank(self):
        cekDuit = zerorpc.Client()
        cekDuit.connect('tcp://127.0.0.1:5000')
        keret = cekDuit.cekSaldo()
        return(keret)
    
    def cekSaldoMarket(self):
        return(self.saldoMarket)

    def tambahUangMarket(self, uang):
        cekDuit = zerorpc.Client()
        cekDuit.connect('tcp://127.0.0.1:5000')
        keter = cekDuit.dikrisUang(uang)
        self.saldoMarket = self.saldoMarket + keter
        return(self.saldoMarket)

    def isiDuitBank(self, uang):
        cekDuit = zerorpc.Client()
        cekDuit.connect('tcp://127.0.0.1:5000')
        keter = cekDuit.inkrisUang(uang)
        return(keter)
    
    def MamaBeliPulsa(self, uang):
        MamaPulsa = zerorpc.Client()
        MamaPulsa.connect('tcp://127.0.0.1:4000')
        if(uang > self.saldoMarket):
            return("mama tak punya pulsa")
        else:
            self.saldoMarket = self.saldoMarket - uang
            MamaPulsa.beliPulsaMama(uang)
            return("mama berhasil membeli pulsa")

market = zerorpc.Server(Marketplace())
market.bind("tcp://0.0.0.0:6000")
market.run()