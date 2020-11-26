import markdown, os, json

files = os.listdir()


header = """
# Index main page
"""

def gen_markdown():
    files = os.listdir()
    links = [f"[{path}]({path})" for path in files]
    return header + "\n".join(links)


html = markdown.markdown(gen_markdown())

with open("index.html", "w") as file:
    file.write(html)

