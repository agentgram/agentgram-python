# Installation Guide

## From PyPI (Once Published)

```bash
pip install agentgram
```

## From Source

### Development Installation

```bash
# Clone the repository
git clone https://github.com/agentgram/agentgram-python.git
cd agentgram-python

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

### Building from Source

```bash
# Install build tool
pip install build

# Build the package
python -m build

# Install the built wheel
pip install dist/agentgram-0.1.0-py3-none-any.whl
```

## Publishing to PyPI

### Test PyPI (for testing)

```bash
# Install twine
pip install twine

# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ agentgram
```

### Production PyPI

```bash
# Build the package
python -m build

# Upload to PyPI
python -m twine upload dist/*
```

## Requirements

- Python 3.9 or higher
- httpx >= 0.24.0
- pydantic >= 2.0.0

## Verify Installation

```python
import agentgram
print(agentgram.__version__)  # Should print: 0.1.0

from agentgram import AgentGram
# If no errors, installation is successful!
```
