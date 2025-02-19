# 使用 Python 3.9 作為基礎映像
FROM python:3.9

# 設定工作目錄
WORKDIR /app

# 複製程式碼
COPY . /app  # 把當前目錄內的所有檔案複製到 Docker 容器的當前目錄（已設定為 /app）

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 啟動 Flask 伺服器
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "Linebotapi_main:app"]