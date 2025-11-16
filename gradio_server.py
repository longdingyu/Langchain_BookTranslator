import gradio as gr

from translator.book_translator import PDFTranslator
from utils.project_config import ProjectConfig


def translation(input_file, source_language, target_language):
    """
    翻译
    :param input_file:
    :param source_language:
    :param target_language:
    :return:
    """

    output_file = translator.translate_book(input_file, source_language, target_language)
    return output_file

def init_translator():
    config = ProjectConfig()
    config.initialize()

    # 初始化 LLM
    if config.model_type == 'OpenAIModel':
        from ai_model.openai_model import OpenAIModel
        model = OpenAIModel( config.model_name, config.api_key )
    elif config.model_type == 'GLMModel':
        from ai_model.glm_model import ChatGLMModel
        model = ChatGLMModel( config.model_name, config.api_key )
    else:
        raise ValueError( f'不支持的模型类型：{config.model_type}' )

    print( f"Model Type: {config.model_type}" )
    print( f"API Key: {config.api_key}" )

    global translator
    translator = PDFTranslator( model )


def run_gradio():
    """
    启动gradio
    :return:
    """

    instance = gr.Interface(
        fn = translation,
        title = '自动翻译器 v2.0',
        inputs = [
            gr.File(label = '请上传文件'),
            gr.Textbox(label = '源语言(默认:英文)', placeholder = 'English', value = 'English'),
            gr.Textbox(label = '目标语言(默认:中文)', placeholder = '中文', value = '中文'),
        ],
        outputs = [
            gr.File(label = '下载翻译之后的文件')
        ],
        allow_flagging = 'never' #不现实Flag按钮
    )

    instance.launch(server_name = '0.0.0.0', server_port = 8008)




if __name__ == '__main__':
    init_translator()
    run_gradio()
