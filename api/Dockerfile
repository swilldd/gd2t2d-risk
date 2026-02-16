FROM python:3.13.9-slim

# Install curl for health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

ENV PATH="/app/.venv/bin:$PATH"

COPY "pyproject.toml" "uv.lock" ".python-version" ./

RUN uv sync --locked

COPY ./src/ /code/src/ 

EXPOSE 9696

ENTRYPOINT ["uv", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "9696"]