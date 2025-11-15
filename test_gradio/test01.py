import gradio as gr

def caculate(a, op, b):
    if op == '加法':
        return a + b
    elif op == '减法':
        return a - b
    elif op == '乘法':
        return a * b
    elif op == '除法':
        if b == 0:
            raise gr.Error('除数不能为0')
        return a / b

instance = gr.Interface( #构建一个UI界面
    fn = caculate,
    inputs = [
        'number',
        gr.Radio(choices = ['加法', '减法', '乘法', '除法'], label="运算符"),
        'number'
    ],
    outputs = 'number'
)


instance.launch(server_name = '0.0.0.0', server_port = 8008, auth = ('admin', '123123'))