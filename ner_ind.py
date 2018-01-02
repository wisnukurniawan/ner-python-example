# coding=utf-8
import ner_core
import utils

sentence = """Perubahan ini disebut bisa meredam konflik antara Kalanick dengan salah satu investor mereka, yaitu Benchmark.
Selama ini, Kalanick mempunyai hak voting ekstra. Hal ini membuat ia bisa menunjuk dua anggota direksi baru tanpa mengabarkan CEO Uber Dara Khosrowshahi dan anggota direksi lainnya.
Langkah Uber masuk bursa saham akan menjadi salah satu proses IPO perusahaan teknologi yang terbesar hingga saat ini. 
Hal ini pun bisa menjadi semacam pembuktian apakah startup teknologi besar bisa tetap sukses setelah mereka masuk 
bursa saham atau tidak."""

if __name__ == '__main__':
    ner = ner_core.NerCore(sentence)

    names = ner.extract_names("ind")
    locations = ner.extract_location("ind")
    dates = ner.extract_date_time()

    print("==============================")
    print("Hasil extract data (Indonesia)")
    print("========================")
    print("Nama")
    print("====================")
    utils.get_result(names)

    print
    print("========================")
    print("Lokasi")
    print("====================")
    utils.get_result(locations)

    print
    print("========================")
    print("Tanggal")
    print("====================")
    utils.get_result(dates)


