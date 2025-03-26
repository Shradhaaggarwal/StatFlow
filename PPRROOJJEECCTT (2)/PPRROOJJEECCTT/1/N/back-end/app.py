from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import geopandas as gpd
# import cufflinks as cf
import plotly.offline as pyo
import plotly.graph_objs as go
import time 
import plotly.express as px

app = Flask(__name__, template_folder='template')
app.config['UPLOAD_DIRECTORY'] = "C:/Users/shrad/OneDrive/Desktop/PPRROOJJEECCTT"  # Change this to your desktop path
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024  # 25MB

@app.route('/')
def index():
    return render_template('index.html')

def check():
    file_path = "C:/Users/shrad/OneDrive/Desktop/PPRROOJJEECCTT/Hello.xlsx"

    if os.path.exists(file_path):
        df = pd.read_excel(file_path)


    # Your code to process the Excel file goes here
    # For example, print the first few rows of the DataFrame
        print(df.head())
        #bar graph
        x=df['Continent']
        y=df['Average IQ']
        plt.bar(x, y)

        plt.xlabel('Continent')
        plt.ylabel('Average IQ')
        plt.title('Bar Graph Example')

        plt.xticks(rotation=45) 
        plt.show() 

        time.sleep(5) 

        #line chart
        m=df['Literacy Rate']
        n=df['Average IQ']
        plt.plot(n, m)

        plt.xlabel('X-axis Label')
        plt.ylabel('Y-axis Label')
        plt.title('Line Chart Example')

        plt.show()
        time.sleep(5)

        
        #scatter plot
        plt.scatter(x, y)

        plt.xlabel('X-axis Label')
        plt.ylabel('Y-axis Label')
        plt.title('Scatter Plot Example')
        plt.xticks(rotation=45) 

        plt.show()
        time.sleep(5) 

        sns.boxplot(df['Average IQ'])
        plt.show()
        time.sleep(5)

        #histogram

        sns.histplot(df['Average IQ'])
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram Example')

        plt.show()
        time.sleep(5)

        #kdep with hist 
        sns.histplot(df['Average IQ'], kde=True, bins=10, color='skyblue', edgecolor='black')

        plt.xlabel('Values')
        plt.ylabel('Frequency/Density')
        plt.title('Histogram with Kernel Density Estimate Plot Example')

        plt.show()
        time.sleep(5)

        #kernal density estimate plot 
        sns.kdeplot(df['Average IQ'], shade=True)

        plt.xlabel('Values')
        plt.ylabel('Density')
        plt.title('Kernel Density Estimate Plot Example')

        plt.show()
        time.sleep(5)

        sns.stripplot(x=df['Average IQ'])
        time.sleep(5)

        df.iplot(kind='scatter', x='Country', y='Average IQ', mode='markers', colorscale='set1',
         title='Interative Plot',xaxis_title='Country', yaxis_title='Average IQ')
        time.sleep(5)

        fig = px.choropleth(df, locations='Country', locationmode='country names', color='Average IQ', hover_name='Country', range_color=(40, 110), title='Average IQ')
        fig.show()
        time.sleep(5)

        df.iplot(kind='pie', labels='Continent', values='Average IQ', textinfo='percent+label', title='Pie Chart Example')
        time.sleep(5)

        df.iplot(kind='pie', labels='Country', values='Average IQ', textinfo='percent+label', title='Pie Chart Example')
        time.sleep(5)


    else:
        print("File does not exist.")


@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1].lower()
        
        
        if file:
            custom_filename = 'Hello' + os.path.splitext(file.filename)[1].lower()
            # if extension not in app.config['ALLOWED_EXTENSIONS']:
            #     return 'File is not a CSV file.'
            file.save(os.path.join(
                app.config['UPLOAD_DIRECTORY'],
                secure_filename(custom_filename)
                
            ))
            check()
            
        
    except RequestEntityTooLarge:
        return 'The file size exceeds the limit of 25 MB.'
    

    

    

    return redirect('/')

@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/team.html')
def team():
    return render_template('team.html')




if __name__ == '__main__':
    app.run(debug=True)


    
    
