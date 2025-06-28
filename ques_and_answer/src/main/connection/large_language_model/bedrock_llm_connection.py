from langchain_aws import BedrockLLM
# Bedrock Foundation Model
class BedrockLLMConnection:
    credentials_profile_name = 'default'
    anthropic_claude_v2_model_id = 'anthropic.claude-v2'

    #Claude Foundation Model
    def bedrock_llm_anthropic_claude_v2(self):
        bedrockLLM = BedrockLLM(
            credentials_profile_name=self.credentials_profile_name,
            model_id=self.anthropic_claude_v2_model_id,
            model_kwargs={
            "max_tokens_to_sample":3000,
            "temperature": 0.1,
            "top_p": 0.9})
        return bedrockLLM