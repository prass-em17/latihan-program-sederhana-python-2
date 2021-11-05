
#I
from os import system
import time
from time import localtime
import datetime
import threading
from datetime import datetime
import sys
from os import system
import time

#data
user={"emoney":300000, "token":0, "name":"pras", "pin":"1019", "vchr":"1q2w3e", "unvalid":0, "chance":1}
#fungsi
#menu awal    
def main():
    while True:
        system("cls")
        print("        ================================================        ")
        print("        DUUUUUUUUUUUUUAAAAAAAAAAAAAAARRRRRRRRRRRRRRRR!!!!!")
        print("\n        DAPATKAN DISKON 30% KHUSUS PEMBELIAN DI HARI INI !")
        print("        BERLAKU 1x PEMAKAIAN DAN 2 MENIT SETELAH LOGIN")
        print("        ================================================        ")
        print("\n        ===   Saldo anda = ","Rp.",user["emoney"])
        print("        ===   Token anda = ", user["token"],"Token")
        print("        ================================================       ")
        print("        ===    Silahkan Pilih Menu Yang Tersedia     ===~~~~~~~")
        print("        ================================================       ")
        print("        ===   1. Top Up                              ===       ")
        print("        ===   2. Skin Bundle                         ===       ")
        print("        ===   3. Keluar                              ===       ")
        print("        ================================================       ")
        plhn = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if plhn == 1:
            print("")
            print("")
            print("")
            topup()
            break
        if plhn == 2:
            print("")
            print("")
            print("")
            skin()
            break
        if plhn == 3:
            exit()
        else :
            system("cls")
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")
            loadan = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            for i in range(len(loadan)):
                time.sleep(0.2)
                sys.stdout.write("\r" + loadan[i % len(loadan)])
                sys.stdout.flush()

def vchr():
    while True:
        print("        ===                 VOUCHER                  ===~~~~~~~~")
        print("        ================================================        ")
        print("        ===   1. Token 35            Rp. 50.000      ===        ")
        print("        ===   2. Token 75            Rp. 120.000     ===        ")
        print("        ===   3. Token 150           Rp. 225.000     ===        ")
        print("        ===   4. Keluar                              ===        ")
        print("        ================================================        ")

def topup():
    while True:
        system("cls")
        print("        ===   Saldo anda = ","Rp.",user["emoney"])
        print("        ===   Token anda = ", user["token"],"Token")
        print("        ================================================       ")
        print("        ===       Silahkan Pilih Nominal Top Up      ===~~~~~~~~")
        print("        ================================================        ")
        print("        ======== Nominal ============== Harga ==========        ")
        print("        ===   1. Token 35            Rp. 50.000      ===        ")
        print("        ===   2. Token 75            Rp. 120.000     ===        ")
        print("        ===   3. Token 150           Rp. 225.000     ===        ")
        print("        ===   4. Keluar                              ===        ")
        print("        ================================================        ")
        plhn = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if plhn == 1:
            print("")
            print("")
            print("")
            tkn35()
            print("")
            print("")
            ulang1()
            break
        elif plhn == 2:
            print("")
            print("")
            print("")
            tkn75()
            print("")
            print("")
            ulang1()
            break
        elif plhn == 3:
            print("")
            print("")
            print("")
            tkn130()
            print("")
            print("")
            ulang1()
            break
        elif plhn == 4:
            exit()
        else :
            system("cls")
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")
            loadan = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            for i in range(len(loadan)):
                time.sleep(0.2)
                sys.stdout.write("\r" + loadan[i % len(loadan)])
                sys.stdout.flush()
def skin():
    while True:
        system("cls")
        print("        ===   Saldo anda = ","Rp.",user["emoney"])
        print("        ===   Token anda = ", user["token"],"Token")
        print("        ================================================       ")
        print("        ===        Silahkan Pilih Skin Bundle        ===~~~~~~~~")
        print("        ================================================        ")
        print("        ======== Skin ================= Harga ==========        ")
        print("        ===   1. Skin M416 Volcano    60 Token       ===        ")
        print("        ===   2. Skin AKM Draconic    95 Token       ===        ")
        print("        ===   3. Skin AWP Pharaoh    140 Token       ===        ")
        print("        ===   4. Keluar                              ===        ")
        print("        ================================================        ")
        plhn = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if plhn == 1:
            print("")
            print("")
            print("")
            skn1()
            print("")
            print("")
            ulang2()
            break
        elif plhn == 2:
            print("")
            print("")
            print("")
            skn2()
            print("")
            print("")
            ulang2()
            break
        elif plhn == 3:
            print("")
            print("")
            print("")
            skn3()
            print("")
            print("")
            ulang2()
            break
        elif plhn == 4:
            exit()
        else :
            system("cls")
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")
            loadan = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            for i in range(len(loadan)):
                time.sleep(0.2)
                sys.stdout.write("\r" + loadan[i % len(loadan)])
                sys.stdout.flush()
        


#ulang
def ulangpin():
    while True: 
        print("        ===   1. Masukkan Pin Lagi                   ===       ")
        print("        ===   2. Keluar                              ===       ")
        ulang = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if ulang == 1:
            print("")
            print("")
            print("")
            break
        elif ulang == 2:
            exit()
def ulang1():
    while True: 
        print("        ===    Apakah anda ingin mengulang lagi?     ===       ")
        print("        ================================================       ")
        print("        ===   1. Kembali                             ===       ")
        print("        ===   2. Ke Menu Utama                       ===       ")
        print("        ===   3. Keluar                              ===       ")
        print("        ================================================       ")
        ulang = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if ulang == 1:
            print("")
            print("")
            print("")
            topup()
            break
        elif ulang == 2:
            print("")
            print("")
            print("")
            main()
            break
        elif ulang == 3:
            exit()
        else :
            system("cls")
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")
            loadan = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            for i in range(len(loadan)):
                time.sleep(0.2)
                sys.stdout.write("\r" + loadan[i % len(loadan)])
                sys.stdout.flush()
            system("cls")
            

def ulang2():
    while True: 
        print("        ===    Apakah anda ingin mengulang lagi?     ===       ")
        print("        ================================================       ")
        print("        ===   1. Kembali                             ===       ")
        print("        ===   2. Ke Menu Utama                       ===       ")
        print("        ===   3. Keluar                              ===       ")
        print("        ================================================       ")
        ulang = int(input("~~~~~~~~===   Masukkan Pilihan = "))
        if ulang == 1:
            print("")
            print("")
            print("")
            skin()
            break
        elif ulang == 2:
            print("")
            print("")
            print("")
            main()
            break
        elif ulang == 3:
            exit()
        else :
            system("cls")
            print("")
            print("")
            print("        ================================================       ")
            print("        ===          Pilihan Tidak Tersedia          ===       ")
            print("        ================================================       ")
            print("")
            print("")
            loadan = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            for i in range(len(loadan)):
                time.sleep(0.2)
                sys.stdout.write("\r" + loadan[i % len(loadan)])
                sys.stdout.flush()
            system("cls")

#TOPUP
def tkn35():
    system("cls")
    if(int(user["emoney"]) < 50000) :
        print("        ================================================       ")
        print("        ===          Saldo anda tidak cukup          ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["emoney"]) - 50000
        user["emoney"] = c
        d =int(user["token"]) + 35
        user["token"] = d
        print("        ================================================       ")
        print("        ===       Pembelian anda telah berhasil      ===       ")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 
        
def tkn75():
    system("cls")
    if(int(user["emoney"]) < 120000) :
        print("        ================================================       ")
        print("        ===          Saldo anda tidak cukup          ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["emoney"]) - 120000
        user["emoney"] = c
        d =int(user["token"]) + 75
        user["token"] = d
        print("        ================================================       ")
        print("        ===       Pembelian anda telah berhasil      ===       ")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 

def tkn130():
    system("cls")
    if(int(user["emoney"]) < 225000) :
        print("        ================================================       ")
        print("        ===          Saldo anda tidak cukup          ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["emoney"]) - 225000
        user["emoney"] = c
        d =int(user["token"]) + 150
        user["token"] = d
        print("        ================================================       ")
        print("        ===       Pembelian anda telah berhasil      ===       ")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 

#SKIN
def skn1():
    system("cls")
    if(int(user["token"]) < 60) :
        print("        ================================================       ")
        print("        ===          Token anda tidak cukup          ===       ")
        print("        ===     Silahkan Melakukan Top Up Kembali    ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        waktu = datetime.now()
        menit1 = int(waktu.strftime("%M"))
        print("Anda berada di menit ke-",menit1)
        limit = menit1 + 2
        invchr = str(input("Masukkan Kode Voucher Discount. Jika Tidak Ada Isi 0 \n=>>"))
        waktu = datetime.now()
        menit = int(waktu.strftime("%M"))
        timer = menit - limit
        if user["unvalid"] == 0 and invchr == user["vchr"] and timer < 2:
            system("cls")
            print("\nSelamat! Anda Mendapatkan Diskon 30%")
            c =int(user["token"]) - int(60 * 0.3)
            user["token"] = c
            user["unvalid"] = 1
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif user["unvalid"] == 0 and invchr == user["vchr"] and timer > 2:
            print ("\nMaaf Kode Voucher Telah Kadaluarsa\nAnda Mendapatkan Harga Normal")
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif user["unvalid"] == 1 and invchr == user["vchr"] and timer > 2:
            print ("\nMaaf Kode Voucher Telah Kadaluarsa\nAnda Mendapatkan Harga Normal")
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif user["unvalid"] == 1 and invchr == user["vchr"] and timer < 2:
            print ("\nMaaf Kode Voucher Telah Digunakan\nAnda Mendapatkan Harga Normal")
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif invchr == "0":
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif invchr != user["vchr"] and invchr != 0:
            print ("\nMaaf Kode Voucher Salah\nAnda Mendapatkan Harga Normal")
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 

def skn2():
    system("cls")
    if(int(user["token"]) < 95) :
        print("        ================================================       ")
        print("        ===          Token anda tidak cukup          ===       ")
        print("        ===     Silahkan Melakukan Top Up Kembali    ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        waktu = datetime.now()
        menit1 = int(waktu.strftime("%M"))
        print("Anda berada di menit ke-",menit1)
        limit = menit1 + 2
        invchr = str(input("Masukkan Kode Voucher Discount. Jika Tidak Ada Isi 0 \n=>>"))
        waktu = datetime.now()
        menit = int(waktu.strftime("%M"))
        timer = menit - limit
        if user["unvalid"] == 0 and invchr == user["vchr"] and timer < 2:
            system("cls")
            print("\nSelamat! Anda Mendapatkan Diskon 30%")
            c =int(user["token"]) - int(60 * 0.3)
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif user["unvalid"] == 0 and invchr == user["vchr"] and timer > 2:
            print ("\nMaaf Kode Voucher Telah Kadaluarsa\nAnda Mendapatkan Harga Normal")
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif user["unvalid"] == 1 and invchr == user["vchr"] and timer > 2:
            print ("\nMaaf Kode Voucher Telah Kadaluarsa\nAnda Mendapatkan Harga Normal")
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif user["unvalid"] == 1 and invchr == user["vchr"] and timer < 2:
            print ("\nMaaf Kode Voucher Telah Digunakan\nAnda Mendapatkan Harga Normal")
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif invchr == "0":
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
        elif invchr != user["vchr"] and invchr != 0:
            print ("\nMaaf Kode Voucher Salah\nAnda Mendapatkan Harga Normal")
            c =int(user["token"]) - 60
            user["token"] = c
            print("        ================================================       ")
            print("        ===       Pembelian anda telah berhasil      ===~~~~~~~")
            print("        ================================================       ")
            print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
            print("        ===  Sisa Token anda = ", user["token"],"Token") 
def skn3():
    system("cls")
    if(int(user["token"]) < 140) :
        print("        ================================================       ")
        print("        ===          Token anda tidak cukup          ===       ")
        print("        ===     Silahkan Melakukan Top Up Kembali    ===       ")
        print("        ================================================       ")
        print("")
        print("")
        print("")
    else:
        c =int(user["token"]) - 140
        user["token"] = c
        print("        ================================================       ")
        print("                  Pembelian anda telah berhasil")
        print("        ================================================       ")
        print("        ===  Sisa Saldo anda = ","Rp.",user["emoney"])
        print("        ===  Sisa Token anda = ", user["token"],"Token") 


def check_time(ijam,imenit): 
    jam_ke_menit = ijam * 60 
    pukul = jam_ke_menit + imenit
    return pukul
    

#WELCOME
system("cls")
print("")
print("")
print("        ================================================       ")
print("        ===                VALORSHOP                 ===       ")
print("        ================================================       ")
print("")
print("")
loadan = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
for i in range(len(loadan)):
    time.sleep(0.2)
    sys.stdout.write("\r" + loadan[i % len(loadan)])
    sys.stdout.flush()
system("cls")
jam = datetime.now()
waktu = int(jam.strftime("%H"))
print (jam.strftime("[ TANGGAL = %d/%b/%Y ]      [ WAKTU = %H:%M:%S ]"))
while True :
    namein = input("Masukkan Username Anda : ")
    pinin = input("Masukkan PIN Anda : ")
    if namein == user["name"] and pinin == user["pin"]:
        print("        ================================================        ")
        print("                 Pin dan Username Anda Benar ")
        print("        ================================================        ")
        break
    else :
        print("        ================================================        ")
        print("                  Pin dan Username Anda Salah ")
        print("               Silahkan Masukkan PIN Anda Kembali")
        print("        ================================================        ")
        ulangpin()

usia = int(input("Masukkan Usia Anda : "))
if waktu >= 0 and waktu <= 10 and usia >= 0 and usia <= 17 :
    ktgr = "Dek"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 10 and waktu <= 15 and usia >= 0 and usia <= 17 :
    ktgr = "Dek"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 15 and waktu <= 18 and usia >= 0 and usia <= 17 :
    ktgr = "Dek"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 18 and waktu <= 24 and usia >= 0 and usia <= 17 :
    ktgr = "Dek"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 0 and waktu <= 10 and usia >= 17 and usia <= 25 :
    ktgr = "Kak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 10 and waktu <= 15 and usia >= 17 and usia <= 25 :
    ktgr = "Kak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 15 and waktu <= 18 and usia >= 17 and usia <= 25 :
    ktgr = "Kak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 18 and waktu <= 24 and usia >= 17 and usia <= 25 :
    ktgr = "Kak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 0 and waktu <= 10 and usia >= 25 and usia <= 50 :
    ktgr = "Pak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 10 and waktu <= 15 and usia >= 25 and usia <= 50 :
    ktgr = "Pak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 15 and waktu <= 18 and usia >= 25 and usia <= 50 :
    ktgr = "Pak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")
elif waktu >= 18 and waktu <= 24 and usia >= 25 and usia <= 50 :
    ktgr = "Pak"
    print("        ================================================        ")
    print("        Selamat Datang Di ValorShop", ktgr, user["name"])
    print("        Tempat Top Up dan beli Item game termurah ")
    print("        ================================================        ")

main()

