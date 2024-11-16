import flet as ft

def main(pagina):
    # CHAT
    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem_tunel):
        texto_entrada = ft.Text(mensagem_tunel)
        chat.controls.append(texto_entrada)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f"{nome_usuario.value}: {mensagem.value}")
        mensagem.value = ""
        pagina.update()
    
    def test_func(evento): # Isso aqui é legal de saber, é até possível fazer um "user está digitando"
        print("OK")

    mensagem = ft.TextField(label="Digite sua mensagem", on_change=test_func, on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row(controls=[mensagem, botao_enviar]) # funciona sem o "controls="

    # POPUP
    def entrar_chat(evento):
        popup.open = False
        pagina.update()
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(chat)
        pagina.add(linha_enviar)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        pagina.update()

    titulo_popup = ft.Text("Bem vindo ao FefeGois Chat")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton(text="Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )

    #PAGINA
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    texto = ft.Text("FefeGois Chat")
    botao_iniciar = ft.ElevatedButton(text="Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)
