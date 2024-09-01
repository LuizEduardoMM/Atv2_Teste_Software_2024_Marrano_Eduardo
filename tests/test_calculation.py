import unittest

from pycpfcnpj import calculation as calc


class CalculationTests(unittest.TestCase):
    """docstring for CalculationTests"""

    def setUp(self):
        self.first_part_cpf_number = '131654777'
        self.first_part_cnpj_number = '234568890123'
        self.result_division_two_cnpj = '234568890123'
        self.result_division_two_cpf = '131654777'

    def test_first_digit_division_two(self):
        test_number = self.result_division_two_cnpj
        expected_result = '9'
        result = calc.calculate_first_digit(test_number)
        self.assertEqual(expected_result, result,
                         "The function should return the expected result when rest_division <=2")

    def test_first_digit_division_two_cpf(self):
        test_number = self.result_division_two_cpf
        expected_result = '9'
        result = calc.calculate_first_digit(test_number)
        self.assertEqual(expected_result, result,
                         "The function should return the expected result when rest_division <=2")

    # TESTS FOR CPF DIGITS
    def test_cpf_calculate_first_digit_true(self):
        correct_first_digit = '9'
        self.assertEqual(correct_first_digit,
                         calc.calculate_first_digit(self.first_part_cpf_number))

    def test_cpf_calculate_first_digit_false(self):
        incorrect_first_digit = '0'
        self.assertNotEqual(incorrect_first_digit,
                            calc.calculate_first_digit(self.first_part_cpf_number))

    def test_cpf_calculate_second_digit_true(self):
        updated_cpf_number = self.first_part_cpf_number + \
                             calc.calculate_first_digit(
                                 self.first_part_cpf_number)
        correct_second_digit = '5'
        self.assertEqual(correct_second_digit,
                         calc.calculate_second_digit(updated_cpf_number))

    def test_cpf_calculate_second_digit_false(self):
        updated_cpf_number = self.first_part_cpf_number + \
                             calc.calculate_first_digit(
                                 self.first_part_cpf_number)
        incorrect_second_digit = '7'
        self.assertNotEqual(incorrect_second_digit,
                            calc.calculate_second_digit(updated_cpf_number))

    # TESTS FOR CNPJ DIGITS
    def test_cnpj_calculate_first_digit_true(self):
        correct_first_digit = '9'
        self.assertEqual(correct_first_digit,
                         calc.calculate_first_digit(self.first_part_cnpj_number))

    def test_cnpj_calculate_first_digit_false(self):
        correct_first_digit = '7'
        self.assertNotEqual(correct_first_digit,
                            calc.calculate_first_digit(self.first_part_cnpj_number))

    def test_cnpj_calculate_second_digit_true(self):
        correct_second_digit = '9'
        updated_cnpj_number = self.first_part_cnpj_number + \
                              calc.calculate_first_digit(
                                  self.first_part_cnpj_number)
        self.assertEqual(correct_second_digit,
                         calc.calculate_second_digit(updated_cnpj_number))

    def test_cnpj_calculate_second_digit_false(self):
        correct_second_digit = '2'
        updated_cnpj_number = self.first_part_cnpj_number + \
                              calc.calculate_first_digit(
                                  self.first_part_cnpj_number)
        self.assertNotEqual(correct_second_digit,
                            calc.calculate_second_digit(updated_cnpj_number))
