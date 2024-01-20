import numpy as np
import pandas as pd
import time
from sklearn import manifold
import matplotlib.pyplot as plt
from IPython.display import display, Markdown
#import plotly.plotly as py
#import plotly as py
#import plotly.graph_objs as go
#import plotly.grid_objs as gro
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

def neighborhoods(a, L, S ):  # Window len = L, Stride len/stepsize = S
    nrows = ((a.size-L)//S)+1
    n = a.strides[0]
    return np.lib.stride_tricks.as_strided(a, shape=(nrows,L), strides=(S*n,n))

def md_print(mystring):
    """Prints some text using Markdown in the Jupyter Notebook Interface    
    """
    display(Markdown(mystring))

def mds(similarities):
    """Computes nonmetric multidimensional scaling on the given
    distances, projecting the data into a 2D space.

    Parameters
    ----------
    distances : dataframe of shape (n, n)
        The distances between points (i.e., with zeros along the diagonal)

    Returns
    -------
    dataframe of shape (n, 2)

    """
    # parameters that are used by both of the MDS runs
    params = {
        'random_state': 23497,
        'eps': 1e-6,
        'max_iter': 500,
        'dissimilarity': "precomputed",
        'n_jobs': 1,
        'n_components': 2
    }

    # first fit the metric MDS, which we will use as initialization
    # for the nonmetric MDS algorithm
    mds = manifold.MDS(metric=True, n_init=1, **params)
    pos = mds.fit(1 - similarities).embedding_

    # now run the nonmetric MDS algorithm
    nmds = manifold.MDS(metric=False, n_init=1, **params)
    pos = nmds.fit_transform(1 - similarities, init=pos)
    
    df = pd.DataFrame(pos, index=similarities.index.copy(), columns=["x", "y"])
    df.index.name = "label"
    return df.reset_index()


def zscore(X):
    """Normalize an array by shifting it by its mean and scaling it
    by its standard deviation.
    
    """
    return (X - X.mean(axis=0)) / X.std(axis=0)


def generate_swiss_roll(N=1000):
    """Generate dataset C with `N` points."""
    np.random.seed(123)
    phi = (3 * np.pi / 2) * (1 + 2 * np.random.rand(N))
    height = 50 * np.random.rand(N)
    data = zscore(np.array([2 * phi * np.cos(phi), height, phi * np.sin(phi)]).T)
    colors = phi.copy()
    return data, colors

def arrayplotbw(data):
    """Plots an binary matrix of 1 and 0s in a pleasing colorscale  
    """
    trace=go.Heatmap(z=np.flipud(data), colorscale=[[0, 'lightgrey'], [1.0, 'black']],xgap=2,ygap=2,showscale=False)
    data=[trace]
    layout = go.Layout(xaxis=dict(scaleanchor='y',visible=False),yaxis=dict(scaleanchor='x',visible=False))
    fig = go.Figure(data=data,layout=layout)
    iplot(fig,filename='myarrayplot'+str(time.time()))

def arrayplot(data):
    """Plots an binary matrix of 1 and 0s in a pleasing colorscale  
    """
    trace=go.Heatmap(z=np.flipud(data), colorscale=[[0, '#d9d9e9'], [1.0, '#9c99c4']],xgap=2,ygap=2,showscale=False)
    data=[trace]
    layout = go.Layout(xaxis=dict(scaleanchor='y',visible=False),yaxis=dict(scaleanchor='x',visible=False))
    fig = go.Figure(data=data,layout=layout)
    iplot(fig,filename='myarrayplot'+str(time.time()))

def arrayplot_animate(df):
    """Creates an animation of a sequence of binary matricies in a pleasing colorscale"""
    frame_titles = df.columns[2:].values.tolist()

    colorscale = [[0, '#d9d9e9'], [1.0, '#9c99c4']]
    
    figure = {
        'data': [],
        'layout': {},
        'frames': [],
        'config': {'scrollzoom': True}
    }

    figure['layout']=dict(autosize=True,
                  xaxis=dict(scaleanchor='y',visible=False),
                  yaxis=dict(scaleanchor='x',visible=False),
                  showlegend=False)

    figure['layout']['slider'] = {'args': [
            'slider.value', {
                'duration': 400,
                'ease':'cubic-in-out'
            }
        ],
        'initialValue': df.columns[2],
        'plotlycommand': 'animate',
        'values': frame_titles,
        'visible': True}

    figure['layout']['updatemenus'] = [
        {
            'buttons': [
                {
                    'args': [None, {'frame': {'duration': 500, 'redraw': True},
                             'fromcurrent': True, 'transition': {'duration': 300}}],
                    'label': 'Play',
                    'method': 'animate'
                },
                {
                    'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate',
                    'transition': {'duration': 0}}],
                    'label': 'Pause',
                    'method': 'animate'
                }
            ],
            'direction': 'left',
            'pad': {'r': 10, 't': 87},
            'showactive': True,
            'type': 'buttons',
            'x': 0.1,
            'xanchor': 'right',
            'y': 0,
            'yanchor': 'top'
        }
    ]

    sliders_dict = {
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 10},
            'prefix': 'Step: ',
            'visible': True,
            'xanchor': 'right'
        },
        'transition': {'duration': 300, 'easing': 'cubic-in-out'},
        'pad': {'b': 10, 't': 50},
        'len': 0.9,
        'x': 0.1,
        'y': 0,
        'steps': []
    }

    figure['layout']['sliders']=[sliders_dict]


    data=[dict(type='heatmap',
               x=df['x'].values.tolist(),
               y=df['y'].values.tolist(), 
               z=df[df.columns[2]].values.tolist(), 
               zmin=0,
               zmax=1.0,
               xgap=2,ygap=2,showscale=False,
               colorscale=colorscale)]

    figure["data"]=data

    frames=[dict(data=[dict(z=df[k].values.tolist(),
                            zmax=1.0)],
                            traces=[0],
                            name=k,
                            ) for k in frame_titles]  

    figure["frames"]=frames
    steps=[dict(method='animate',
        label=k,
        args=[[k],{'frame': {'duration': 300, 'redraw': True},
             'mode': 'immediate'}]
        ) for k in frame_titles]

    figure['layout']['sliders'][0]['steps']=steps

    iplot(figure, filename='myanimation'+str(time.time()),validate=False) # the validate=False thing is apparently a plotly bug

