import markdown, os, json

def gen_markdown():
    files = set(os.listdir()) - {".vscode", "index.py", "css",
    "index.html", ".git", "REAMDE.md"}
    titles = [" ".join(doc.split("-")).title() for doc in files]
    titles = [doc.split(".")[0] for doc in titles]
    links = [f" - [{title}]({path})" for (path, title) in zip(files, titles)]
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

