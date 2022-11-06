import re
import js
import asyncio
from js import navigator
from pyodide import create_proxy


PLACEHOLDER_TEXT = """• `{0}start` to start
• `{0}pick` to pick a starter
• `{0}catch` to catch a pokemon"""


input = document.getElementById('input')
prefix_from = document.getElementById('prefix-from')
prefix_to = document.getElementById('prefix-to')
output_title = document.getElementById('output-title')
output = document.getElementById('output')
submit = document.getElementById('btn-form')
copy = document.getElementById('btn-copy')


def disable_check():
    if len(output.value) == 0:
        disabled = True
    else:
        disabled = False
    copy.disabled = disabled

def select_change(element: str):
    if element == "from":
        p_from = prefix_from.value
        input.placeholder = PLACEHOLDER_TEXT.format(p_from)

    elif element == "to":
        p_to = prefix_to.value
        output.placeholder = PLACEHOLDER_TEXT.format(p_to)

prefix_from.addEventListener("change", create_proxy(lambda *args, **kwargs: select_change("from")))
prefix_to.addEventListener("change", create_proxy(lambda *args, **kwargs: select_change("to")))

def replace(*args, **kwargs):
    prefix_from = document.getElementById('prefix-from')
    prefix_to = document.getElementById('prefix-to')

    pattern = re.compile(f"(\W|^){prefix_from.value}{'?' if prefix_from.value[-1] == ' ' else ''}")
    
    text = pattern.sub(f"\\1{prefix_to.value}", input.value)

    output.innerHTML = text

    disable_check()

def copy_text(*args, **kwargs):
    content = output.value
    navigator.clipboard.writeText(content)