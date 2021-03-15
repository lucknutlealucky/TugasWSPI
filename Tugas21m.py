def ukurNilai (val) :
    kriteria = ""
    if val >= 88 :
        kriteria = "A"
    if val >= 77 and val < 88 :
        kriteria = "B"
    if val >= 60 and val < 77 :
        kriteria = "C"
    if val >= 45 and val < 60 :
        kriteria = "D"
    if val < 45 :
        kriteria = "E"
    return kriteria