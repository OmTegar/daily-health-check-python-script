import datetime
import sys
import time
import os

now=datetime.datetime.now()
os.system('cls')

def dhc():
    print('')
    print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                    Daily Health Check !...
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """)

dhc()

nama =input("""
                            +----------------------------------------------------------+
                             Username : """)
os.system('cls')

def security():
    keluar=int(input("klik 0 untuk keluar : "))
    if keluar==0:
        os.system('cls')
        print(exit())
        menu()
    else :
        print  ("""
                        ========================================================================
                        ======== WARNING : MASUKKAN INPUT JAWABAN YANG BENAR MASZEH !!! ========
                        ========================================================================
                                                                                            """)
        keluar=int(input("klik 0 untuk keluar : "))
        if keluar==0:
            os.system('cls')
            print(exit())
            menu()
        else:
            os.system('cls')
            print  ("""
                    ======================================================================================
                    =  ANDA TELAH KAMI KELUARKAN DARI SYSTEM KARENA TIDAK MEMATUHI PROTOCOL SYSTEM KAMI  =
                    ======================================================================================
                                                                                            """)
            print (off())

def off():
    dhc()
    print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                            terimakasih """,nama ,""" telah menggunakan layanan daily health check
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)
    print("")
    print("""
                    ============= copyright 2022 by Tegar Dito Priandika and Aisyatul Huriyah =============
                                                                                                                """)
    sys.exit()

def exit():
    dhc()
    print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                    terimakasih """,nama ,""" telah menggunakan fitur kami
                                              silahkan coba fitur lainya !!!
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)
    menu()
    
def keseimbangan():
    print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                Cek keseimbangan tubuh anda !...
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)

    tinggi=float(input("masukkan tinggi anda (cm) :"))
    berat=float(input("masukan berat anda (kg) : "))
    tinggi = tinggi/100
    penghitungan=berat/(tinggi*tinggi)
    print("massa tubuh anda : ",penghitungan)
    if(penghitungan>0):
        if(penghitungan<=16):
            print("")
            print("anda sangat kurus, perbanyak makan ya manis")
        elif(penghitungan<=18.5):
            print("")
            print("anda kurus, perbanyak makan ya manis")
        elif(penghitungan<=25):
            print("")
            print("hebat , kamu sehat , tetap jaga kesehatan ya")
        elif(penghitungan<=30):
            print("")
            print("kamu sedikit gendutan, tapi gapapa kok")
        else: print("kamu suka makan ya, tubuhmu sangat gendut")
    else:
        print("masukkan detail dengan benar !!!")
        print("perhatikan kalender hari ini , dan lakukan penghitungan kembali lain waktu")
        print("")

    
    print ("Waktu lokal saat ini :", now)

def kalori():
    print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                          Cek kalori yang terbakar setelah berjalan !...
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)

    berat = int(input("Masukkan Berat Badan Anda Dalam KG : \n"))
    tinggi = int(input("Masukkan Tinggi Anda Dalam cm : \n"))
    umur = int(input("Masukkan Umur Anda : \n"))
    cowo = str(input("Apakah Anda Seorang Lelaki? (y/n) :"))

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
            KALORI YANG TERBAKAR :''',cal                                    
                                        )

def diabetes():
    print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                           TEST DIABETES !...
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)

    print(      
        "Jawablah Pertanyaan berikut agar program dapat memulai akumulasi apakah anda terkena penyakit diabetes! "
    )
    print('''
                                    +----------------------------------------------------------+
                                    |                      pertanyaan 1                        |
                                    |                  BERAPAKAH UMUR ANDA ?                   |
                                    +----------------------------------------------------------+
                                    | 1. Di bawah 40 Tahun                                     | 
                                    +----------------------------------------------------------+
                                    | 2. Di Antara 40-49 Tahun                                 |
                                    +----------------------------------------------------------+
                                    | 3. Di Atas 60 Tahun                                      | 
                                    +----------------------------------------------------------+
                                                                                                ''')
    jawaban_1=int(input("silahkan jawab pertanyaan pertama (1/2/3) ? : "))
    if jawaban_1==1:
        jawaban_1=0
    if jawaban_1==2:
        jawaban_1=1
    if jawaban_1==3:
        jawaban_1=3

    print('''
                                    +----------------------------------------------------------+
                                    |                      pertanyaan 2                        |
                                    |                 MASUKKAN GENDER ANDA ?                   |
                                    +----------------------------------------------------------+
                                    | 1. PRIA / LAKI-LAKI                                      | 
                                    +----------------------------------------------------------+
                                    | 2. WANITA / PEREMPUAN                                    |
                                    +----------------------------------------------------------+
                                                                                                ''')
    jawaban_2=int(input("silahkan jawab pertanyaan ke dua (1/2) ? : "))
    if jawaban_2==1:
        jawaban_2=1
    if jawaban_2==2:
        jawaban_2=0

    print('''
                                    +----------------------------------------------------------+
                                    |                      pertanyaan 3                        |
                                    |   APAKAH ADA ANGGOTA KELUARGA YANG MENGIDAP DIABETES ?   |
                                    +----------------------------------------------------------+
                                    | 1. YA                                                    | 
                                    +----------------------------------------------------------+
                                    | 2. TIDAK                                                 |
                                    +----------------------------------------------------------+
                                                                                                ''')
    jawaban_3=int(input("silahkan jawab pertanyaan ke tiga (1/2) ? : "))
    if jawaban_3==1:
        jawaban_3=1
    if jawaban_3==2:
        jawaban_3=0

    print('''
                                    +----------------------------------------------------------+
                                    |                      pertanyaan 4                        |
                                    |       APAKAH ANDA MEMILIKI TEKANAN DARAH TINGGI ?        |
                                    +----------------------------------------------------------+
                                    | 1. YA                                                    | 
                                    +----------------------------------------------------------+
                                    | 2. TIDAK                                                 |
                                    +----------------------------------------------------------+
                                                                                                ''')
    jawaban_4=int(input("silahkan jawab pertanyaan ke empat (1/2) ? : "))
    if jawaban_4==1:
        jawaban_4=1
    if jawaban_4==2:
        jawaban_4=0

    print('''
                                    +----------------------------------------------------------+
                                    |                      pertanyaan 5                        |
                                    |      APAKAH ANDA KELEBIHAN BERAT BADAN /OBESITAS ?       |
                                    +----------------------------------------------------------+
                                    | 1. NORMAL                                                | 
                                    +----------------------------------------------------------+
                                    | 2. SEDIKIT GENDUT                                        |
                                    +----------------------------------------------------------+
                                    | 3. OBESITAS / KELEBIHAN BERAT BADAN                      |
                                    +----------------------------------------------------------+
                                                                                                ''')
    jawaban_5=int(input("silahkan jawab pertanyaan ke lima (1/2/3) ? : "))
    if jawaban_5==1:
        jawaban_5=0
    if jawaban_5==2:
        jawaban_5=1
    if jawaban_5==2:
        jawaban_5=2

    print('''
                                    +----------------------------------------------------------+
                                    |                      pertanyaan 6                        |
                                    |              APAKAH ANDA AKTIF SECARA FISIK ?            |
                                    +----------------------------------------------------------+
                                    | 1. YA                                                    | 
                                    +----------------------------------------------------------+
                                    | 2. TIDAK                                                 |
                                    +----------------------------------------------------------+
                                                                                                ''')
    jawaban_6=int(input("silahkan jawab pertanyaan ke enam (1/2) ? : "))
    if jawaban_6==1:
        jawaban_6=0
    if jawaban_6==2:
        jawaban_6=1

    akumulasi=(jawaban_1 + jawaban_2 + jawaban_3 + jawaban_4 + jawaban_5 + jawaban_6)

    if(akumulasi<=3):
        print("ANDA BERKEMUNGKINAN RENDAH TERKENA DIABETES ...")
    elif (akumulasi==3):
        print("ANDA BERKEMUNGKINAN TERKENA DIABETES DENGAN PERBANDINGAN 1/2 ...")
    elif (akumulasi<=6):
        print("ANDA BERKEMUNGKINAN TERKENA DIABETES DENGAN PERBANDINGAN LEBIH DARI 50% ...")
    else : print ("ANDA KAMI KAMI ANGGAP TERKENA DIABETES , SEGERA LAKUKAN PENGECEKKAN DI TENAGA MEDIS TERDEKAT")

def pernapasan():
    print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                    Cek Pernapasan Sederhana !...
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)
    print("Selamat Datang di Tes Pernafasan Sederhana :) ")
    print("Untuk memulai, Silahkan lakukan langkah-langkah berikut:")
    print("1. Duduk dan tarik napas selama 3 kali berturut-turut dan buanglah secara perlahan.")
    print("2. Kemudian, tarik nafas dan tahan selama yang kamu bisa sambil menekan stopwatch.")

    def stopwatch():
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                          STOPWATCH AKAN BERJALAN SETELAH CLICK ENTER !...
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """) 
        print  ("""
                                        ===================================================
                                        ====== WARNING : HARAP LAKUKAN SEKUAT ANDA!!! =====
                                        ===================================================
                                                                                                """)  
        def time_convert(sec):
            mins = sec // 60
            sec = sec % 60
            hours = mins // 60
            mins = mins % 60
            print("lama bertahan = {0}:{1}:{2}".format(int(hours),int(mins),sec))
    
        input("TEKAN ENTER UNTUK MEMULAI")
        start_time = time.time()

        input("TEKAN ENTER UNTUK BERHENTI")
        end_time = time.time()

        time_lapsed = end_time - start_time
        time_convert(time_lapsed)


    stopwatch()
    print("perhatikan data di atas, data tersebut memiliki format [jam : menit : detik]")
    napas = int(input("Silahkan Masukkan berapa detik anda dapat menahan Nafas : "))
    if (napas <= 40) :
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                        Sistem kerja pernafasan Anda tidak terlalu bagus
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """)
        print  ("""
                        ========================================================================
                        ====== WARNING : Segeralah ke Dokter untuk Periksa lebih lanjut!!! =====
                        ========================================================================
                                                                                                """)
    elif (napas >= 40 and napas <= 49) :
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                Sistem kerja pernafasan Anda normal
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """)
    elif (napas >= 50 and napas <= 60) :
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                        Sistem kerja pernafasan Anda Sangat Bagus
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """)
    else :
        print  ("""
                                    ===================================================
                                    ======  WARNING : HASIL ANDA TIDAK VALID !!!  =====
                                    ===================================================
                                                                                                """) 

def denyut():
    print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                    Cek Denyut Jantung !...
                                            Selamat Datang di Tes Denyut Jantung :
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)
    print("  ")
    print("Untuk memulai, Silahkan lakukan langkah-langkah berikut:")
    print("1. Letakkan bantalan jari tengah dan jari telunjuk pada pergelangan tangan atau di leher (sisi tenggorokan)")
    print("2. Tekan dengan lembut sampai anda menemukan denyut nadi")


    def countdownTimer(start_minute, start_second):
        total_second = start_minute * 60 + start_second
        while total_second:
            mins, secs = divmod(total_second, 60)
            print(f'{mins:02d}:{secs:02d}', end='\r')
            time.sleep(1)
            total_second -= 1
        print("waktu telah selesai!")
    stopwatch=input(("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                            STOPWATCH AKAN BERJALAN SETELAH CLICK ENTER !...
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """))
    stopwatch==countdownTimer(00, 10)


    print("   ")
    hasil = int(input("Silahkan Masukkan banyak nadi yang terhitung: "))
    
    denyut = (hasil * 6)

    if (denyut<=60):
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                            Denyut nadi Anda sangat Lambat
                                            Detak denyut nadi anda: """, denyut, """bpm
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """)
    elif (denyut<=85):
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                            Denyut nadi Anda Normal
                                             Detak denyut nadi anda: """, denyut, """bpm
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """)
    elif (denyut <= 100 ) :
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                            Denyut nadi Anda sedikit lebih cepat
                                            Detak denyut nadi anda: """, denyut, """bpm
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """)
    elif (denyut >=100) :
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                            Denyut nadi Anda sangat Cepat
                                            Detak denyut nadi anda: """, denyut, """bpm
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                        """)
        print  ("""
                        ========================================================================
                        ==== WARNING : Silahkan hubungi Dokter untuk periksa lebih lanjut!!! ===
                        ========================================================================
                                                                                                """)
    else :
        print  ("""
                        ========================================================================
                        ====         WARNING : Silahkan hitung kembali denyut nadi anda      ===
                        ========================================================================
                                                                                                """)

def menu():
    print('''
                                +----------------------------------------------------------+
                                |                 Fitur yang Tersedia                      |
                                +----------------------------------------------------------+
                                | 1. Cek keseimbangan tubuh anda                           | 
                                +----------------------------------------------------------+
                                | 2. Cek kalori yang terbakar setelah berjalan             |
                                +----------------------------------------------------------+
                                | 3. Cek Apakah Anda Berkemungkinan Terkena Diabetes       | 
                                +----------------------------------------------------------+
                                | 4. Cek Kesehatan Sistem Pernapasan                       | 
                                +----------------------------------------------------------+
                                | 5. Cek Denyut Nadi                                       | 
                                +----------------------------------------------------------+
                                | 6. Exit                                                  | 
                                +----------------------------------------------------------+
                                                                                                ''')
    pilihan=int(input("pilihlah fitur yang anda mau dengan menginputkan nomor fitur tersebut (1/2/3/4/5/6) ? : "))
    if pilihan==1:
        os.system('cls')
        print(keseimbangan())
        security()
    if pilihan==2:
        os.system('cls')
        print(kalori())
        security()
    if pilihan==3:
        os.system('cls')
        print(diabetes())
        security()
    if pilihan==4:
        os.system('cls')
        print(pernapasan())
        security()
    if pilihan==5:
        os.system('cls')
        print(denyut())
        security()
    if pilihan==6:
        os.system('cls')
        print(off())

def intro():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<11:
        os.system('cls')
        dhc()
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        Selamat pagi, hai """,nama ,""" Selamat Datang Di Layanan Daily Health check
                                        Silahkan Nikmati Layanan Yang Kami Berikan !!!
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)
        menu()

    elif hour>=11 and hour<15:
        os.system('cls')
        dhc()
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                         Selamat siang, hai """,nama ,""" Selamat Datang Di Layanan Daily Health check
                                          Silahkan Nikmati Layanan Yang Kami Berikan !!!
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """) 
        menu()
    
    elif hour>=15 and hour<18:
        os.system('cls')
        dhc()
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                          Selamat sore, hai """,nama ,""" Selamat Datang Di Layanan Daily Health check
                                          Silahkan Nikmati Layanan Yang Kami Berikan !!!
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)
        menu()

    else:
        os.system('cls')
        dhc()
        print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                         Selamat malam, hai """,nama ,""" Selamat Datang Di Layanan Daily Health check
                                          Silahkan Nikmati Layanan Yang Kami Berikan !!!
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)
        menu()

intro()