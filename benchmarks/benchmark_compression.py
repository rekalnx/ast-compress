"""Benchmark Compression Savings across Languages."""
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ast_compress import compress_python, compress_javascript

def run():
    print("=== ast-compress Token Compression Benchmark ===")
    sample_py = """
class DataPipeline:
    def __init__(self, conn_str: str):
        self.conn = conn_str
        self.cache = {}
        self.is_active = True

    def process_records(self, records: list) -> dict:
        \"\"\"Process raw batches into sanitized records.\"\"\"
        out = {}
        for r in records:
            if not r.get('valid'): continue
            clean = r['val'].strip().lower()
            out[r['id']] = clean
        return out

    def flush_cache(self) -> None:
        self.cache.clear()
""" * 50

    t0 = time.perf_counter()
    res = compress_python(sample_py)
    dt = (time.perf_counter() - t0) * 1000

    orig_len = len(sample_py)
    comp_len = len(res)
    savings = (1.0 - (comp_len / orig_len)) * 100

    print(f"[*] Original: {orig_len:,} chars (~{orig_len//4:,} tokens)")
    print(f"[*] Compressed: {comp_len:,} chars (~{comp_len//4:,} tokens)")
    print(f"[*] Saved: {savings:.2f}% | Latency: {dt:.2f} ms")

if __name__ == "__main__":
    run()
