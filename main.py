from translator.book_translator import PDFTranslator
from utils.project_config import ProjectConfig
import os

if __name__ == '__main__':
    # 初始化项目配置
    config = ProjectConfig()
    config.initialize()
    os.environ.pop( 'http_proxy', None )
    os.environ.pop( 'https_proxy', None )

    # 初始化 LLM
    if config.model_type == 'OpenAIModel':
        from ai_model.openai_model import OpenAIModel
        model = OpenAIModel(config.model_name, config.api_key)
    elif config.model_type == 'GLMModel':
        from ai_model.glm_model import ChatGLMModel
        model = ChatGLMModel(config.model_name, config.api_key)
    else:
        raise ValueError(f'不支持的模型类型：{config.model_type}')

    print( f"Model Type: {config.model_type}" )
    print( f"API Key: {config.api_key}" )

    translator = PDFTranslator(model)
    translator.translate_book(config.input_file, config.source_language, config.target_language, config.file_format)