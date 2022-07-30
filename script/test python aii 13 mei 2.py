import time

print("""
                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                    Cek Denyut Jantung !...
                                            Selamat Datang di Tes Denyut Jantung :
                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                     """)
print("  ")
print("Untuk memulai, Silahkan lakukan langkah-langkah berikut:")
print("1. Letakkan bantalan jari tengah dan jari telunjuk pada pergelangan tangan dan di leher (sisi tenggorokan)")
print("2. Tekan dengan lembut sampai anda menemukan denyut nadi")


def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
    print("waktu telah selesai!")
stopwatch=input("klik enter untuk memulai")
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