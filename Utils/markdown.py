import markdown
from django.contrib.staticfiles.storage import staticfiles_storage

def readmd(app, filename):
    """
    ## Summary
    Read from App/static/App/markdown/filename.md

    ## Args:
    - `app`
    - `filename`
    """
    try:
        with open(
            staticfiles_storage.path(app + "/markdown/" + filename + ".md")
        ) as f:
            return markdown.markdown(f.read())
    except:
        return "ERROR:日志读取失败"