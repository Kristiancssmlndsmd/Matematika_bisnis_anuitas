# ---------------------- ANUITAS BIASA ----------------------
modal_awal = input("masukan nilai modal awal: ")
modal_awal = float(modal_awal)
i = input("masukan nilai I: ")
i = float(i)
n = input("masukan nilai: n: ")
n = int(n)
a = input("masukan nilai a: ")
a = float(a)
hasil_hitungan = a *((1 -(1 + i)** -n)) / i

hasil_hitungan_2 =  (1 + i)
hasil_hitungan_3 = hasil_hitungan_2 ** -n
hasil_hitungan_4 = 1 - hasil_hitungan_3
hasil_hitungan_5 = hasil_hitungan_4 / i
hasil_hitungan_6 = modal_awal / hasil_hitungan_5
if modal_awal == 0:
    print(hasil_hitungan)
elif a == 0:
    print("Anuitas: ","Rp",hasil_hitungan_6)
    print("Anuitas: ","Rp",hasil_hitungan_6,"*",n,"=","total uang yang dibayar","Rp",
          hasil_hitungan_6 * n)

