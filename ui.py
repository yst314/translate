import time
import os
import streamlit as st

st.write("Hello, World")
st.markdown("# Translator")

def get_last_modified_time(folder_path):
    return max(os.path.getmtime(os.path.join(folder_path, f)) for f in os.listdir(folder_path))

folder_path = 'results'
last_modified_time = get_last_modified_time(folder_path)

# Streamlitアプリのメインループ
while True:
    time.sleep(1)  # 1秒ごとにチェック
    new_modified_time = get_last_modified_time(folder_path)
    if new_modified_time > last_modified_time:
        last_modified_time = new_modified_time
        # ここでStreamlitアプリの表示を更新
        st.experimental_rerun()