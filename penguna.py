import zerorpc

while True:
    try:
        print("1. mengisi\n2. beli\n3. cekSaldo\n4. keluar")
        pilih = int(input("pilih: "))
        if(pilih == 1):
             masuk = int(input("masukan nominal: "))
             penguna = zerorpc.Client()
             penguna.connect("tcp://127.0.0.1:6000")
             keter = penguna.tambahUang(masuk)
             print("sekarang uang anda: ", keter)

        elif(pilih == 2):
            masuk = int(input("masukan nominal: "))
            penguna = zerorpc.Client()
            penguna.connect("tcp://127.0.0.1:6000")
            keter = penguna.kurasUang(masuk)
            print("sekarang uang anda: ", keter)
        
        elif(pilih == 3):
            penguna = zerorpc.Client()
            penguna.connect("tcp://127.0.0.1:6000")
            keter = penguna.cekSaldoBerow()
            print("Saldo anda: ", keter)

        elif(pilih == 4):
            break
        
        else:
            print("anda salah input")
            
    except KeyboardInterrupt:
        print("galat")