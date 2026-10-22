"""Unit Test Suite for ast-compress."""
import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ast_compress import compress_python, compress_javascript, compress_golang
from languages.rust_pruner import compress_rust

class TestCompress(unittest.TestCase):
    def test_py_compress(self):
        code = '''
def add(a: int, b: int) -> int:
    """Adds numbers."""
    c = a + b
    return c
'''
        res = compress_python(code)
        self.assertIn("def add", res)
        self.assertNotIn("c = a + b", res)

    def test_js_compress(self):
        code = '''
export class UserService {
    async getUser(id) {
        const u = await db.query(id);
        return u;
    }
}
'''
        res = compress_javascript(code)
        self.assertIn("UserService", res)

    def test_go_compress(self):
        code = '''
package main
type User struct { Name string }
func Process(u User) error {
    return nil
}
'''
        res = compress_golang(code)
        self.assertIn("func Process", res)

    def test_rust_compress(self):
        code = '''
pub struct Engine;
impl Engine {
    pub fn start(&self) -> bool { true }
}
'''
        res = compress_rust(code)
        self.assertIn("pub struct Engine;", res)

if __name__ == "__main__":
    unittest.main()
