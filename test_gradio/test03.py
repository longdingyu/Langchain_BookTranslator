import random
import time

import gradio as gr
from reportlab.lib.pagesizes import letter


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
    # inputs = [
    #    gr.Text(label = '请输入一个提问')
    # ],
    # outputs = gr.Text(label = '输出结果:'),
    title = '模拟流式输出'
)

instance.launch( server_name = '0.0.0.0', server_port = 8008 )
