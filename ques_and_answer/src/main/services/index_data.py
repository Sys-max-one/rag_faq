from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from ques_and_answer.src.main.data.data_embedding import DataEmbeddings
from ques_and_answer.src.main.data.load_data import LoadData
from ques_and_answer.src.main.helper.data_helper import DataHelper

class IndexDataService:

    data_embeddings = DataEmbeddings()
    data_helper = DataHelper()
    load_data = LoadData()

    def db_index(self):
        data_load = self.load_data.load_pdf_data_from_default_file()
        data_split = self.data_helper.recursive_text_splitter_default()
        bedrock_data_embeddings = self.data_embeddings.bedrock_embeddings()

        #Create Vector DB, Store Embeddings and Index for Search
        data_index = VectorstoreIndexCreator(
            text_splitter=data_split,
            embedding=bedrock_data_embeddings,
            vectorstore_cls=FAISS)
        #Create index for FAQ Document
        db_index = data_index.from_loaders([data_load])
        return db_index