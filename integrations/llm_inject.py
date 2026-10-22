"""LLM System Prompt Injection Helper."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ast_compress import scan_directory

def generate_llm_system_context(codebase_dir: str, max_tokens: int = 8000) -> str:
    """Generates ultra-compact Markdown code interface documentation for LLM prompts."""
    files = scan_directory(codebase_dir, [".py", ".ts", ".js", ".go"])
    lines = [
        "### Project Architecture Context (Extracted via ast-compress)",
        "The following interfaces represent the type signatures and contracts of the project.\n"
    ]
    for f in files:
        lines.append(f"#### File: `{os.path.basename(f['file'])}`")
        lines.append(f"```{os.path.splitext(f['file'])[1].lstrip('.')} \n{f['content']}\n```\n")
    return "\n".join(lines)
