from langchain_openai import ChatOpenAI

from ai_model.model import Model


class ChatGLMModel( Model ):

    def __init__( self, model_name: str, api_key: str ):
        self.model_name = model_name
        self.api_key = api_key

    def create_llm( self ):
        """
        初始化智普的大语言模型对象
        :return:
        """
        # 创建智谱 LLM 实例
        llm = ChatOpenAI(
            temperature = 0.6,
            model = "glm-4.5",
            openai_api_key = self.api_key,
            openai_api_base = "https://open.bigmodel.cn/api/paas/v4/"
        )

        return llm
