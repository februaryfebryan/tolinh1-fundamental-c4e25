from gmail import *
# Login
gmail = GMail('tophuonglinh12@gmail.com','Chunchun123') 

# Create...
html_content = '''
<p>The most {{ basic }} type of basic query that can be performed in MongoDB is&nbsp;
<a class="reference internal" title="pymongo.collection.Collection.find_one" href="http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one"><code class="xref py py-meth docutils literal"><span class="pre">find_one()</span></code></a>. This method returns a single document matching a query (or&nbsp;<code class="docutils literal"><span class="pre">None</span></code>&nbsp;if there are no matches). It is useful when you know there is only one matching document, or are only interested in the first match. Here we use&nbsp;<a class="reference internal" title="pymongo.collection.Collection.find_one" href="http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one"><code class="xref py py-meth docutils literal"><span class="pre">find_one()</span></code></a>&nbsp;to get the first document from the posts collection:</p>
'''

new_html = html_content.replace('{{ basic }}', 'BASIC')
msg = Message('Test Message',to=' tophuonglinh12@gmail.com',html=new_html)
gmail.send(msg)