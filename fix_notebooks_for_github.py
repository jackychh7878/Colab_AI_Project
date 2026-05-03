"""
Make notebooks render on GitHub without 'Invalid Notebook' / missing
application/vnd.jupyter.widget-state+json errors.

Hugging Face / tqdm often save progress bars as ipywidget display_data. GitHub's
renderer requires valid widget *state* in notebook metadata, which Colab often
omits. This script:

  1. Removes application/vnd.jupyter.widget-view+json from cell outputs only.
  2. Keeps text/plain, images, HTML, and all other MIME types (your results stay).
  3. Removes broken metadata.widgets blobs that confuse GitHub.

Run from repo root:  python fix_notebooks_for_github.py
Optional:  python fix_notebooks_for_github.py path/to/file.ipynb
"""

from __future__ import annotations

import sys
from pathlib import Path

import nbformat

WIDGET_VIEW = "application/vnd.jupyter.widget-view+json"


def fix_notebook_node(nb) -> int:
    """Return count of widget-view MIME bundles removed."""
    removed = 0
    for cell in nb.cells:
        if cell.get("cell_type") != "code":
            continue
        outputs = cell.get("outputs")
        if not outputs:
            continue
        new_outputs = []
        for out in outputs:
            otype = out.get("output_type")
            if otype in ("display_data", "execute_result"):
                data = out.get("data")
                if isinstance(data, dict) and WIDGET_VIEW in data:
                    del data[WIDGET_VIEW]
                    removed += 1
                if isinstance(data, dict) and not data:
                    # No remaining renderable data (widget-only line)
                    continue
            new_outputs.append(out)
        cell["outputs"] = new_outputs

    if "widgets" in nb.metadata:
        del nb.metadata["widgets"]

    return removed


def main() -> None:
    root = Path(__file__).resolve().parent
    if len(sys.argv) > 1:
        paths = [Path(p) for p in sys.argv[1:]]
    else:
        paths = sorted(root.glob("*.ipynb"))
        paths = [p for p in paths if p.name != "clear_format.ipynb"]

    if not paths:
        print("No notebooks found.")
        return

    for path in paths:
        if not path.is_file():
            print(f"Skip (not a file): {path}")
            continue
        nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
        n = fix_notebook_node(nb)
        nbformat.write(nb, path)
        print(f"{path.name}: removed {n} widget-view bundle(s), cleared metadata.widgets if present")


if __name__ == "__main__":
    main()
