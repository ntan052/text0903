#!/usr/bin/env python
# coding: utf-8

# In[19]:


from flask import Flask, request, render_template


# In[20]:


app = Flask(__name__)


# In[21]:


#!pip install textblob, installed already so hash it


# In[22]:


from textblob import TextBlob

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




