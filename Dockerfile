FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY impact_crater_depth_diameter_calculator.py app.py ./

EXPOSE 7860

CMD ["python", "app.py"]
