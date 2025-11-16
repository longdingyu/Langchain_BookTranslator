import time

import gradio as gr

def do_it( text: str, progress= gr.Progress()): #定义一个函数,并初始化一个进度条
    res = ''
    progress(0, desc = '开始...')

    #进度条滚动,模拟处理
    for i in progress.tqdm(text, desc = '正在处理中...'):
        time.sleep(0.25)
        res += i
    return res


instance = gr.Interface( #构建一个UI界面
    fn = do_it,
    inputs = [
       gr.Text(label = '输入任何文本')
    ],
    outputs = gr.Text(label = '输出结果:')
)


instance.launch(server_name = '0.0.0.0', server_port = 8008)