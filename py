S1 = float(input("1. Sınav Notunu Giriniz: "))
S2 = float(input("2. Sınav Notunu Giriniz: "))
P1 = float(input("1. Performans Notunu Giriniz: "))

ort = (S1 + S2 + P1) / 3

if ort == 0:
sonuç = "olumsuz"

elif ort >= 85:
sonuç = "Pek iyi"

elif ort >= 70:
sonuç = "Iyi"

elif ort >= 55:
sonuç = "Orta"

elif ort >= 40:
sonuç = "Gecer"

else:
sonuç = "Başarısız"

print(f"Ortalama: {ort:.2f}")
print(f"Degerlendirme: {conclusion}")
