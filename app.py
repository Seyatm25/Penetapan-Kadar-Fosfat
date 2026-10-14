from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Spektrofotometer Digital - Penetapan Fosfat",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Buang header/footer/padding bawaan Streamlit supaya web tampil penuh layar
st.markdown(
    """
    <style>
    #MainMenu, footer, header[data-testid="stHeader"] {display: none !important;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    [data-testid="stVerticalBlock"] {gap: 0 !important;}
    iframe {height: 100vh !important; width: 100% !important; border: 0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)


def cari_berkas() -> Path:
    folder = Path(__file__).parent
    for nama in ("index.html", "index1.html"):
        berkas = folder / nama
        if berkas.exists():
            return berkas
    raise FileNotFoundError("Taruh index.html satu folder dengan app.py")


berkas = cari_berkas()
if hasattr(st, "iframe"):  # Streamlit terbaru
    st.iframe(berkas, height=900)
else:  # Streamlit versi lama
    import streamlit.components.v1 as components

    components.html(berkas.read_text(encoding="utf-8"), height=900, scrolling=True)
