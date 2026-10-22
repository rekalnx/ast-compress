# ast-compress ⚡

> **Prune whole codebases into ultra-dense LLM context windows. Zero dependencies. Save 65%–85% on prompt tokens.**

Large language models (Claude 3.7, GPT-4o, DeepSeek-V3) don't need 10,000 lines of implementation boilerplate to understand your project's architecture, debug an interface, or write new features. They only need **type signatures, interfaces, exports, and contracts**.

`ast-compress` is a lightweight, zero-dependency CLI that parses ASTs across multiple programming languages and strips function bodies down to pure structural interfaces while preserving 100% of the architectural context.

---

## 🚀 Key Features

- **Pure Zero-Dependencies**: Built entirely on standard libraries (`ast`, `re`, `json`). No `pip install` hell.
- **Multi-Language Engine**: Native support for **Python**, **TypeScript**, **JavaScript**, **Go**, and **JSON**.
- **Massive Token Savings**: Typically reduces context size by **70% to 85%** without losing type hints or return contracts.
- **LLM-Ready Formatting**: Outputs Markdown with syntax highlighting blocks or structured JSON with compression metrics.
- **Safe & Deterministic**: AST-based verification guarantees syntactically sound stubs.

---

## 📦 Installation

Just download the single script or run with `python3`:

```bash
curl -O https://raw.githubusercontent.com/rekalnx/ast-compress/main/ast_compress.py
chmod +x ast_compress.py
sudo mv ast_compress.py /usr/local/bin/ast-compress
```

---

## 🛠️ Usage

### Compress a single file:
```bash
ast-compress my_service.py
```

### Compress an entire repository into a prompt context file:
```bash
ast-compress ./src --format markdown -o prompt_context.md
```

### Output JSON with compression metrics:
```bash
ast-compress ./backend --format json
```

---

## 📊 Benchmark Example

Compressing `ast_compress.py` itself:
```text
Original Size:   9,051 bytes (~2,260 tokens)
Compressed Size: 1,439 bytes (~360 tokens)
Token Savings:   84.1%
```

---

## 📄 License
MIT © [Reihan Valentino (rekalnx)](https://github.com/rekalnx)
