import datetime
now=datetime.datetime.now()

berat = int(input("Masukkan Berat Badan Anda Dalam KG : \n"))
tinggi = int(input("Masukkan Tinggi Anda Dalam cm : \n"))
umur = int(input("Masukkan Umur Anda : \n"))
cowo = str(input("Apakah Anda Seorang Lelaki? (y/n)"))

if cowo == "y":
    cowo = True
elif cowo == "n":
    cowo = False
else:
    print("Error input jawaban anda dengan (y/n)")
    quit()
    
if cowo:
    bmr = 66.5 + (13.75 * berat) + (5 * tinggi) - (6.755 * umur)
else:
    bmr = 655.1 + (9.6 * berat) + (1.8 * tinggi) - (4.7 * umur)

bmr = round(bmr)
print(bmr)

print("Masukkan kecepatan rata rata anda berjalan !")        
speed=float(input("kecepatan Berjalan Dalam (km/h) : "))
a=3.2
b=4.0
c=4.8
d=5.6
e=6.4
f=7.2
g=8.0
if speed<=a:
    mets=2.0
if speed==a:
     mets=2.8
if speed==b:
    mets=3.0
if speed==c:
     mets=3.5
if speed==d:
    mets=4.3
if speed==e:
    mets=5.0
if speed==f:
    mets=7.0
if speed==g:
    mets=8.3

if speed==a:
    mets=2.8
    mets = (speed, b, c, d, e, f, g)
print("Masukkan Berapa Lama anda Berjalan")


dur=int(input(" Masukkan kecepatan (dalam jam): "))
print("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            SEKARANG MENGHITUNG BERAPA BANYAK KALORI YANG ANDA BAKAR!.......
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                                                      """)
'''engine.say("Sekarang menghitung berapa banyak kalori yang anda bakar")
engine.runAndWait()'''
print("Menghitung kalori yang anda bakar")
cal=bmr*mets/24*dur
print("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     SELAMAT ANDA MEMBAKAR TOTAL KALORI  : """,cal,"calories","""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                                     """)

        
print("LANJUTKAN KERJA BAIK MU ;) ")   
print("BERIKUT ADALAH DATA BERJALAN ANDA? ")
print('''             DATA AKAN DI MASUKKAN SEBAGAI BERIKUT:
                                                                                ''')
print('''
        TANGGAL MEMASUKKAN DATA :''',now
                                                                                )
print('''
        KECEPATAN BERJALAN : ''',speed
                                                                    )
print('''
        DURASI BERJALAN :''',dur
                                                                        )
print('''
        KALORI TERBAKAR :''',cal                                    )