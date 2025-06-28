import unittest
from unittest.mock import patch
from ques_and_answer.src.main.data.load_data import LoadData

load_data = LoadData()
test_pdf_file_path = '../../resources/document/pdf/test_Leave-Policy-India.pdf'

class TestLoadData(unittest.TestCase):
    def test_load_pdf_data_from_file(self):
        data_load = load_data.load_pdf_data_from_file_with_path(test_pdf_file_path)
        data_test = data_load.load_and_split()
        self.assertEqual(len(data_test), 8)

    @patch("ques_and_answer.src.main.data.load_data.LoadData.default_pdf_file", new=test_pdf_file_path)
    def test_load_pdf_data_from_default_file(self):
        data_load = load_data.load_pdf_data_from_default_file()
        data_test = data_load.load_and_split()
        self.assertEqual(len(data_test), 8)

if __name__ == '__main__':
    unittest.main()
