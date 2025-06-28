from ques_and_answer.src.main.connection.large_language_model.bedrock_llm_connection import BedrockLLMConnection

class RAGResponse:

    llm_connection = BedrockLLMConnection()

    #Get Response by sending both of these to LLM:
    # 1. Vector similarity search index
    # 2. User prompt(or question)
    def rag_llm_response(self, vector_store_index, question):
        response = vector_store_index.query(question=question, llm=self.llm_connection)
        return response