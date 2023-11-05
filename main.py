# Program <VendingManchine>
# Mensimulasikan kopi vending machine 

#KAMUS
# menu : dictionary
# L_menyu : list of string
# reso : dictionary
# report() : function
# ketersesidaan(pesanan_string) : function
# display_menu() : function
# update_menu(pesanan_string,menu_list) : function
# display_level(pesanan_angka,pesanan_string) : function
# display_pembayaran(pesanan_string) : function
# proses_pembuatan_kopi(pesanan_string) : function

# menyu_integer : integer
# menyu_string : string
# is_on : boolean
# availablity : boolean/string
# sudah_bayar : boolean
# pause : string
# menu_tambahan : list of integer

# ALGORITMA
menu = { 
    "Hot Kopi Gula Aren": {
        "bahan": {"air": 100,"es": 0,"susu": 100,"kopi": 15,"gula aren": 4,"coklat": 0,"gula": 0},
        "harga": 13000,
    },
    "Ice Kopi Gula Aren": {
        "bahan": {"air": 100,"es": 10,"susu": 100,"kopi": 15,"gula aren": 4,"coklat": 0,"gula": 0},
        "harga": 13000,
    },
    "Hot Americano": {
        "bahan": {"air": 100,"es": 0,"susu": 0,"kopi": 15,"gula aren": 0,"coklat": 0,"gula": 0},
        "harga": 13000,
    },
    "Ice Americano": {
        "bahan": {"air": 100,"es": 10,"susu": 0,"kopi": 15,"gula aren": 0,"coklat": 0,"gula": 0},
        "harga": 13000,
    },
    "Hot Cappunccino": {
        "bahan": {"air": 100,"es": 0,"susu": 100,"kopi": 15,"gula aren": 0,"coklat": 0,"gula": 4},
        "harga": 13000,
    },
    "Ice Cappunccino": {
        "bahan": {"air": 100,"es": 10,"susu": 100,"kopi": 15,"gula aren": 0,"coklat": 0,"gula": 4},
        "harga": 13000,
    },
    "Hot Dark Chocolate": {
        "bahan": {"air": 100,"es": 0,"susu": 100,"kopi": 0,"gula aren": 0,"coklat": 30,"gula": 0},
        "harga": 13000,
    },
    "Ice Dark Chocolate": {
        "bahan": {"air": 100,"es": 10,"susu": 100,"kopi": 0,"gula aren": 0,"coklat": 30,"gula": 0},
        "harga": 13000,
    },
    "Hot Kopi Hitam": {
        "bahan": {"air": 100,"es": 0,"susu": 0,"kopi": 15,"gula aren": 0,"coklat": 0,"gula": 4},
        "harga": 8000,
    },
    "Ice Kopi Hitam": {
        "bahan": {"air": 100,"es": 10,"susu": 0,"kopi": 15,"gula aren": 0,"coklat": 0,"gula": 4},
        "harga": 8000,
    },
    "Hot Kopi Susu": {
        "bahan": {"air": 100,"es": 0,"susu": 100,"kopi": 15,"gula aren": 0,"coklat": 0,"gula": 4},
        "harga": 8000,
    },
    "Ice Kopi Susu": {
        "bahan": {"air": 100,"es": 10,"susu": 100,"kopi": 15,"gula aren": 0,"coklat": 0,"gula": 4},
        "harga": 8000,
    }
}

#List menu dalam bentuk string
l_menyu = [
  'Hot Kopi Gula Aren','Ice Kopi Gula Aren',
  'Hot Americano','Ice Americano',
  'Hot Cappunccino','Ice Cappunccino', 
  'Hot Dark Chocolate','Ice Dark Chocolate',
  'Hot Kopi Hitam','Ice Kopi Hitam',
  'Hot Kopi Susu','Ice Kopi Susu'
]

#Bahan yang tersedia
reso = {
  "air": 300,
  "es": 50,
  "susu": 300,
  "kopi": 300,
  "gula aren": 24,
  "coklat": 100,
  "gula": 24
}

#saldo awal QRIS Rp300.000,00
saldo = {"uang" : 300000}
from inputimeout import inputimeout

#mendefinisikan fungsi untuk refill resource
def isiulang():
  #kamus lokal
  #isi : int
  #i : str
  #reso : dictionary
  for i in reso:
    isi=int(input(f"Masukkan jumlah {i} yang ingin diisi ulang: "))
    reso[i]+=isi
# mendefinisikan laporan dari sisa bahan atau menu 13 pada display menu
def report():    
  print(f"Available Resources:\n"
        f"Air: {reso['air']} ml \n"
        f"Aren: {reso['gula aren']} g \n"
        f"Coklat: {reso['coklat']} g \n"
        f"Es: {reso['es']} g \n"
        f"Gula {reso['gula']} g \n"
        f"Kopi: {reso['kopi']} g\n"
        f"Susu: {reso['susu']} ml \n")

# fungsi untuk memeriksa ketersediaan sisa bahan yang dibutuhkan untuk pembuatan kopi
def ketersediaan_reso(pesanan_string):
  for i in reso:    # untuk setiap bahan
    # jika bahan yang dibutuhkan untuk pembuatan lebih besar dari reso (bahan yang tersedia)
    if menu[pesanan_string]["bahan"][i] > reso[i]:   
      # output berupa bahan tidak tersedia
      return f"Maaf, pesanan tidak bisa dilakukan karena {i} tidak tersedia."  
  return True    # memecah loop

# fungsi untuk menunjukkan display dari menu ketika kode di run pertama kali
def display_menu(): 
  #kamus lokal
  #ketersediaan : array
  print("Vending Machine")    # output judul mesin
  ketersediaan = []    # kelas array untuk ketersediaan
  for i in menu:    # looping untuk menunjukkan stok dari setiap menu 
    if ketersediaan_reso(i) == True:     # jika ketersediaan dari menu benar
      ketersediaan.append("Tersedia")    # memasukkan string tersedia ke array untuk di keluarkan sebagai output
    else:
      ketersediaan.append('Habis')    # memasukkan string habis ke array untuk di keluarkan sebagai output

  print(f"""No  Menu                 Harga      Ketersediaan
1.  Hot Kopi Gula Aren   Rp 13000   {ketersediaan[0]}
2.  Ice Kopi Gula Aren   Rp 13000   {ketersediaan[1]}
3.  Hot Americano        Rp 13000   {ketersediaan[2]}
4.  Ice Americano        Rp 13000   {ketersediaan[3]}
5.  Hot Cappuccino       Rp 13000   {ketersediaan[4]}
6.  Ice Cappuccino       Rp 13000   {ketersediaan[5]}
7.  Hot Dark Chocolate   Rp 13000   {ketersediaan[6]}
8.  Ice Dark Chocolate   Rp 13000   {ketersediaan[7]}
9.  Hot Kopi Hitam       Rp 8000    {ketersediaan[8]}
10. Ice Kopi Hitam       Rp 8000    {ketersediaan[9]}
11. Hot Kopi Susu        Rp 8000    {ketersediaan[10]}
12. Ice Kopi Susu        Rp 8000    {ketersediaan[11]}
------------------------------------------------    
Pilihan lainnya:
13. Cek bahan yang tersedia
14. Staff Only
15. Exit""")

#fungsi update menu
def update_menu(pesanan_string,menu_list):
  #kamus lokal
  #menu_list : array
  #menu  : dictionary
  menu[pesanan_string]['bahan']['gula']+= menu_list[0] #gula yang digunakan akan ditambahkan sesuai dengan jumlah yang diinput
  menu[pesanan_string]['bahan']['gula aren']+=menu_list[1] #aren yang digunakan akan ditambahkan sesuai dengan jumlah yang diinput
  menu[pesanan_string]['bahan']['es']+=menu_list[2] #es yang digunakan akan ditambahkan sesuai dengan jumlah yang diinput

#fungsi display level
def display_level(pesanan_angka,pesanan_string): 
  #kamus lokal
  #level1_list, level1_list, menu_list, sugar_level, aren_level, ice_level  : array
  #level0, level1, level2 : int
  #availability : boolean, string
  #update_menu, ketersediaan_reso(pesanan_string) : function
  level1_list = ["","",""]       # inisialisasi array untuk level1_list
  menu_list = [4,0,0] #inisialisai array menu_list
  update_menu(pesanan_string,menu_list) #mengupdate menu dengan memsukkan isi dari menu_list
  availability = ketersediaan_reso(pesanan_string)
  if availability != True: #jika bahan tidak cukup
    level1_list[0] = "!" #pada display level akan muncul tanda ! sebagai penanda
  menu_list = [-4,0,0] #inisialisasi array akhir menu_list
  update_menu(pesanan_string,menu_list) #mengupdate menu dengan memsukkan isi dari menu_list

  menu_list = [0,4,0]
  update_menu(pesanan_string,menu_list)
  availability = ketersediaan_reso(pesanan_string)
  if availability != True: #jika bahan tidak cukup
    level1_list[1] = "!" #pada display level akan muncul tanda ! sebagai penanda
  menu_list = [0,-4,0] #inisialisasi array akhir menu_list
  update_menu(pesanan_string,menu_list) #mengupdate menu dengan memsukkan isi dari menu_list

  menu_list = [0,0,10]
  update_menu(pesanan_string,menu_list)
  availability = ketersediaan_reso(pesanan_string)
  if availability != True: #jika bahan tidak cukup
    level1_list[2] = "!" #pada display level akan muncul tanda ! sebagai penanda
  menu_list = [0,0,-10] #inisialisasi array akhir menu_list
  update_menu(pesanan_string,menu_list) #mengupdate menu dengan memsukkan isi dari menu_list

  level2_list = ["","",""] #inisialisasi array untuk level2_list
  menu_list = [8,0,0]
  update_menu(pesanan_string,menu_list)
  availability = ketersediaan_reso(pesanan_string)
  if availability != True: #jika bahan tidak cukup
    level2_list[0] = "!" #pada display level akan muncul tanda ! sebagai penanda
  menu_list = [-8,0,0] #inisialisasi array akhir menu_list
  update_menu(pesanan_string,menu_list) #mengupdate menu dengan memsukkan isi dari menu_list

  menu_list = [0,8,0]
  update_menu(pesanan_string,menu_list)
  availability = ketersediaan_reso(pesanan_string)
  if availability != True: #jika bahan tidak cukup
    level2_list[1] = "!" #pada display level akan muncul tanda ! sebagai penanda
  menu_list = [0,-8,0] #inisialisasi array akhir menu_list
  update_menu(pesanan_string,menu_list) #mengupdate menu dengan memsukkan isi dari menu_list

  menu_list = [0,0,20]
  update_menu(pesanan_string,menu_list)
  availability = ketersediaan_reso(pesanan_string)
  if availability != True: #jika bahan tidak cukup
    level2_list[2] = "!" #pada display level akan muncul tanda ! sebagai penanda
  menu_list = [0,0,-20] #inisialisasi array akhir menu_list
  update_menu(pesanan_string,menu_list) #mengupdate menu dengan memsukkan isi dari menu_list

  level0,level1,level2 = 0,0,0

  sugar_level = [0,4,8] #inisialisasi array sugar_level
  aren_level = [0,4,8] #inisialisasi array aren_level
  ice_level = [0,10,20] #inisialisasi array ice_level
  if pesanan_angka not in [1, 2, 3, 4, 7, 8]: #jika pesanan mengandung gula
    print(f"Pilih sugar level: [1] {level1_list[0]}[2] {level2_list[0]}[3]")
    level0 = int(input('Sugar Level: '))-1
  elif pesanan_angka in [1, 2]: #jika pesanan mengandung gula aren
    print(f"Pilih sugar level: [1] {level1_list[1]}[2] {level2_list[1]}[3]")
    level1 = int(input('Sugar Level: '))-1
  if pesanan_angka % 2 == 0: #jika pesanan mengandung es
    print(f"Pilih ice level: [1] {level1_list[2]}[2] {level2_list[2]}[3]")
    level2 = int(input('Ice Level: '))-1
  return [sugar_level[level0],aren_level[level1],ice_level[level2]]

#fungsi display pembayaran
def display_pembayaran(pesanan_string): #fungsi untuk pembayaran
  #kamus lokal
  #menu,saldo : dictionary
  #confirm : str
  print(f"""Harga yang harus anda bayar adalah : {menu[pesanan_string]["harga"]}
Silahkan scan QRIS dalam 30 detik""")
  try:

    #Input dengan batas waktu 30 detik
    confirm = inputimeout(prompt='Konfirmasi Bayar (Y/N): ', timeout=30)

  # Catch the timeout error
  except Exception:

    #Timeout
    confirm = 'Waktu Habis'
  if saldo["uang"]<menu[pesanan_string]["harga"]:
    confirm = 'Saldo tidak cukup'
  else: #jika saldo cukup
    saldo["uang"]-=menu[pesanan_string]["harga"]
  if confirm=='Y':
    return True
  elif confirm=='N':
    return False
  else: #confirm!+'Y' or confirm!='N'
    print(confirm)
    return confirm

#fungsi pembuatan kopi
def proses_pembuatan_kopi(pesanan_string): #fungsi untuk proses pengurangan bahan dari dictionary karena minuman dibuat
  #kamus lokal
  #menu,reso : dictionary
  #i : int
  for i in reso: #perulangan untuk mengurangi bahan dari dictionary
    reso[i] -= menu[pesanan_string]["bahan"][i]
#------------------------------------------------------------------------------------------------
#ALGORITMA
is_on = True
while is_on:
  display_menu()    # memanggil function display_menu untuk menunjukkan menu
  menyu_integer = int(input("Pilih nomor menu: "))    # meminta input pengguna untuk memilih menu yang diinginkan
  print()    # membuat pause
  match menyu_integer:      # menyocokkan menyu_integer dengan angka spesifik
    case 15: #keluar dari program
      print("Terima Kasih telah menggunakan Vending Machine")
      is_on = False
    case 14: #mode staff untuk isi ulang
      print('Staff Mode')
      pw=int(input('Masukkan sandi: '))
      if pw!=69420:
        print('Sandi salah')
        continue
      else: #pw==69420
        isiulang()
    case 13: #mengecek bahan yang tersedia
      report()
      pause = input()
    case _: # 1,2,3,4,5,6,7,8,9,10,11,12 , memesan kopi
      menyu_string = l_menyu[menyu_integer - 1] #mengubah bentuk integer menjadi string 
      availability = ketersediaan_reso(menyu_string)
      if availability != True:      # syarat ketika ketersediaan tidak ada
        print(availability)    # output kolom ketersediaan
        pause = input()      # membuat jeda supaya terbaca
        continue      
      menu_tambahan = display_level(menyu_integer,menyu_string) #display level and innput level
      update_menu(menyu_string,menu_tambahan) #mengupdate menu menjadi sesuai dengan yg diinginkan
      print()
      availability = ketersediaan_reso(menyu_string)      
      if availability != True:      # syarat ketika ketersediaan tidak ada
        print(availability)    # output kolom ketersediaan
        pause = input()      # membuat jeda supaya terbaca
        menu_tambahan = [-menu_tambahan[0],-menu_tambahan[1],-menu_tambahan[2]] #reset menu
        update_menu(menyu_string,menu_tambahan)      # memperbaharui menu menjadi sesuai yang diinginkan    
        continue
      sudah_bayar = display_pembayaran(menyu_string)    # mendefinisikan variabel sudah_bayar dengan memanggil function display_pembayaran
      if sudah_bayar != True:
        continue
      proses_pembuatan_kopi(menyu_string)      # memanggil function proses_pembuatan_kopi
      print(f'Silahkan nikmati {menyu_string} Anda.')    # output
      pause = input()    # membuat jeda supaya terbaca
      menu_tambahan = [-menu_tambahan[0],-menu_tambahan[1],-menu_tambahan[2]] #reset menu
      update_menu(menyu_string,menu_tambahan)    # memperbaharui menu
