from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
import pandas as pd
from typing import Optional
app=FastAPI()
templates=Jinja2Templates(directory='Templates')


@app.get('/')
def home(request:Request):
    return templates.TemplateResponse('home.html',context={'request':request})

@app.post('/')
def home(request:Request,product_name:str=Form(...),submit:Optional[str]=Form(None)):
    df=pd.read_excel('output_data.xlsx')
    df.set_index('Product name in Flipkart',inplace=True)
    
    
    if submit=='submit' and product_name!=None:
        ret_df=df.loc[product_name]
        ret_df=pd.DataFrame(ret_df)

    return templates.TemplateResponse('home.html',context={'request':request,'ret_df':ret_df.to_html()})