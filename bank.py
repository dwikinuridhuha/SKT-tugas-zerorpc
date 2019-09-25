import zerorpc

class Bank(object):
    saldoBank = 200
    def cekSaldo(self):
        return (self.saldoBank)
        
    def inkrisUang(self, tambahUang):
        self.saldoBank = self.saldoBank + tambahUang
        return (self.saldoBank)

    def dikrisUang(self, kurasUang):
        if(kurasUang > self.saldoBank):
            return ("Saldo anda kurang")
        else:
            self.saldoBank = self.saldoBank - kurasUang
            return (kurasUang)

bankBrow = zerorpc.Server(Bank())
bankBrow.bind('tcp://0.0.0.0:5000')
bankBrow.run()