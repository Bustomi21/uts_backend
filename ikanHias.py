print("\n======Ikan Hias Warna Warni======")
print("Menyediakan Berbagai jenis Ikan Hias Air Tawar ")

Ih = input("Silahkan Masukkan nama anda : ")
print("Nama Pembeli = ", Ih)


jawab= 'y'
while(True):

    ikan = ["Ikan Mas", "Ikan Cupang" , "Ikan Lohan" , "Ikan Red Devils" , "Ikan Arwana" ]
 
    for list in ikan:
        print("\n==== 1. ", ikan[0],"====")
        print("\n==== 2. ", ikan[1],"====")
        print("\n==== 3. ", ikan[2],"====") 
        print("\n==== 4. ", ikan[3],"====") 
        print("\n==== 5. ", ikan[4],"====") 
        break   

    beli = int(input("Silahkan Pilih ikan yang akan dibeli : "))
    ekor = int(input("Berapa Ekor : " ))

    if  beli == 1:
        harga= ekor*10000
        print("Harga Ikan Mas Rp : ",harga )

    elif beli == 2:
        harga = ekor*150000
        print("Harga Ikan Cupang Rp : ", harga)

    elif beli == 3:
        harga = ekor*2300000
        print("Harga Ikan Lohan Rp : ", harga)

    elif beli == 4:
        harga = ekor*20000
        print("Harga Ikan Red Devils Rp : ", harga)

    elif beli == 5:
        harga = ekor*5000000
        print("Harga Ikan Arwana Rp : ", harga)

    print("Terima Kasih ")
    print("\n==========================================")
    print (" Nama               :",Ih)
    print (" Biaya              :",harga)

    jawab= input("")
    if jawab == 't':
        break
