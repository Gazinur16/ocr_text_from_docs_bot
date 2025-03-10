import markdown
from bs4 import BeautifulSoup

def remove_markdown(text: str) -> str:
    html_text = markdown.markdown(text)
    soup = BeautifulSoup(html_text, "html.parser")
    return soup.get_text(separator="\n\n", strip=True)

