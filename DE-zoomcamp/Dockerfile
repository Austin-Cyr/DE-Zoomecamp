FROM python:3.13.11-slim

RUN pip install pandas pyarrow

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/




WORKDIR /code
# Copy dependency files first (better layer caching)
# Add virtual environment to PATH so we can use installed packages
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml uv.lock .python-version  README.md ./
COPY src/ ./src/
# install dependencies from uv.lock file to bring over from venv to docker env
RUN uv sync --locked

COPY ingest_data.py . 

# below comments are cached
ENTRYPOINT ["python", "ingest_data.py"]