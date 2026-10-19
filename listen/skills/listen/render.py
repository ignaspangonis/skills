import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

KINDS = {
    "context": "Where we are",
    "problem": "The problem",
    "options": "Options",
    "pick": "My pick",
    "question": "Your call",
    "next": "What happens next",
}

data = json.load(sys.stdin)
root = Path(os.environ.get("TMPDIR") or tempfile.gettempdir()) / "claude-listen"
run = root / datetime.now().strftime("%Y%m%d-%H%M%S")
run.mkdir(parents=True, exist_ok=True)

voice = ["-v", os.environ["LISTEN_VOICE"]] if os.environ.get("LISTEN_VOICE") else []
rate = os.environ.get("LISTEN_RATE", "170")

def synthesize(index, text):
    base = run / str(index)
    base.with_suffix(".txt").write_text(text)
    subprocess.run(
        ["say", *voice, "-r", rate, "-o", str(base.with_suffix(".aiff")), "-f", str(base.with_suffix(".txt"))],
        check=True,
    )
    subprocess.run(
        ["afconvert", "-f", "m4af", "-d", "aac", str(base.with_suffix(".aiff")), str(base.with_suffix(".m4a"))],
        check=True,
    )


with ThreadPoolExecutor() as pool:
    list(pool.map(synthesize, range(len(data["sections"])), [section["say"] for section in data["sections"]]))

sections = []
for index, section in enumerate(data["sections"]):
    kind = section.get("kind", "context")
    sections.append(
        {
            "kind": kind,
            "label": section.get("label") or KINDS.get(kind, kind.title()),
            "say": section["say"],
            "show": section.get("show", ""),
            "audio": f"{index}.m4a",
        }
    )

payload = json.dumps({"title": data.get("title", "Listen"), "sections": sections}).replace("</", "<\\/")
template = (Path(__file__).parent / "page.html").read_text()
page = run / "index.html"
page.write_text(template.replace("__TITLE__", data.get("title", "Listen")).replace("__DATA__", payload))

subprocess.run(["open", str(page)], check=True)
print(page)
