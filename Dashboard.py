import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os
import shutil
import random

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, mm

import fitz
from PIL import Image

from datetime import datetime


# Open the PDF file

df = pd.read_excel(r"C:\Users\viral.sherathiya\OneDrive - Online PSB Loans\JanSuraksha Tracker\Meeting Tracker with Banks.xlsx", sheet_name='Data')

df['Bank Name'] = df['Bank Name'].str.strip()
df['Particulars'] = df['Particulars'].str.strip()


particular_map = {'SBI Life Insurance Co. Ltd':'<b>SBI Life Insurance</b>',
 'National Insurance Co. Ltd':'<b>National Insurance</b>',
 'IndiaFirst Life Insurance Company Ltd':'<b>IndiaFirst Life Insurance</b>',
 'Overall':'Overall',
 'Life Insurance Corporation of India':'<b>LIC of India</b>',
 "United India Insurance Co Ltd":"United India Insurance",
 "New India Assurance Co Ltd":"New India Assurance",
 "Star Union dai-ichi Life Insurance Co. Ltd":"Star Union dai-ichi Life Insurance",
 "Canara HSBC OBC Life Ins Co Ltd":"Canara HSBC OBC Life Ins",
 "Future Generalli India Assurance Ltd":"Future Generalli India Assurance",
 "The Oriental Insurance Co. Ltd":"The Oriental Insurance",
 "ICICI Prudential Life Insurance Co. Ltd":"ICICI Prudential Life Insurance",
 "ICICI Lombard General Insurance Co Ltd":"ICICI Lombard General Insurance",
 "Star Union dai-ichi Life Insurance Co. Ltd":"Star Union dai-ichi Life Insurance",
 "Universal Sompo General Insurance Co Ltd":"Universal Sompo General Insurance"
 }
df['Particulars'] = df['Particulars'].replace(particular_map)

particular_map_values = ['<b>State Bank of India</b>', '<b>SBI Life Insurance</b>', '<b>National Insurance</b>', '<b>Overall</b>', '<b>Bank of Baroda</b>', '<b>IndiaFirst Life<br>Insurance</b>', '<b>Indian Bank</b>', '<b>LIC of India</b>', '<b>United India Insurance</b>', '<b>Central Bank of India</b>', '<b>New India Assurance</b>', '<b>Union Bank of India</b>', '<b>Star Union dai-ichi<br>Life Insurance</b>', '<b>Canara Bank</b>', '<b>Canara HSBC<br>OBC Life Ins</b>', '<b>UCO Bank</b>', '<b>Future Generalli<br>India Assurance</b>', '<b>Punjab National Bank</b>', '<b>The Oriental Insurance</b>', '<b>Punjab & Sind Bank</b>', '<b>ICICI Bank</b>', '<b>ICICI Prudential<br>Life Insurance</b>', '<b>ICICI Lombard<br>General Insurance</b>', '<b>HDFC Bank</b>', '<b>HDFC Life</b>', '<b>HDFC Ergo</b>', '<b>Bank of India</b>', '<b>Bank of Maharashtra</b>', '<b>Indian Overseas bank</b>', '<b>Universal Sompo<br>General Insurance</b>']

particular_map_keys = ['State Bank of India', '<b>SBI Life Insurance</b>', '<b>National Insurance</b>', 'Overall', 'Bank of Baroda', '<b>IndiaFirst Life Insurance</b>', 'Indian Bank', '<b>LIC of India</b>', 'United India Insurance', 'Central Bank of India', 'New India Assurance', 'Union Bank of India', 'Star Union dai-ichi Life Insurance', 'Canara Bank', 'Canara HSBC OBC Life Ins', 'UCO Bank', 'Future Generalli India Assurance', 'Punjab National Bank', 'The Oriental Insurance', 'Punjab & Sind Bank', 'ICICI Bank', 'ICICI Prudential Life Insurance', 'ICICI Lombard General Insurance', 'HDFC Bank', 'HDFC Life', 'HDFC Ergo', 'Bank of India', 'Bank of Maharashtra', 'Indian Overseas bank', 'Universal Sompo General Insurance']
particular_map = {key: value for key, value in zip(particular_map_keys, particular_map_values)}



    

df['Particulars'] = df['Particulars'].replace(particular_map)

def Gauge_chart(bank, x, y):
    val = df[(df['Bank Name'] == bank) & (df['Particulars'] == '<b>Overall</b>')]['Progress'].values[0] * 100
    fig = go.Figure(go.Indicator(
        mode = "gauge",
        value = round(val),
        title = {'text': f"<b>{bank}</b>",'font': {
            'size': 20,
            'family': 'Arial',
            'color' : '#000000'
        }},
        gauge = {
            'axis': {'range': [0, 100], 'visible': False, 'tickmode': 'array', 'tickvals': [0, 100]},
            'bar': {'color': '#f6bb35', 'thickness': 1, 'line': {'color': '#f6bb35', 'width': 0}},
        }
    ))
    
    fig.update_layout(
        annotations=[
            go.layout.Annotation(
                x=0.5,
                y=0.3,
                text=f'<b>Overall</b><br><b>{round(val)}%</b>',
                showarrow=False,
                font={'size': 20}
            )
        ],
        width=chart_width_gauge,
        height=chart_height_gauge,
        margin=dict(l=4, r=4, t=4, b=4),
        
    )

    path = f'img/gauge/{bank}.png'
    fig.write_image(path)
    c.rect(x, y , chart_width_gauge, chart_height_gauge, stroke=1, fill=0)  # add the box
    c.drawInlineImage(f'img/gauge/{bank}.png', x , y , chart_width_gauge, chart_height_gauge)


def Bar_chart(bank, x, y):
    data = df[df['Bank Name']==bank]
    data = data.drop(data[data['Particulars']=='<b>Overall</b>'].index)
    
    fig = px.bar(data_frame=data, x='Particulars', y='Progress')
    fig.update_layout(
        title = {'text': f'<b>{bank}</b>',
        'font': {
            'size': 20,
            'family': 'Arial',
            'color' : '#000000'
        },
        'y': 0.95,
        'x': 0.5,
    },
        width=chart_width_bar,
        height=chart_height_bar,
        margin=dict(l=4, r=4, t=4, b=4),
        xaxis=dict(
            tickfont=dict(
                size=13,  # increase the font size
                color='black'
            ),
            tickangle=0,
            tickmode='array',  # set tickmode to array
            ticktext=data['Particulars'],  # set ticktext to the values in Particulars column
            automargin=True,
        ),
        xaxis_title = None,
        yaxis=dict(
            range=[0, 1.24],
            tickfont=dict(
                size=11,
                color='black',
            ),
            ticks='',
            showticklabels=False
        ),
        font=dict(
            size=13,
            color='black',
            
        ),
        plot_bgcolor='white'
    )
    
    fig.update_traces(
        marker_color = '#24699e',
        texttemplate='<b>%{y:.0%}</b>', 
        textposition='outside',
        textfont=dict(size=14)
    )
    path = f'img/bar/{bank}.png'
    fig.write_image(path)
    # fig.close()
    c.rect(x, y , chart_width_bar, chart_height_bar,stroke=1, fill=0)  # add the box
    c.drawInlineImage(f'img/bar/{bank}.png', x , y , chart_width_bar, chart_height_bar)



chart_width_gauge = 4.5 * inch
chart_height_gauge = 3.5 * inch
chart_width_bar = 7.5 * inch
chart_height_bar = 5 * inch
# print(df['Bank Name'].unique())


os.makedirs('img',exist_ok=True)
os.makedirs('img/gauge',exist_ok=True)
os.makedirs('img/bar',exist_ok=True)
c = canvas.Canvas("Dashboard_single.pdf", pagesize=(8.5 * inch , 9.4 * inch))
c.setLineWidth(3)
# color = '#6082c0'
##########################################################################################################
for i in range(len(df['Bank Name'].unique())):
    
    Gauge_chart(df['Bank Name'].unique()[i], 2*inch, 5.5*inch)
    Bar_chart(df['Bank Name'].unique()[i], .5*inch, 0.25*inch)
    if i ==13:
        break
    c.showPage()
    c.setLineWidth(3)

##########################################################################################################

c.save()


Banks = df['Bank Name'].unique()


# Delete folder and its contents
# shutil.rmtree('img')
pdf_file = 'Dashboard_single.pdf'
doc = fitz.open(pdf_file)
# Iterate over all the pages of the PDF
for page_idx in range(doc.page_count):
    # Get the page object
    page = doc[page_idx]
    
    # Convert the PDF page to a JPEG image
    mat = fitz.Matrix(300/72, 300/72)
    pix = page.get_pixmap(matrix=mat)
    
    os.makedirs(f'img/banks',exist_ok=True)
    output_folder = f'img/banks'
    # Save the Pixmap object as a JPEG image with a specific quality
    output_file = f'{output_folder}/{Banks[page_idx]}.jpg'  # e.g., page1.jpg, page2.jpg, etc.
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    im.save(output_file, quality=80)

# Close the PDF file
doc.close()



df = pd.read_excel(r"C:\Users\viral.sherathiya\OneDrive - Online PSB Loans\JanSuraksha Tracker\Meeting Tracker with Banks.xlsx", sheet_name='Data')

df['Bank Name'] = df['Bank Name'].str.strip()
df['Particulars'] = df['Particulars'].str.strip()


particular_map = {'SBI Life Insurance Co. Ltd':'<b>SBI Life Insurance</b>',
 'National Insurance Co. Ltd':'<b>National Insurance</b>',
 'IndiaFirst Life Insurance Company Ltd':'<b>IndiaFirst Life Insurance</b>',
 'Overall':'Overall',
 'Life Insurance Corporation of India':'<b>LIC of India</b>',
 "United India Insurance Co Ltd":"United India Insurance",
 "New India Assurance Co Ltd":"New India Assurance",
 "Star Union dai-ichi Life Insurance Co. Ltd":"Star Union dai-ichi Life Insurance",
 "Canara HSBC OBC Life Ins Co Ltd":"Canara HSBC OBC Life Ins",
 "Future Generalli India Assurance Ltd":"Future Generalli India Assurance",
 "The Oriental Insurance Co. Ltd":"The Oriental Insurance",
 "ICICI Prudential Life Insurance Co. Ltd":"ICICI Prudential Life Insurance",
 "ICICI Lombard General Insurance Co Ltd":"ICICI Lombard General Insurance",
 "Star Union dai-ichi Life Insurance Co. Ltd":"Star Union dai-ichi Life Insurance",
 "Universal Sompo General Insurance Co Ltd":"Universal Sompo General Insurance"
 }

df['Particulars'] = df['Particulars'].replace(particular_map)

particular_map = {
    'State Bank of India': '<b>State Bank<br>of India</b>',
    '<b>SBI Life Insurance</b>': '<b>SBI Life<br>Insurance</b>',
    '<b>National Insurance</b>': '<b>National Insurance</b>',
    'Overall': '<b>Overall</b>',
    'Bank of Baroda': '<b>Bank of<br>Baroda</b>',
    '<b>IndiaFirst Life Insurance</b>': '<b>IndiaFirst Life<br>Insurance</b>',
    'Indian Bank': '<b>Indian Bank</b>',
    '<b>LIC of India</b>': '<b>LIC of<br>India</b>',
    'United India Insurance': '<b>United India<br>Insurance</b>',
    'Central Bank of India': '<b>Central Bank<br>of India</b>',
    'New India Assurance': '<b>New India<br>Assurance</b>',
    'Union Bank of India': '<b>Union Bank<br>of India</b>',
    'Star Union dai-ichi Life Insurance': '<b>Star Union<br>dai-ichi<br>Life Insurance</b>',
    'Canara Bank': '<b>Canara Bank</b>',
    'Canara HSBC OBC Life Ins': '<b>Canara HSBC<br>OBC Life<br>Ins</b>',
    'UCO Bank': '<b>UCO Bank</b>',
    'Future Generalli India Assurance': '<b>Future Generalli<br>India Assurance</b>',
    'Punjab National Bank': '<b>Punjab National<br>Bank</b>',
    'The Oriental Insurance': '<b>The <br>Insurance</b>',
    'Punjab & Sind Bank': '<b>Punjab & Sind Bank</b>',
    'ICICI Bank': '<b>ICICI Bank</b>',
    'ICICI Prudential Life Insurance': '<b>ICICI Prudential<br>Life Insurance</b>',
    'ICICI Lombard General Insurance': '<b>ICICI Lombard<br>General Insurance</b>',
    'HDFC Bank': '<b>HDFC Bank</b>',
    'HDFC Life': '<b>HDFC Life</b>',
    'HDFC Ergo': '<b>HDFC Ergo</b>',
    'Bank of India': '<b>Bank of India</b>',
    'Bank of Maharashtra': '<b>Bank of Maharashtra</b>',
    'Indian Overseas bank': '<b>Indian Overseas bank</b>',
    'Universal Sompo General Insurance': '<b>Universal Sompo<br>General Insurance</b>'
}


df['Particulars'] = df['Particulars'].replace(particular_map)

import os
from PIL import Image
import fitz
from reportlab.lib.pagesizes import inch
from reportlab.pdfgen import canvas

# Define the chart sizes
chart_width_gauge = 5 * inch
chart_height_gauge = 2.5 * inch
chart_width_bar = 6 * inch
chart_height_bar = 3.5 * inch

# Define the page size
page_width = 33.2 * inch
page_height = 8 * inch

c = canvas.Canvas("Dashboard_combined.pdf", pagesize=(page_width, page_height))

c.setLineWidth(3)
Gauge_chart('State Bank of India', 1*inch, 4*inch)
Bar_chart('State Bank of India', 0.5*inch, 0.25*inch)

Gauge_chart('Bank of Baroda', 7.5*inch, 4*inch)
Bar_chart('Bank of Baroda', 7*inch, 0.25*inch)

Gauge_chart('Indian Bank', 14*inch, 4*inch)
Bar_chart('Indian Bank', 13.5*inch, 0.25*inch)

Gauge_chart('Central Bank of India', 20.5*inch, 4*inch)
Bar_chart('Central Bank of India', 20*inch, 0.25*inch)

Gauge_chart('Union Bank of India', 27*inch, 4*inch)
Bar_chart('Union Bank of India', 26.5*inch, 0.25*inch)

c.showPage()

# Page 2
c.setLineWidth(3)

Gauge_chart('Canara Bank',1*inch, 4*inch)
Bar_chart('Canara Bank', 0.5*inch, 0.25*inch)

Gauge_chart('UCO Bank', 7.5*inch, 4*inch)
Bar_chart('UCO Bank',7*inch, 0.25*inch)

Gauge_chart('Punjab National Bank', 14*inch, 4*inch)
Bar_chart('Punjab National Bank', 13.5*inch, 0.25*inch)

Gauge_chart('Punjab & Sind Bank', 20.5*inch, 4*inch)
Bar_chart('Punjab & Sind Bank', 20*inch, 0.25*inch)

Gauge_chart('ICICI Bank',  27*inch, 4*inch)
Bar_chart('ICICI Bank', 26.5*inch, 0.25*inch)
c.showPage()

# Page 3
c.setLineWidth(3)


Gauge_chart('HDFC Bank', 1*inch, 4*inch)
Bar_chart('HDFC Bank', 0.5*inch, 0.25*inch)

Gauge_chart('Bank of India', 7.5*inch, 4*inch)
Bar_chart('Bank of India', 7*inch, 0.25*inch)

Gauge_chart('Bank of Maharashtra', 14*inch, 4*inch)
Bar_chart('Bank of Maharashtra', 13.5*inch, 0.25*inch)

Gauge_chart('Indian Overseas bank',20.5*inch, 4*inch)
Bar_chart('Indian Overseas bank', 20*inch, 0.25*inch)

c.showPage()

c.save()


bank_three = ['PNB_UBI_INB','BOB_SBI-s_SBI-m','CNB_CBI_PSB']
# Delete folder and its contents
# shutil.rmtree('img')
pdf_file = 'Dashboard_combined.pdf'
doc = fitz.open(pdf_file)
# Iterate over all the pages of the PDF
for page_idx in range(doc.page_count):
    # Get the page object
    page = doc[page_idx]
    
    # Convert the PDF page to a JPEG image
    mat = fitz.Matrix(300/72, 300/72)
    pix = page.get_pixmap(matrix=mat)
    
    os.makedirs(f'management',exist_ok=True)
    output_folder = f'management'
    # Save the Pixmap object as a JPEG image with a specific quality
    output_file = f'{output_folder}/{bank_three[page_idx]}.jpg'  # e.g., page1.jpg, page2.jpg, etc.
    im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    im.save(output_file, quality=80)

# Close the PDF file
doc.close()


