import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import base64
from io import BytesIO

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    #print(image_png)
    graph=base64.b64encode(image_png)
    #print(graph)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(20,10))
    plt.title('Visualization of close')
    plt.plot(x,y,color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Trade Code')
    plt.ylabel('Close')
    graph=get_graph()
    return graph
def get_barplot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(20,10))
    plt.title('Visualization of volume')
    plt.plot(x,y,color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
    plt.xlabel('Trade Code')
    plt.ylabel('Volume')
    graph=get_graph()
    return graph    
