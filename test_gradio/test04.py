import random
import time

import gradio as gr


def do_it( message, history ):  # 定义一个函数,并初始化一个进度条
    responses = [
        "谢谢您的留言！",
        "非常有趣！",
        "我不确定该如何回答。",
        "请问还有其他问题吗？",
        "我会尽快回复您的。",
        "很高兴能与您交流！",
    ]

    # 生成一个随机答案
    resp = random.choice( responses )
    # 流式输出
    res = ''
    for char in resp:
        res += char
        time.sleep( 0.1 )
        yield res


instance = gr.ChatInterface(  # 构建一个UI界面
    fn = do_it,
    chatbot = gr.Chatbot( height = 300, placeholder = '<strong>AI机器人</strong><br> 你可以问任何问题' ),
    textbox = gr.Textbox( placeholder = '请输入问题...', lines = 1, container = False, scale = 8 ),
    title = '我的AI聊天机器人',
    description = 'AI助手',
    examples = [
        [ '你好' ],
        [ '你叫什么名字？' ],
        [ '你喜欢吃什么？' ],
        [ '你喜欢吃什么？' ],
    ],
    cache_examples = True,
)

instance.launch( server_name = '0.0.0.0', server_port = 8008 )
