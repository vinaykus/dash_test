"""Functions to create plots"""
from typing import List, Dict, Any
import numpy as np
import pandas as pd
from dash_core_components import Graph
import plotly.graph_objs as go
"""Function for creating a data table"""
import pandas as pd
from dash_table import DataTable


bar_colors = ['#ffd050', '#fd5a3e', '#97cc64']

def create_donut(labels: List[str], values: List[int]) -> Graph:
    """Create a donut plot"""
    return Graph(style={"height": "26rem"}, figure={
        "data": [go.Pie(labels=labels, values=values,textinfo='label', hole=.2, marker=dict(colors=bar_colors))],
        "layout": go.Layout(
            margin={"l": 60, "r": 60},
            showlegend=True,
            paper_bgcolor="rgb(255,255,255,0)"
        )
    }, config={"displayModeBar": False})


def violin(df: pd.DataFrame, graph_id: str, name: str) -> Graph:
    """Create and return a bar plot"""
    return Graph(id=graph_id, figure=go.Figure(
        data=[go.Violin(y=df[name], name=name)],
        layout=go.Layout(
            showlegend=False,
            legend=go.layout.Legend(x=0, y=1.0),
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)  # noqa (l is an ambigous name)
        )
    ))


def lineplot(df: pd.DataFrame, graph_id: str, x: str, names: List[str], showlegend: bool = False
             ) -> Graph:
    """Create and return a bar plot"""
    x=['Pass', 'Fail', 'Pause', 'Skip']
    return Graph(id=graph_id, figure=go.Figure(
        
        data=[go.Scatter(x=x, y=[40, 20, 30, 50], mode="lines+markers", line=dict(width=0.5, color='rgb(184, 247, 212)'),stackgroup='one',groupnorm='percent'),
              go.Scatter(x=x, y=[50, 70, 40, 60], mode="lines+markers", line=dict(width=0.5, color='rgb(111, 231, 219)'),stackgroup='one',groupnorm='percent'),
              go.Scatter(x=x, y=[470, 80, 60, 70], mode="lines+markers", line=dict(width=0.5, color='rgb(127, 166, 238)'),stackgroup='one',groupnorm='percent'),
              go.Scatter(x=x, y=[100, 100, 100, 100], mode="lines+markers", line=dict(width=0.5, color='rgb(131, 90, 241)'),stackgroup='one',groupnorm='percent'),
             
              ],
        layout=go.Layout(
            showlegend=showlegend,
            autosize=True,
            xaxis_tickangle=-45,
            legend=go.layout.Legend(x=0.9, y=1.0),
            margin=go.layout.Margin(l=40, r=10, t=10, b=30)  # noqa (l is an ambigous name)
        )
    ), config={"displayModeBar": False})


def boxplot(df: pd.DataFrame, graph_id: str, names: List[str], yaxis_type: str = "linear") -> Graph:
    """Create and return a boxplot"""
    return Graph(id=graph_id, figure=go.Figure(
        data=[go.Box(y=df[name], name=name, jitter=0.1) for name in names],
        layout=go.Layout(
            showlegend=False,
            yaxis_type=yaxis_type,
            legend=go.layout.Legend(x=1.0, y=1.0),
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)  # noqa (l is an ambigous name)
        )
    ))


def histogram(df: pd.DataFrame, graph_id: str, names: List[str]) -> Graph:
    """Create and return a boxplot"""
    return Graph(id=graph_id, figure=go.Figure(
        data=[go.Histogram(x=df[name], name=name, opacity=0.8) for name in names],
        layout=go.Layout(
            barmode='overlay',
            legend=go.layout.Legend(x=0, y=1.0),
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)  # noqa (l is an ambigous name)
        )
    ))


def barplot(df: pd.DataFrame, graph_id: str, x: List[str], names: List[str]) -> Graph:
    """Create and return a barplot"""
    
    return Graph(id=graph_id, figure=go.Figure(
        data=[go.Bar(x=x, y=names, marker=dict(color=bar_colors), text=names, textposition='outside')],
        layout=go.Layout(
            xaxis_title="Status",
            yaxis_title="Test Case Count",
            xaxis_tickangle=-45,
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)  # noqa (l is an ambigous name)
        )
    ), config={"displayModeBar": False})


def verticlebar(df: pd.DataFrame, graph_id: str, x: List[str], names: List[str]) -> Graph:
    """Create and return a barplot"""
    return Graph(id=graph_id, figure=go.Figure(
        data=[go.Bar(x=names, y=x, marker_color="#035aa6",text=names, textposition='auto', orientation='h')],
        layout=go.Layout(
            xaxis_title="Transit Count",
            yaxis_title="Transit Country",
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)  # noqa (l is an ambigous name)
        )
    ), config={"displayModeBar": False})

from typing import List, Dict, Any
import pandas as pd


def get_align_map() -> Dict[str, List[str]]:
    """Mapping of columns to alignment, default is right"""
    return {
        "left": ["name", "date", "created_at", "status", "comment"],
        "center": [],
        "right": []
    }


def get_aligned() -> List[Dict]:
    """Return list of style objects for columns"""
    return [{"if": {"column_id": c}, "textAlign": a}
            for a, cols in get_align_map().items() for c in cols]


def get_even_odd_coloring() -> List[Dict]:
    """Return styling for even-odd coloring"""
    mapping = {"odd": "#dbdbdb", "even": "white"}
    return [{"if": {"row_index": k}, "backgroundColor": v} for k, v in mapping.items()]


def get_shared_styles(df: pd.DataFrame) -> Any:
    """Return styles for header and cells"""
    max_height = "{:d}rem".format(min(30, int(4 + 2 * len(df.index))))

    return {
        "sort_action": "native",
        "sort_mode": "multi",
        "page_action": "native",
        "filter_action": "native",
        "style_cell_conditional": get_aligned() + get_even_odd_coloring(),
        "style_table": {"overflowX": "auto", "maxWidth": "100%", "maxHeight": max_height},
        "style_cell": {"padding": "0.5rem 0.5rem", "line-height": "100%", "font-size": "11px",'textAlign': 'center'},
        "style_header": {"fontWeight": "bold", "text-align": "center", "backgroundColor": "#a4c5c6"},
    }


def create_table(df: pd.DataFrame, t_id: str, styling: None
                 ) -> DataTable:
    """Create and return data table"""
    complete_styling = get_shared_styles(df)
    if styling is not None:
        complete_styling.update(styling)

    df_new = df
    return DataTable(
        id=t_id, data=df_new.to_dict("records"),
        columns=[{"name": col, "id": col} for col in df_new.columns],
        fixed_rows={'headers': True, 'data': 0},
        **complete_styling
    )
