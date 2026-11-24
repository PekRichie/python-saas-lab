"""HTML-escape-elt tranzakciós e-mail sablonmotor."""
import html, re

VAR_RE = re.compile(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}")


def render_template(template: str, context: dict[str, str], escape_html: bool = True) -> str:
    required = set(VAR_RE.findall(template))
    missing = required - set(context.keys())
    if missing:
        raise KeyError(f"Hiányzó sablonváltozók: {sorted(missing)}")
    def repl(m):
        val = str(context[m.group(1)])
        return html.escape(val) if escape_html else val
    return VAR_RE.sub(repl, template)
