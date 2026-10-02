FROM python:3.11-slim
WORKDIR /app
COPY inf1103-lab5.py . 
CMD ["python", "inf1103-lab5.py"]dok