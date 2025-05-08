FROM python:3.11
WORKDIR /app
COPY CommandService /app
COPY shared /app/shared
RUN pip install fastapi uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]
