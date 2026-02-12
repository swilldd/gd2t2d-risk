FROM python:3.13.9-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

ENV PATH="/app/.venv/bin:$PATH"

COPY "pyproject.toml" "uv.lock" ".python-version" ./

RUN uv sync --locked

COPY ./utils/ /code/utils/ 

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "streamlit_app", "--host", "0.0.0.0", "--port", "8501"]