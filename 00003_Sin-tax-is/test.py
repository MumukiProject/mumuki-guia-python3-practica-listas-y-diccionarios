class Test(unittest.TestCase):

  def test_el_guiso_de_lentejas_es_apto_celiacos(self):
    self.assertTrue(apto_celiacos(guiso_de_lentejas))
    
  def test_las_empanadas_no_son_apto_celiacos(self):
    self.assertFalse(apto_celiacos(empanadas))    