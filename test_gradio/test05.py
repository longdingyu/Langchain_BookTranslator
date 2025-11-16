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
    history.append( (message, resp) )
    time.sleep( 1 )
    return '', history  # 返回一个空字符串，并把输入的message和生成的答案添加到history里面, 并清空输入框


# Blocks：自定义各种组件联合的一个函数
with gr.Blocks( title = '我的AI聊天机器人' ) as instance:
    chatbot = gr.Chatbot( height = 300, placeholder = '<strong>AI机器人</strong><br> 你可以问任何问题' )
    msg = gr.Textbox( placeholder = '请输入问题...', container = False )
    clear = gr.ClearButton( value = '清除聊天内容', components = [ chatbot, msg ] )

    msg.submit( do_it, [ msg, chatbot ], [ msg, chatbot ] )

instance.launch( server_name = '0.0.0.0', server_port = 8008 )
