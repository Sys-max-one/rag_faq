from langchain.text_splitter import RecursiveCharacterTextSplitter

class DataHelper:
    default_chunk_overlap = 10
    default_separators = ["\n\n", "\n", " ", ""]
    default_chunk_size = 1000

    #Split the Text based on Character, size etc.
    def recursive_text_splitter_default(self):
        data_split = RecursiveCharacterTextSplitter(separators=self.default_separators, chunk_size=self.default_chunk_size, chunk_overlap=self.default_chunk_overlap)
        return data_split

    def recursive_text_splitter(self, separators, chunk_size):
        data_split = RecursiveCharacterTextSplitter(separators=separators, chunk_size=chunk_size, chunk_overlap=self.default_chunk_overlap)
        return data_split