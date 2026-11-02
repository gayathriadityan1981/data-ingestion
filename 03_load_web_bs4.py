"""
03_load_web_bs4.py
------------------
Concept: Web Page Loader (BeautifulSoup)

Goal:
Extract text content from a live web page using LangChain’s
`BSHTMLLoader` — ideal for static web scraping.

LangChain Concept:
HTMLLoader → Document[]
"""

from langchain_community.document_loaders import BSHTMLLoader
import tempfile, requests, os

print("\n🌐 WEB LOADER (BS4) DEMO\n" + "-" * 40)

# Example page (you can replace)
url = "https://langchain.com/"
html = requests.get(url).text

# Save temporarily
tmp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".html").name
'''
Creates a new, empty temporary file on your computer.
The file will have a random name and end with .html (so it looks like an HTML file).
delete=False means the file will NOT be deleted automatically when closed.
.name gives you the full path (location) of this new file and saves it in tmp_path.
'''
with open(tmp_path, "w", encoding="utf-8") as f:
    f.write(html)
'''
Opens the temporary file you just created, in “write” mode ("w"), so you can put text into it.
encoding="utf-8" ensures it can handle all kinds of characters (including emojis, non-English letters, etc.).
f.write(html) writes the HTML content you downloaded from the web page into this file.
The with block automatically closes the file when done (good practice).
'''    

# Load using BS4 loader
# loader = BSHTMLLoader(tmp_path)
# loader = BSHTMLLoader(html)
    
loader = BSHTMLLoader(tmp_path, open_encoding="utf-8")    
docs = loader.load()

print(f"✅ Loaded {len(docs)} document(s) from {url}")
print(f"📄 Content snippet:\n{docs[0].page_content[1000:1200]}...\n")

print("""
----------------------------------------
📘 Key Takeaways:
1️⃣ BSHTMLLoader cleans and parses HTML via BeautifulSoup.
2️⃣ Great for extracting readable content from static pages.
3️⃣ Use responsibly — avoid scraping dynamic or restricted sites.
""")


'''
Uses: BSHTMLLoader (BeautifulSoup)

How it works: Downloads the web page HTML, saves it to a file, and uses BeautifulSoup to extract readable text.
Best for: Simple, static web pages (like blogs, articles, documentation) where the main content is in the HTML and not hidden behind JavaScript.
Pros:
Fast and lightweight.
Good for basic text extraction.
Cons:
May include navigation bars, ads, or other “noise.”
Not great for complex or highly dynamic sites.
'''