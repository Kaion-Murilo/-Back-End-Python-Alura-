from wsgiref.simple_server import make_server
def aplicacao (environ, start_response):
    produto = [
        {'nome':'Notebook', 'valor':7986.99},
        {'nome':'Mause', 'valor':86.99},
        {'nome':'Teclado', 'valor':796.99},
        {'nome':'Monitor', 'valor':1200.99},
        {'nome':'Microfone', 'valor':846.99},
        {'nome':'WebCam', 'valor':1000}
        ]
    linhas_html = ""
    for produto in produto:
        linhas_html += f'<li>{produto['nome']} - R$ {produto['valor']}</li>'
    start_response ('200 ok',[('Content-type','text/html;charset-utf-8')])
    with open('flask/index.html','r',encoding='utf-8') as files:
        html = files.read()
    html_final = html.replace('{{PRODUTOS}}',linhas_html)
    return [html_final.encode('utf-8')]
make_server('',5000,aplicacao).serve_forever()