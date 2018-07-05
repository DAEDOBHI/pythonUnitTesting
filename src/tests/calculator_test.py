 # -*- coding: utf-8 -*-
import unittest

from  app.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    
    def setUp(self):
        """
            Create a instance to class Calculator
        """
        self.calc = Calculator()

    def test_calculate_iva(self):
        
        
        result = self.calc.get_iva(100)
        self.assertEqual(result,16)

        result2 = self.calc.get_iva(200)#32
        self.assertEqual(result2,32)

        result3 = self.calc.get_iva(500)#32
        self.assertEqual(result3,80)

        result3 = self.calc.get_iva(1000)#32
        self.assertEqual(result3,160)
    def test_calculate_iva_with_different_rate(self):
        
        result = self.calc.get_iva(200,rate =.20)
        self.assertEqual(result,40)

    def test_calculate_interest(self):
        """PRUEBA UNA FUCNION QUE CALCULA EL INTERÉS,
        RECIBIENDO MONTO INCIAL, TASA DE INTERÉS Y PERIODOS
        (INTERÉS SIMPLE)
        IS = (MI*IR)*N
        """
        
        result = self.calc.get_interest(100,.10,10)
        self.assertEqual(result,100)
    
    def test_calculate_compound_interest():
        result = self.calc.get_interest(1000,.10,10,compound = True)
        self.asserAlmostEqual(result,100)

        """    def test_calculate_invertion():
        result = self.calc.get_invertion(1000,.10,500,2)
        self.asserAlmostEqual(result,)"""
        """
            calcular inversion
            recibe: inicial,rate,monto_mensal,periods
    
        """
