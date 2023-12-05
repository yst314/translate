import time

import streamlit as st


def main():
    status_text = st.empty()
    # プログレスバー
    progress_bar = st.progress(0)

    for i in range(100):
        status_text.text(f'Progress: {i}%')
        # for ループ内でプログレスバーの状態を更新する
        progress_bar.progress(i + 1)
        time.sleep(0.1)

    status_text.text('Done!')
    st.balloons()


if __name__ == '__main__':
    main()