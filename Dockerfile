# Build stage
FROM python:3.10.6-slim-buster AS builder
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app

# Run stage
FROM python:3.10.6-slim-buster AS runner
RUN adduser --disabled-password tuna
USER tuna
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder /app /app
WORKDIR /app
EXPOSE 12031
CMD ["gunicorn", "-b", "0.0.0.0:12031", "personal_website:app"]
