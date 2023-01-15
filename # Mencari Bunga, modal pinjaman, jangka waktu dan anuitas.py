# -------------Mencari Bunga dengan Anuitas --------------
from typing import Any
import  math



An = float(input("masukan nilai An( An lebih besar dari Am): "))
Am = float(input("masukan nilai Am( Am lebih kecil dari An): "))
m1 = int( input("masukan nilai m ( m lebih kecil dari n): "))
n1 = int(input("masukan nilai n( n lebih besar dari m): "))
i = float(input("masukan presentase bunga: "))
hitungan1 = (An / Am) ** (1/(n1 - m1))
hitungan2 = hitungan1 - 1
if i == 0 :
    print("-----Mencari Bunga -----")
    print ("i =",hitungan2)
    # MENCARI ANUITAS 
    print("MENCARI ANUITAS : ")
    Ax = float(input("masukan nilai Ax ( Ax lebih kecil dari nilai Ax): "))
    y = int(input("masukan nilai y ( y lebih besar dari x): "))
    x = int(input("masukan nilai x ( x lebih kecil dari y): "))
    by = float(input("masukan besaran bunga pada tahun y: "))
    hitungan_anuitas1 = (1+ hitungan2)
    hitungan_anuitas2 = (y-x)
    hitungan_anuitas3 = hitungan_anuitas1 ** hitungan_anuitas2
    hitungan_anuitas4 = (Ax * hitungan_anuitas3)
    hitungan_anuitas_FINAL = (hitungan_anuitas4 + by)
    print("angsuran pokok bulan : ",y,"=",hitungan_anuitas4)
    print("Jumlah Anuitas: ", hitungan_anuitas_FINAL)
    # MENCARI ANGSURAN POKOK PERTAMA DAN BESARAN BUNGA PERTAMA
    print("-----Mencari Angsuran Pokok Pertama dan Besaran Bunga Pertama---------")
    hitungan_angsuran_AWAL = (1 + hitungan2) ** (1 - x)
    hitungan_angsuran_AWAL2 = Ax * hitungan_angsuran_AWAL
    print("Angsuran pokok awal : ", hitungan_angsuran_AWAL2)
    print( "Besaran Bunga pertama :" ,round(hitungan_anuitas_FINAL - hitungan_angsuran_AWAL2))
    # MENCARI MODAL AWAL PINJAMAN
    print("-------Mencari Modal Awal-----------")
    print("Nilai modal awal: "), print(round((hitungan_anuitas_FINAL - hitungan_angsuran_AWAL2) / hitungan2))
    hitungan_jangkaWAKTU = (round((hitungan_anuitas_FINAL - hitungan_angsuran_AWAL2) / hitungan2))
    hitungan_jangkaWAKTU2 = hitungan_jangkaWAKTU / hitungan_anuitas_FINAL
    hitungan_jangkaWAKTU3 =  hitungan_jangkaWAKTU2 * hitungan2
    hitungan_jangkaWAKTU4 = 1 - hitungan_jangkaWAKTU3
    hitungan_jangkaWAKTU5 = math.log(hitungan_jangkaWAKTU4)
    hitungan_jangkaWAKTU6 = math.log(hitungan1)
    hitungan_jangkaWAKTU7 = hitungan_jangkaWAKTU5 / hitungan_jangkaWAKTU6
    print("Jangka waktu : "),print(round(hitungan_jangkaWAKTU7 * -1))
     
    
    
    
    