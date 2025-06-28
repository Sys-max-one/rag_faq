from langchain_community.document_loaders import PyPDFLoader

class LoadData:

    default_pdf_file = '../resources/document/pdf/Leave-Policy-India.pdf'

    def load_pdf_data_from_default_file(self):
        data = self.load_pdf_data_from_file_with_path(self.default_pdf_file)
        return data

    def load_pdf_data_from_file_with_path(self, file_path):
        data = PyPDFLoader(file_path)
        return data