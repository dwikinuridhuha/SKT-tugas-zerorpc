import zerorpc

class Bank(object):
    saldo = 100
    def cekSaldo(self):
        return (self.saldo)
        
    def inkrisUang(self, tambahUang):
        self.saldo = self.saldo + tambahUang
        return (self.saldo)

    def dikrisUang(self, kurasUang):
        if(kurasUang > self.saldo):
            return ("Saldo anda kurang")
        else:
            self.saldo = self.saldo - kurasUang
            return (self.saldo)

bankBrow = zerorpc.Server(Bank())
bankBrow.bind('tcp://0.0.0.0:5000')
bankBrow.run()