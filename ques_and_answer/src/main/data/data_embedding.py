from langchain_aws import BedrockEmbeddings

class DataEmbeddings:
    aws_credentials_profile_name = 'default',
    aws_titan_text_v1_model_id = 'amazon.titan-embed-text-v1'

    #Create Embeddings: Bedrock Client connection
    def bedrock_embeddings(self):
        data_embeddings = BedrockEmbeddings(
            credentials_profile_name = self.aws_credentials_profile_name,
            model_id = self.aws_titan_text_v1_model_id)
        return data_embeddings