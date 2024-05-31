def findMin(x, y):
  """Mencari nilai minimum dari dua angka."""
  if x <= y:
    return x
  else:
    return y


def kecepatanLambat(kecepatan):
  """Menghitung derajat keanggotaan kecepatan lambat."""
  if kecepatan <= 1000:
    return 1
  elif kecepatan > 1000 and kecepatan < 5000:
    return (5000 - kecepatan) / (5000 - 1000)
  else:
    return 0


def kecepatanCepat(kecepatan):
  """Menghitung derajat keanggotaan kecepatan cepat."""
  if kecepatan >= 5000:
    return 1
  elif kecepatan > 1000 and kecepatan < 5000:
    return (kecepatan - 1000) / (5000 - 1000)
  else:
    return 0


def suhuRendah(suhu):
  """Menghitung derajat keanggotaan suhu rendah."""
  if suhu <= 100:
    return 1
  elif suhu > 100 and suhu < 600:
    return (600 - suhu) / 500
  else:
    return 0


def suhuTinggi(suhu):
  """Menghitung derajat keanggotaan suhu tinggi."""
  if suhu >= 600:
    return 1
  elif suhu > 100 and suhu < 600:
    return (suhu - 100) / 500
  else:
    return 0


def sumberPrekuensiKecil(alfa):
  """Menghitung frekuensi kecil berdasarkan derajat keanggotaan."""
  if alfa > 0 and alfa < 1:
    return (7000 - alfa * 5000)
  elif alfa == 1:
    return 2000
  else:
    return 7000


def sumberPrekuensiBesar(alfa):
  """Menghitung frekuensi besar berdasarkan derajat keanggotaan."""
  if alfa > 0 and alfa < 1:
    return (2000 + alfa * 5000)
  elif alfa == 1:
    return 7000
  else:
    return 2000


def aturan(kecepatan, suhu):
  """Menerapkan aturan fuzzy berdasarkan input kecepatan dan suhu."""
  alfa = [0, 0, 0, 0]
  z = [0, 0, 0, 0]
  # Aturan 1: Jika kecepatan LAMBAT dan suhu TINGGI, maka frekuensi KECIL
  alfa[0] = findMin(kecepatanLambat(kecepatan), suhuTinggi(suhu))
  z[0] = sumberPrekuensiKecil(alfa[0])
  # Aturan 2: Jika kecepatan LAMBAT dan suhu RENDAH, maka frekuensi KECIL
  alfa[1] = findMin(kecepatanLambat(kecepatan), suhuRendah(suhu))
  z[1] = sumberPrekuensiKecil(alfa[1])
  # Aturan 3: Jika kecepatan CEPAT dan suhu TINGGI, maka frekuensi BESAR
  alfa[2] = findMin(kecepatanCepat(kecepatan), suhuTinggi(suhu))
  z[2] = sumberPrekuensiBesar(alfa[2])
  # Aturan 4: Jika kecepatan CEPAT dan suhu RENDAH, maka frekuensi BESAR
  alfa[3] = findMin(kecepatanCepat(kecepatan), suhuRendah(suhu))
  z[3] = sumberPrekuensiBesar(alfa[3])
  return alfa, z


def deufuzzyfikasi(alfa, z):
  """Melakukan deufuzzyfikasi menggunakan metode Tsukamoto."""
  temp1 = 0
  temp2 = 0
  for i in range(len(alfa)):
    temp1 += alfa[i] * z[i]
    temp2 += alfa[i]
  return round(temp1 / temp2)


def prediksiFrekuensi(kecepatan, suhu):
  """Menghitung frekuensi putar kipas angin berdasarkan input kecepatan dan suhu."""
  alfa, z = aturan(kecepatan, suhu)
  return deufuzzyfikasi(alfa, z)


# Contoh penggunaan
kecepatan = 4000
suhu = 300
frekuensi = prediksiFrekuensi(kecepatan, suhu)
print(
    f"Frekuensi putar kipas angin yang dihasilkan adalah {frekuensi} rpm."
)