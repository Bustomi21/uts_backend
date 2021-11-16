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
        biaya1= ekor*10000
        print("Harga Ikan Mas Rp : ",biaya1 )

    elif beli == 2:
        biaya1 = ekor*15000
        print("Harga Ikan Cupang Rp : ", biaya1)

    elif beli == 3:
        biaya1 = ekor*23000
        print("Harga Ikan Lohan Rp : ", biaya1)

    elif beli == 4:
        biaya1 = ekor*30000
        print("Harga Ikan Red Devils Rp : ", biaya1)


    elif beli == 5:
        biaya1 = ekor*35000
        print("Harga Ikan Arwana Rp : ", biaya1)


    print("Terima Kasih")
    print("\n==========================================")
    print (" Nama               :",Ih)
    print (" Biaya              :",biaya1)
    




    jawab= input("")
    if jawab == 't':
        break
