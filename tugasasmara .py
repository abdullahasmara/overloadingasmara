class BilanganBulat(object):
   def __init__(self, nilai):
      if not isinstance(nilai, int):
         raise TypeError("Nilai harus bertipe bilangan bulat")
      self.nilai = nilai

   def __div__(self, objek):
      if isinstance(objek, int):
         return self.nilai / objek
      elif isinstance(objek, float):
         return float(self.nilai / objek)
      elif isinstance(objek, BilanganBulat):
         return self.nilai / objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")

   def __le__(self, objek):
      if isinstance(objek, int):
         return self.nilai <= objek
      elif isinstance(objek, float):
         return float(self.nilai) <= objek
      elif isinstance(objek, BilanganBulat):
         return self.nilai <= objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")

def main():

   a = BilanganBulat(30)
   b = BilanganBulat(20)


   c = 50


   d = 20.00


   print("a == b: ", a <= b)
   print("a == c: ", a <= c)
   print("b == d: ", b <= d)

if __name__ == "__main__":
   main()
