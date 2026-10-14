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


def cari_berkas():
    folder = Path(__file__).parent
    for nama in ("index.html", "index1.html"):
        if (folder / nama).exists():
            return folder / nama
    # cadangan: pakai berkas .html apa saja yang ada di repositori
    lain = sorted(folder.rglob("*.html"))
    return lain[0] if lain else None


berkas = cari_berkas()
if berkas is None:
    st.error("Berkas index.html tidak ditemukan di repositori ini.")
    st.write("Unggah index.html ke GitHub, satu folder dengan app.py. Berkas yang terlihat saat ini:")
    st.code("\n".join(sorted(p.name for p in Path(__file__).parent.iterdir())) or "(kosong)")
    st.stop()

if hasattr(st, "iframe"):  # Streamlit terbaru
    st.iframe(berkas, height=900)
else:  # Streamlit versi lama
    import streamlit.components.v1 as components

    components.html(berkas.read_text(encoding="utf-8"), height=900, scrolling=True)
