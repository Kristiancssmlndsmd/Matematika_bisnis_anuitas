#    PERUBAHAN ANUITAS SAMPAI 3 KALI
modal_awal = input("masukan nilai modal: ")
modal_awal = int(modal_awal)
i = input("masukan nilai i atau bunga awal: ")
i = float(i)
r = input("masukan nilai r atau bunga kedua: ")
r = float(r)
s = input("masukan nilai s atau bunga ketiga: ")
s = float(s)
a = input("masukan nilai anuitas: ")
a = float(a)
n1 = input("masukan berapa tahun bunga pertama?: ")
n1 = int(n1)
n2 = input("masukan berapa tahun bunga kedua?: ")
n2 = int(n2)
n3 = input("masukan berapa tahun bunga ketiga?: ")
n3 = int(n3)
# UNTUK PERUBAHAN 2 KALI
# ----- TAHAP AWAL -----------
hasil_hitungan1 = (1+i)
hasil_hitungan2 = hasil_hitungan1 ** -n1
hasil_hitungan3 = 1 - hasil_hitungan2
hasil_hitungan4 = hasil_hitungan3 / i
#------ TAHAP KEDUA ---------
hasil_hitungan5 = 1+r
hasil_hitungan6 = hasil_hitungan5 ** -n2
hasil_hitungan7 = 1 - hasil_hitungan6
hasil_hitungan8 = hasil_hitungan7 / r
# ------ TAHAP KETIGA ---------
hasil_hitungan9 = (1 + i) ** -n1
#--------- Pengganbungan Tahap 3 dan 2
hasil_hitungan10 = hasil_hitungan8 * hasil_hitungan9    
hasil_hitungan11 = hasil_hitungan10 + hasil_hitungan4
hasil_hitungan12 = modal_awal / hasil_hitungan11
# UNTUK PERUBAHAN 3 KALI
# Untuk Perubahan S
hasil_hitungan13 = 1 + s
hasil_hitungan14 = hasil_hitungan13 ** -n3
hasil_hitungan15 = 1 - hasil_hitungan14
hasil_hitungan16 = hasil_hitungan15 / s
# Untuk R ( i sudah dihitung pada hitungan 9)
hasil_hitungan17 = (1 + r) ** -n2
# Penggabungan Anuitas 3 kali
hasil_hitungan18 = hasil_hitungan16 * hasil_hitungan17
hasil_hitungan19 = hasil_hitungan18 * hasil_hitungan9
hasil_hitungan20 = hasil_hitungan11 + hasil_hitungan19
hasil_hitungan21 = modal_awal / hasil_hitungan20
if a == 0:
    print("TAHAPAN PERTAMA")
    print(1,"+",i,"=", hasil_hitungan1)
    print(hasil_hitungan1,"**",-n1,"=",hasil_hitungan2)
    print(1,"-",hasil_hitungan2)
    print(hasil_hitungan3,"/",i, "=", hasil_hitungan4 )
    print("TAHAPAN KEDUA")
    print( 1,"+",r,"=", hasil_hitungan5)
    print(hasil_hitungan5,"**",-n2,"=",hasil_hitungan6)
    print(1,"-",hasil_hitungan6,"=", hasil_hitungan7)
    print(hasil_hitungan7,"/",r,"=", hasil_hitungan8)
    print("TAHAPAN KETIGA")
    print(1,"+",i,"=", hasil_hitungan1)
    print(hasil_hitungan1,"**", -n1,"=", hasil_hitungan9)
    print("PENGGABUNGAN")
    print("Perhitungan bunga kedua: ",hasil_hitungan8,"*",hasil_hitungan9,"=", hasil_hitungan10 )
    print( "Perhitungan bunga pertama ditambah bunga kedua:",hasil_hitungan10,"+"
          ,hasil_hitungan4,"=", hasil_hitungan11)
    print("MENGHITUNG BUNGA KETIGA")
    print(hasil_hitungan13,"**", -n3,"=",hasil_hitungan14)
    print(1,"-", hasil_hitungan14,"=", hasil_hitungan15)
    print(hasil_hitungan15,"/",s,"=", hasil_hitungan16)
    print(hasil_hitungan5, "**", -n2, "=", hasil_hitungan6)
    print("PENGGABUNGAN BUNGA PERTAMA KETIGA DAN KEDUA")
    print( hasil_hitungan16,"*",hasil_hitungan17,"=", hasil_hitungan18)
    print(hasil_hitungan18 ,"*", hasil_hitungan9,"=", hasil_hitungan19)
    print( hasil_hitungan11,"+",hasil_hitungan19,"=", hasil_hitungan20)
    print(modal_awal,"/", hasil_hitungan20,)
    print("ANUITAS =","Rp",hasil_hitungan21)
    print("TOTAL YANG DIBAYARKAN","Rp", hasil_hitungan21 * ( n1 + n2 + n3))
elif modal_awal == 0 and a > 0:
    print("TAHAPAN PERTAMA")
    print(1,"+",i,"=", hasil_hitungan1)
    print(hasil_hitungan1,"**",-n1,"=",hasil_hitungan2)
    print(1,"-",hasil_hitungan2)
    print(hasil_hitungan3,"/",i, "=", hasil_hitungan4 )
    print("TAHAPAN KEDUA")
    print( 1,"+",r,"=", hasil_hitungan5)
    print(hasil_hitungan5,"**",-n2,"=",hasil_hitungan6)
    print(1,"-",hasil_hitungan6,"=", hasil_hitungan7)
    print(hasil_hitungan7,"/",r,"=", hasil_hitungan8)
    print("TAHAPAN KETIGA")
    print(1,"+",i,"=", hasil_hitungan1)
    print(hasil_hitungan1,"**", -n1,"=", hasil_hitungan9)
    print("PENGGABUNGAN")
    print("Perhitungan bunga kedua: ",hasil_hitungan8,"*",hasil_hitungan9,"=", hasil_hitungan10 )
    print( "Perhitungan bunga pertama ditambah bunga kedua:",hasil_hitungan10,"+"
          ,hasil_hitungan4,"=", hasil_hitungan11)
    print("MENGHITUNG BUNGA KETIGA")
    print(hasil_hitungan13,"**", -n3,"=",hasil_hitungan14)
    print(1,"-", hasil_hitungan14,"=", hasil_hitungan15)
    print(hasil_hitungan15,"/",s,"=", hasil_hitungan16)
    print(hasil_hitungan5, "**", -n2, "=", hasil_hitungan6)
    print("PENGGABUNGAN BUNGA PERTAMA KETIGA DAN KEDUA")
    print( hasil_hitungan16,"*",hasil_hitungan17,"=", hasil_hitungan18)
    print(hasil_hitungan18 ,"*", hasil_hitungan9,"=", hasil_hitungan19)
    print( hasil_hitungan11,"+",hasil_hitungan19,"=", hasil_hitungan20)
    print("MODAL AWAL : ", hasil_hitungan20,"*",a, "=","Rp",hasil_hitungan20 * a)

        