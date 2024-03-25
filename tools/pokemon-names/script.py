import re
import js
import asyncio
from js import navigator
from pyodide import http

output_title = document.getElementById('output-title')
output = document.getElementById('output')
copy = document.getElementById('btn-copy')
copy_ind = document.getElementById('btn-copy-ind')


def disable_check():
    if len(output.value) == 0:
        disabled = True
    else:
        disabled = False
    copy.disabled = disabled
    copy_ind.disabled = disabled

async def get_ids(*args, **kwargs):
    input = document.getElementById('input').value

    pattern = re.compile(r':?_:? ([\w_.\s-]+):?(?:unknown|male|female):?(?: ".+?")? ?(?::?heart:?|❤️)?　•　Lvl', re.MULTILINE)
    
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
    names = content.split("  ")
    name = names[0]
    navigator.clipboard.writeText(name)
    names.remove(name)
    output_title.innerHTML = f"Output ({len(names)})"
    output.innerHTML = "  ".join(names)

    disable_check()
        
