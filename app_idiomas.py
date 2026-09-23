import streamlit as st
from google import genai

# Configuração visual da página web
st.set_page_config(page_title="Assistente de Idiomas IA", page_icon="🌐", layout="centered")

# Mantém o cliente da IA conectado na memória
if "client" not in st.session_state:
    st.session_state.client = genai.Client()

st.title("🌐 Assistente Pro de Idiomas com IA")
st.markdown("Treine seu vocabulário, faça traduções inteligentes ou simule conversas reais.")

# Criação das abas do sistema
aba_tradutor, aba_conversacao = st.tabs(["🔤 Tradutor Contextual", "💬 Simulador de Conversa"])

# =====================================================================
# ABA 1: TRADUTOR CONTEXTUALIZADO
# =====================================================================
with aba_tradutor:
    st.subheader("Tradução Inteligente")
    st.write("Traduz e explica o significado real de expressões, gírias ou frases do dia a dia.")
    
    # Seleção de idiomas
    idioma_origem = st.selectbox("Idioma de Origem:", ["Português", "Inglês", "Espanhol"], index=0)
    idioma_destino = st.selectbox("Idioma de Destino:", ["Inglês", "Espanhol", "Português"], index=1)
    
    texto_para_traduzir = st.text_area("Digite o texto ou expressão aqui:")
    
    if st.button("Traduzir com Contexto", type="primary"):
        if texto_para_traduzir.strip() == "":
            st.warning("Por favor, digite alguma coisa para traduzir.")
        else:
            with st.spinner("Analisando contexto..."):
                try:
                    prompt_tradutor = f"""
                    Você é um professor especialista em idiomas e tradutor nativo.
                    Traduza o seguinte texto do {idioma_origem} para o {idioma_destino}:
                    "{texto_para_traduzir}"
                    
                    Formate sua resposta exatamente assim:
                    ### 🎯 Tradução Direta:
                    [Coloque a tradução direta aqui]
                    
                    ### 💡 Explicação Contextual e Dicas:
                    [Se houver gírias, expressões idiomáticas, ou diferenças culturais na frase, explique de forma simples. Se for uma frase comum, dê exemplos de como usar ou variações comuns].
                    """
                    
                    response = st.session_state.client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt_tradutor,
                    )
                    
                    st.markdown("---")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Erro de comunicação: {e}")

# =====================================================================
# ABA 2: SIMULADOR DE CONVERSAÇÃO (RPG de Idiomas)
# =====================================================================
with aba_conversacao:
    st.subheader("Simulação de Situações Reais")
    st.write("Escolha um cenário e converse com a IA no idioma escolhido para praticar!")
    
    idioma_pratica = st.selectbox("Qual idioma quer praticar?", ["Inglês", "Espanhol"])
    cenario = st.selectbox("Escolha o cenário da conversa:", [
        "Entrevista de Emprego",
        "Fazendo Check-in em um Hotel",
        "Pedindo comida em um Restaurante",
        "Conversa amigável sobre rotina diária"
    ])
    
    # Inicializa o histórico e o chat específicos para conversação
    if "chat_idiomas_historico" not in st.session_state:
        st.session_state.chat_idiomas_historico = []
    
    # Botão para resetar ou iniciar o cenário do zero
    if st.button("Iniciar / Reiniciar Cenário"):
        st.session_state.chat_idiomas_historico = []
        
        prompt_sistema = f"""
        Você vai simular o cenário '{cenario}' no idioma {idioma_pratica}.
        Aja estritamente como a pessoa daquela situação (ex: o entrevistador, o recepcionista do hotel, o garçom).
        Comece a conversa de forma natural no idioma {idioma_pratica}.
        Mantenha suas respostas curtas (máximo 3 frases) para dar espaço para o usuário responder.
        Não coloque traduções automáticas nas suas falas, deixe o usuário praticar.
        """
        
        # Cria uma sessão limpa de chat
        st.session_state.chat_idiomas_objeto = st.session_state.client.chats.create(
            model="gemini-2.5-flash",
            config={"system_instruction": prompt_sistema}
        )
        
        # Gera a primeira fala da IA para abrir o cenário
        resposta_inicial = st.session_state.chat_idiomas_objeto.send_message("Olá, comece a simulação agora apresentando-se no contexto.")
        st.session_state.chat_idiomas_historico.append({"autor": "assistant", "texto": resposta_inicial.text})

    # Exibe as mensagens da simulação atual na tela
    for msg in st.session_state.chat_idiomas_historico:
        with st.chat_message(msg["autor"]):
            st.write(msg["texto"])

    # Entrada de texto do usuário para responder a IA
    if entrada_usuario := st.chat_input("Responda aqui no idioma que está praticando..."):
        if "chat_idiomas_objeto" not in st.session_state:
            st.error("Por favor, clique no botão 'Iniciar / Reiniciar Cenário' primeiro para começar!")
        else:
            with st.chat_message("user"):
                st.write(entrada_usuario)
            st.session_state.chat_idiomas_historico.append({"autor": "user", "texto": entrada_usuario})
            
            with st.chat_message("assistant"):
                with st.spinner("Pensando..."):
                    try:
                        resposta_ia = st.session_state.chat_idiomas_objeto.send_message(entrada_usuario)
                        st.write(resposta_ia.text)
                        st.session_state.chat_idiomas_historico.append({"autor": "assistant", "texto": resposta_ia.text})
                    except Exception as e:
                        st.error(f"Erro na conexão do chat: {e}")