"""
highlighted_code_extension.py
=============================

This module defines a custom Markdown extension for syntax highlighting using Pygments.

It enables language-aware syntax highlighting for both indented and fenced code blocks
by injecting HTML with appropriate language-specific CSS classes (`language-<lang>`).

Components:
-----------
- HighlightedCodePreprocessor: Parses and transforms fenced code blocks into highlighted HTML.
- CodeHiliteWithLanguage: A Markdown extension that registers the preprocessor into the Markdown parser.

Usage:
------
Include this extension when converting Markdown:

    import markdown
    from highlighted_code_extension import CodeHiliteWithLanguage

    html = markdown.markdown(
        markdown_text,
        extensions=[CodeHiliteWithLanguage()]
    )
"""

import re
import textwrap
from typing import List
import markdown
from markdown.extensions import Extension
from markdown.extensions.codehilite import CodeHilite
from markdown.preprocessors import Preprocessor


class HighlightedCodePreprocessor(Preprocessor):
    """
    A Markdown preprocessor that highlights indented or fenced code blocks.

    Adds syntax highlighting using Pygments and injects language-specific CSS classes.
    """

    fenced_block_regex: re.Pattern = re.compile(
        r'(?P<indent>[ \t]*)'
        r'(?P<fence>`{3,}|~{3,})[ \t]*'
        r'(?P<lang>\w+)?(?P<opts>[^\n]*?)[ \t]*\n'
        r'(?P<code>.*?)(?=\n(?P=indent)(?P=fence)[ \t]*$)\n(?P=indent)(?P=fence)[ \t]*$',
        re.MULTILINE | re.DOTALL
    )

    def __init__(self, markdown_instance: markdown.Markdown, config: dict) -> None:
        super().__init__(markdown_instance)
        self.config: dict = config

    def run(self, markdown_lines: List[str]) -> List[str]:
        """Process all markdown lines and replace fenced blocks with highlighted HTML."""
        content: str = "\n".join(markdown_lines)

        def highlight_match(match: re.Match) -> str:
            indent = match.group('indent') or ''
            language = match.group('lang') or ''
            code = textwrap.dedent(match.group('code'))

            highlighter = CodeHilite(
                src=code,
                lang=language,
                linenums=self.config.get('linenums', False),
                guess_lang=self.config.get('guess_lang', False),
                use_pygments=self.config.get('use_pygments', True),
                noclasses=self.config.get('noclasses', False),
            )
            highlighted = highlighter.hilite()

            # « ```python norun » : bloc non exécutable dans les cours
            run_attr = ' data-run="false"' if 'norun' in (match.group('opts') or '') else ''

            if language:
                highlighted = re.sub(
                    r'<code(.*?)>',
                    f'<code\\1 class="language-{language}"{run_attr}>',
                    highlighted
                )

            return '\n'.join(indent + line if line.strip() else line for line in highlighted.splitlines())

        return self.fenced_block_regex.sub(highlight_match, content).split('\n')


class CodeHiliteWithLanguage(Extension):
    """
    Markdown extension that enables Pygments highlighting and adds language-<lang> classes.
    """

    def __init__(self, **kwargs) -> None:
        self.config = {
            'linenums': [False, 'Show line numbers'],
            'guess_lang': [False, 'Guess language if not specified'],
            'use_pygments': [True, 'Use Pygments for syntax highlighting'],
            'noclasses': [False, 'Use inline styles instead of CSS classes'],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md: markdown.Markdown) -> None:
        """Register the syntax highlighter preprocessor."""
        md.registerExtension(self)
        md.preprocessors.register(
            HighlightedCodePreprocessor(md, self.getConfigs()),
            'fenced_code_block',
            25
        )
