import pickle
import pandas as pd
import dash
import dash_html_components as html 
import webbrowser
from dash.dependencies import Input,Output
import dash_core_components as dcc
import sqlite3 as sql
app=dash.Dash()
project_name=None
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")
    #open browser automatically/opening a tab in browser in automation
    
def reading_reviews():
    global df
    df=pd.read_csv("balanced_reviews.csv")
    df=df[df["overall"]!=3]
    global df2
    df2=df.loc[:,"reviewText"].sample(1000)
    conn=sql.connect("reviews2.db")
    global reviews_db
    reviews_db=pd.read_sql_query("SELECT * FROM real_reviews",conn) 
        
def create_app_ui():
    #actually creating a ui of my app
    main_layout=html.Div(
        [
        html.H1(id='Main_title',children=app.title,style={"text-align":"center","font-size":"300%"}),
        dcc.Textarea(id="textarea_review",
                     placeholder="Enter the Review here.....",
                     style={"width":"100%","height":100,"background-color":"indigo","font-size":"160%","font-family":"verdana","color":"yellow","border":"5px solid black"}
                     ),
             dcc.Dropdown(id="review",style={"color":"black","border":"5px solid black"},
                      options=[{"label":i,"value":i}for i in reviews_db["reviews"]],
                      placeholder="Select Review"),
        html.Button(id="button_review",children="find_review",n_clicks=0,style={"background-color":"blue","border":"5px solid black"}),
        html.H1(id="result",children=None,style={"color":"red","border":"5px solid black","background-color":"orange","text-align":"center"})
        ]
        )
    #Div is a container
    return main_layout

@app.callback(
    Output("button_review","value"),
    [
    Input("textarea_review","value"),
    Input("review","value")
    ]
    )
def update_app_ui(textarea_value,value):
    if textarea_value:
            print("Data Type=",str(type(textarea_value)))
            print("Value=",str(textarea_value))
            result_list=check_review(textarea_value)
            textarea_value=None
            if result_list[0]==0:
                result="Negative"     
            elif result_list[0]==1:
                result="Positive"
            return result
    elif value:
            print("Data Type=",str(type(value)))
            print("Value=",str(value))
            result_list=check_review(value)
            value=None
            if result_list[0]==0:
                result="Negative"     
            elif result_list[0]==1:
                result="Positive"
            return result
@app.callback(
    Output("result","children"),
    [
    Input("button_review","value"),
    Input("button_review","n_clicks")
    ]
    )
def update_button_review(value,clicks):
    if clicks>0 and value: 
        if value=="Positive":
            return value
        elif value=="Negative":
            return value       
@app.callback(
    Output("button_review","n_clicks"),
    [
     Input("button_review","value")
     ]
    )
def n_click(value):
    if not value:
        return 0
        
def load_model():
    #loading pickle and csv file in memory
    print("Busy in loading the model in memory")
    global df
    df=pd.read_csv("balanced_reviews.csv")
    file=open("pickle_model.pkl","rb")
    global pickle_model
    pickle_model=pickle.load(file)
    global vocab
    file=open("feature.pkl","rb")
    vocab=pickle.load(file)

def check_review(reviewText):
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.feature_extraction.text import CountVectorizer
    transformer=TfidfTransformer()
    loaded_vec=CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("feature.pkl","rb")))
    reviewText=transformer.fit_transform(loaded_vec.fit_transform([reviewText]))
    return pickle_model.predict(reviewText)
        
def main():
    #controll the flow of project
    #calling of all the function
    print("Welcome to My Project")
    load_model() 
    reading_reviews()
    open_browser()
    global project_name
    project_name="Sentiments Analysis with Insights"
    global app
    app.title=project_name
    #title of project
    app.layout=create_app_ui
    #it gives me a blank webpage control the ui of a webpage
    app.run_server()
    #start the server running infinte times
    print("this wiil not be executed")
    app=None
    project_name=None
    
if __name__=="__main__":
    main()