"""Rust Interface Extractor (Structs, Enums, Impl Blocks, Traits, Functions)."""
import re

def compress_rust(source: str) -> str:
    lines = source.splitlines()
    out = []
    for line in lines:
        s = line.strip()
        if not s or s.startswith("//"):
            continue
        if s.startswith("pub fn ") or s.startswith("fn "):
            sig = s.split("{")[0].strip()
            out.append(sig + " { ... }")
        elif s.startswith("pub struct ") or s.startswith("struct ") or s.startswith("pub enum ") or s.startswith("enum "):
            out.append(line)
        elif s.startswith("pub trait ") or s.startswith("trait "):
            out.append(line)
        elif s.startswith("impl ") and "{" in s:
            out.append(s.split("{")[0].strip() + " { ... }")
        elif s.startswith("use ") or s.startswith("pub use "):
            out.append(line)
        elif s == "}":
            out.append(line)
    return "\n".join(out)
