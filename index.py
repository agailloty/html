import markdown, os, json

files = os.listdir()


def gen_markdown():
    files = set(os.listdir()) - {".vscode", "index.py", "css",
    "index.html", ".git", "REAMDE.md"}
    links = [f" - [{path}]({path})" for path in files]
    return " \n ".join(links)


html = markdown.markdown(gen_markdown())

body = f"""
<head> 
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{html}
</body>
"""
with open("index.html", "w") as file:
    file.write(body)

