import os


def bootstrapCard(title, link, imageLink, summary):
    return f'''
    <div class="card" style="width: 18rem;">
  <img class="card-img-top" src="{imageLink}" alt="">
  <div class="card-body">
    <h5 class="card-title">{title}</h5>
    <p class="card-text">{summary}</p>
    <a href="{link}" class="btn btn-primary">Aller</a>
  </div>
</div>
    '''


def genCard():
    files = set(os.listdir()) - {".vscode", "index.py", "css",
                                 "index.html", ".git", "README.md"}
    titles = [" ".join(doc.split("-")).title() for doc in files]
    titles = [doc.split(".")[0] for doc in titles]
    images = [fl + "/featured.jpg" for fl in files]
    return [bootstrapCard(title, link, img, "") for (title, link, img) in zip(titles, files, images)]


def gen_markdown():
    files = set(os.listdir()) - {".vscode", "index.py", "css",
                                 "index.html", ".git", "REAMDE.md"}
    titles = [" ".join(doc.split("-")).title() for doc in files]
    titles = [doc.split(".")[0] for doc in titles]
    links = [f" - [{title}]({path})" for (path, title) in zip(files, titles)]
    return " \n ".join(links)


#html = markdown.markdown(gen_markdown())
html = "\n".join(genCard())

body = f"""
<head> 
<link rel="stylesheet" href="css/style.css">
<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
</head>
<body>
  <div class = "container">
    {html}
  </div>
</body>
"""
with open("index.html", "w") as file:
    file.write(body)
