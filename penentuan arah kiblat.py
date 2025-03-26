import math

# Koordinat geografis
Bujur_Kabah = 39.82616111  # Ba
Bujur_Mesjit = 97.150556  # Bb
Lintang_Kabah = 21.42250833  # La
Lintang_Mesjit = 5.125833 # Lb

# Perhitungan
selisih_bujur = Bujur_Kabah - Bujur_Mesjit  # Ba - Bb
sin_selisih_bujur = math.sin(math.radians(selisih_bujur))
cos_selisih_bujur = math.cos(math.radians(selisih_bujur))
sin_lintang_Mesjit = math.sin(math.radians(Lintang_Mesjit))
cos_lintang_Mesjit = math.cos(math.radians(Lintang_Mesjit))
tan_lintang_kabah = math.tan(math.radians(Lintang_Kabah))

# Hitung tan(B)
numerator = sin_selisih_bujur
denominator = cos_lintang_Mesjit * tan_lintang_kabah - sin_lintang_Mesjit * cos_selisih_bujur
tan_B = numerator / denominator

# Hitung sudut B dalam derajat
B = math.degrees(math.atan(tan_B))

# Konversi ke azimuth 0°-360°
if B < 0:
    azimuth_kiblat = 360 + B
else:
    azimuth_kiblat = B

# Konversi ke derajat, menit, detik
derajat = int(azimuth_kiblat)
sisa = (azimuth_kiblat - derajat) * 60
menit = int(sisa)
detik = (sisa - menit) * 60

# Output hasil
print(f"Ba - Bb = {selisih_bujur:.8f} derajat")
print(f"Sin(Ba - Bb) = {sin_selisih_bujur:.8f}")
print(f"Cos(Ba - Bb) = {cos_selisih_bujur:.8f}")
print(f"Sin(Lb) = {sin_lintang_Mesjit:.8f}")
print(f"Cos(Lb) = {cos_lintang_Mesjit:.8f}")
print(f"Tan(La) = {tan_lintang_kabah:.8f}")
print(f"Tan(B) = {tan_B:.8f}")
print(f"Azimuth arah kiblat = {azimuth_kiblat:.8f} derajat")
print(f"Arah kiblat = {derajat}° {menit}' {detik:.2f}""")
