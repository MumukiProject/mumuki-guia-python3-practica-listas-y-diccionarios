class Test(unittest.TestCase):

  def test_titulo_para_el_menu_spaghetti_frutti_di_mare(self):
    
    self.assertEqual(
      titulo_para_el_menu("spaghetti frutti di mare"), 
      "Spaghetti Frutti Di Mare")
      
  def test_titulo_para_el_menu_empanadas_de_carne_cuchillo(self):
    
    self.assertEqual(
      titulo_para_el_menu("empanadas de carne cuchillo"), 
      "Empanadas De Carne Cuchillo")      