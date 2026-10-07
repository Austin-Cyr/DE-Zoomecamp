FROM python:3.13.11-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/




WORKDIR /code
# Copy dependency files first (better layer caching)
# Add virtual environment to PATH so we can use installed packages
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml uv.lock .python-version  README.md ./
COPY src/ ./src/
RUN uv sync --locked

COPY pipeline.py . 

ENTRYPOINT ["uv", "run", "python", "pipeline.py"]