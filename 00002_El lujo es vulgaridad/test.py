class Test(unittest.TestCase):

  def test_las_empanadas_son_sofisticadas(self):
    self.assertTrue(es_sofisticada(empanadas))

  def el_guiso_de_lentejas_no_es_sofisticado(self):
    self.assertFalse(es_sofisticada(guiso_de_lentejas))  
    
  def el_queso_y_dulce_no_es_sofisticado(self):
    self.assertFalse(es_sofisticada(queso_y_dulce))  