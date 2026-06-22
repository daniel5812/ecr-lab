FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser && \
    chown -R appuser:appgroup /app

ENV PORT=8080
ENV APP_ENV=container

EXPOSE 8080

USER appuser

CMD ["python", "app.py"]