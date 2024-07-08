import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="이미지 배경제거기")

st.write("## 이미지의 배경을 제거해보세요!")
st.write(
    ":dog: 이미지를 업로드하여 배경을 제거해보세요. 왼쪽의 사이드바를 통해 원본 퀄리티의 수정된 이미지를 다운받을 수 있습니다."
)
st.write("소스코드[BG_Remover](https://github.com/itzelic-code/BG_Remover). 다음 배경제거 라이브러리를 사용했습니다. [rembg library](https://github.com/danielgatis/rembg) :grin:")
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("원본 이미지 :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("배경 제거된 이미지 :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("수정된 이미지 다운로드", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("이미지 업로드", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("이미지 용량이 초과되었습니다. 5MB 이하의 이미지를 업로드해주세요.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./cat.jpg")
