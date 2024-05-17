import unittest

m3i = '3 lados iguales'
m2i = '2 lados iguales'
m3d = '3 lados distintos'
mnt = 'No es un triángulo'

# Función que no siempre anda bien
def tri(l1,l2,l3):
   if l1 == l2:
      return(m2i)
   else:
      # Esta es la gracia de haber definido m3d
      return('3 Lados distintos')
      
# Acá zampamos los casos de prueba      
class TestTri(unittest.TestCase):

   # Caso de prueba: si vienen 3 ochos, el triángulo tiene tres lados iguales
   def testEq(self):
      self.assertEqual(tri(8,8,8),m3i)
      
   # Etcétera   
   def testIso1(self):
      self.assertEqual(tri(8,8,5),m2i)
      
   def testIso2(self):
      self.assertEqual(tri(5,8,8),m2i)
      
   def testIso3(self):
      self.assertEqual(tri(8,5,8),m2i)

   def testEsc(self):
      self.assertEqual(tri(8,7,6),m3d)
      
   def testNT1(self):
      self.assertEqual(tri(100,22,55),mnt)
      
   def testNT2(self):
      self.assertEqual(tri(0,0,0),mnt)

   def testNT3(self):
      self.assertEqual(tri(4,4,8),mnt)

   def testNT4(self):
      self.assertEqual(tri(1,1,0),mnt)

   def testNT5(self):
      self.assertEqual(tri(8,4,4),mnt)

   def testNT6(self):
      self.assertEqual(tri(4,8,4),mnt)
      
   def testNT7(self):
      self.assertEqual(tri(8,6,1),mnt)
      
# Esto corre los casos de prueba definidos arriba
if __name__ == '__main__':
    unittest.main()
