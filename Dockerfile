FROM python:3.13.3-slim-bookworm
WORKDIR /workspace
# The uv command also errors out when installing semgrep:
# - Getting semgrep-core in pipenv · Issue #2929 · semgrep/semgrep
#   https://github.com/semgrep/semgrep/issues/2929#issuecomment-818994969
ENV SEMGREP_SKIP_BIN=true
COPY pyproject.toml /workspace/
RUN pip install --no-cache-dir uv==0.7.2 \
 && uv sync
COPY . /workspace
ENTRYPOINT [ "uv", "run" ]
CMD ["pytest"]
