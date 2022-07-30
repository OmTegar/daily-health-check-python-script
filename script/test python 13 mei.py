print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                           TEST DIABETS !...
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
