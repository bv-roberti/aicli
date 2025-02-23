# aicli

A CLI tool powered by large language models (LLMs) that serves as an interactive command-line assistant.

## Overview

aicli uses OpenAI's GPT-3.5-turbo model to answer user queries. The assistant can suggest and execute valid shell commands based on your input.

## Installation

Ensure you have Python 3.8 or higher installed.

Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## Setup

Replace the placeholder `OPENAI_API_KEY` in `aicli.py` with your actual OpenAI API key.

## Usage

To start the interactive shell, run:

```bash
python aicli.py
```

You can also use the command-line entry point if the package is installed globally. Once running, simply type your query. If the assistant suggests a shell command, you'll be prompted to confirm before execution.

Try as a global package too

```
pip install --editable .
```

## Project Structure

- **aicli.py**: Main module implementing the CLI tool.
- **setup.py**: Packaging configuration.
- Additional configuration and metadata files are provided for packaging and distribution.

## License

This project is licensed under the terms specified in the `setup.py` metadata.
