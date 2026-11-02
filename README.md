pip install torch==2.2.0 --index-url https://download.pytorch.org/whl/cpu
pip install beautifulsoup4
pip install -U lxml
pip install unstructured
set PYTHONUTF8=1              
pip install -U langchain-community bs4
05_compare_laoder.py has below issue

 html = requests.get(url).text
           ^^^^^^^^^^^^^^^^^
  File "C:\Users\gayat\OneDrive\Documents\GenAI-Dev-Projects\data-ingestion\myenv\Lib\site-packages\requests\api.py", line 87, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gayat\OneDrive\Documents\GenAI-Dev-Projects\data-ingestion\myenv\Lib\site-packages\requests\api.py", line 71, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gayat\OneDrive\Documents\GenAI-Dev-Projects\data-ingestion\myenv\Lib\site-packages\requests\sessions.py", line 651, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gayat\OneDrive\Documents\GenAI-Dev-Projects\data-ingestion\myenv\Lib\site-packages\requests\sessions.py", line 784, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gayat\OneDrive\Documents\GenAI-Dev-Projects\data-ingestion\myenv\Lib\site-packages\requests\adapters.py", line 717, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='langchain.com', port=443): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<HTTPSConnection(host='langchain.com', port=443) at 0x1c37195fa10>, 'Connection to langchain.com timed out. (connect timeout=None)'))

https://www.geeksforgeeks.org/python/how-to-fix-connectionerror-max-retries-exceeded-with-url-in-python/

