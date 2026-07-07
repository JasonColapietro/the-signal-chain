import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import bookkit as bk
import example_build


class BookkitRenderingTests(unittest.TestCase):
    def test_inline_escapes_html(self):
        rendered = bk.inline("A <script>alert(1)</script> riff")
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", rendered)
        self.assertNotIn("<script>", rendered)

    def test_fenced_code_becomes_tab_block(self):
        html = bk.render_blocks(["# Lesson 1 - Test", "", "```text", "e|--0--|", "```"])
        self.assertIn('<pre class="tab"><code>e|--0--|</code></pre>', html)

    def test_markdown_links_are_rendered(self):
        html = bk.render_blocks(["See [Guitar Solutions](https://guitar.solutions)."])
        self.assertIn('<a href="https://guitar.solutions">Guitar Solutions</a>', html)

    def test_example_builder_outputs_self_contained_html(self):
        sample = "# Show HN Sample\n\nParagraph.\n"
        html = example_build.render_markdown(sample, "Sample")
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn('<section class="chapter" id="show-hn-sample">', html)
        self.assertIn("Show HN Sample", html)
        self.assertIn("<style>", html)


if __name__ == "__main__":
    unittest.main()
