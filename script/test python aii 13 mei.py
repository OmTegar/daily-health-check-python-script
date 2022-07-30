print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                    Cek Pernapasan Sederhana !...
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)
print("Selamat Datang di Tes Pernafasan Sederhana :) ")
print("Untuk memulai, Silahkan lakukan langkah-langkah berikut:")
print("1. Duduk dan tarik napas selama 3 kali berturut-turut tanpa membuangnya.")
print("2. Kemudian, tahan napas selama yang bisa kamu tahan sambil menekan stopwatch.")

def stopwatch():
    import time
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