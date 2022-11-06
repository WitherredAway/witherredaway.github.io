import re
import js
import asyncio
from js import navigator
from pyodide import http

output_title = document.getElementById('output-title')
output = document.getElementById('output')
copy = document.getElementById('btn-copy')
copy_ind = document.getElementById('btn-copy-ind')
prefix = document.getElementById("prefix")


def disable_check():
    if len(output.value) == 0:
        disabled = True
    else:
        disabled = False
    copy.disabled = disabled
    copy_ind.disabled = disabled

async def get_ids(*args, **kwargs):
    input = document.getElementById('input').value

    pattern = re.compile(r"^`?\s*(\d+)`?\b", re.MULTILINE)
    
    ids = pattern.findall(input)

    if len(ids) > 0:
        output_title.innerHTML = f"Output ({len(ids)})"
        output.innerHTML = "  ".join(ids)
    else:
        output.innerHTML = "Improper input provided"

    disable_check()

def copy_text(*args, **kwargs):
    content = output.value
    navigator.clipboard.writeText(content)
    
def copy_text_individual(*args, **kwargs):
    content = output.value
    ids = content.split("  ")
    idx = ids[0]
    navigator.clipboard.writeText(f'{(prefix.value + " ") if len(prefix.value) > 0 else ""}{idx}')
    ids.remove(idx)
    output_title.innerHTML = f"Output ({len(ids)})"
    output.innerHTML = "  ".join(ids)

    disable_check()
        