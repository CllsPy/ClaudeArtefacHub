import streamlit as st
import base64

# Configuração da página
st.set_page_config(
    page_title="Galeria Interativa",
    page_icon="🖼️",
    layout="wide"
)

# Título da aplicação
st.title("Galeria Interativa")
st.markdown("Clique nas imagens abaixo para visitar os sites correspondentes.")

# Função para criar um link clicável a partir de uma imagem
def image_as_link(image_url, link_url, caption=""):
    html = f"""
    <a href="{link_url}" target="_blank">
        <img src="{image_url}" style="width:100%; border-radius:10px; margin-bottom:5px;">
        <p style="text-align:center;">{caption}</p>
    </a>
    """
    return html

# Dados das imagens e links (exemplo)
gallery_items = [
    {
        "image": "https://picsum.photos/400/300?random=1",
        "link": "https://www.google.com",
        "caption": "Google"
    },
    {
        "image": "https://picsum.photos/400/300?random=2",
        "link": "https://www.youtube.com",
        "caption": "YouTube"
    },
    {
        "image": "https://picsum.photos/400/300?random=3",
        "link": "https://www.wikipedia.org",
        "caption": "Wikipedia"
    },
    {
        "image": "https://picsum.photos/400/300?random=4",
        "link": "https://www.github.com",
        "caption": "GitHub"
    },
    {
        "image": "https://picsum.photos/400/300?random=5",
        "link": "https://www.twitter.com",
        "caption": "Twitter"
    },
    {
        "image": "https://picsum.photos/400/300?random=6",
        "link": "https://www.reddit.com",
        "caption": "Reddit"
    }
]

# Alternativa usando uma área colorida clicável
st.markdown("## Áreas Clicáveis")
st.markdown("Você também pode clicar nas áreas coloridas abaixo:")

# Layout de grade para as imagens
num_cols = 3
cols = st.columns(num_cols)

# Preencher a grade com imagens clicáveis
for i, item in enumerate(gallery_items):
    col_idx = i % num_cols
    with cols[col_idx]:
        st.markdown(
            image_as_link(item["image"], item["link"], item["caption"]),
            unsafe_allow_html=True
        )

# Áreas coloridas clicáveis
color_areas = [
    {"color": "#FF6B6B", "link": "https://www.netflix.com", "text": "Netflix"},
    {"color": "#4ECDC4", "link": "https://www.spotify.com", "text": "Spotify"},
    {"color": "#FFE66D", "link": "https://www.amazon.com", "text": "Amazon"}
]

# CSS para áreas clicáveis
st.markdown("""
<style>
    .area-link {
        display: block;
        padding: 30px;
        margin: 10px 0;
        text-align: center;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        text-decoration: none;
        transition: transform 0.3s ease;
    }
    .area-link:hover {
        transform: scale(1.03);
    }
</style>
""", unsafe_allow_html=True)

# Layout para áreas coloridas
area_cols = st.columns(len(color_areas))
for i, area in enumerate(color_areas):
    with area_cols[i]:
        st.markdown(
            f"""
            <a href="{area['link']}" target="_blank" class="area-link" style="background-color: {area['color']}">
                {area['text']}
            </a>
            """,
            unsafe_allow_html=True
        )

# Configurações da aplicação
with st.sidebar:
    st.header("Configurações")
    st.write("Personalize sua galeria")
    
    # Opção para modificar o layout
    layout_option = st.selectbox(
        "Layout da galeria",
        ["Grade", "Lista"]
    )
    
    # Opção para escolher a categoria
    category = st.selectbox(
        "Categoria",
        ["Todos", "Redes Sociais", "Tecnologia", "Entretenimento"]
    )
    
    # Botão para adicionar novas imagens (não funcional neste exemplo)
    st.button("Adicionar nova imagem")
    
    st.markdown("---")
    st.markdown("### Como usar")
    st.markdown("1. Clique em qualquer imagem para abrir o site correspondente")
    st.markdown("2. Use as configurações para personalizar a visualização")
    st.markdown("3. Experimente clicar nas áreas coloridas")