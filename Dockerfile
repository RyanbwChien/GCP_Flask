# 使用 Python 3.9 作為基礎映像
FROM python:3.9

# 設定工作目錄
WORKDIR /app

# 複製程式碼
COPY . /app

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 啟動 Flask 伺服器
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "Linebotapi_main:app"]