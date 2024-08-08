import dash
import dash_alternative_viz as dav
import dash_html_components as html
from dash.dependencies import Input, Output
import random

app = dash.Dash(__name__)
app.layout = html.Div([
  html.Button(id="my_button", children="More data!"),
  dav.FusionChart(id="my_highchart", constructorType='column2d')
])

@app.callback(
  Output("my_highchart", "options"), [Input("my_button", "n_clicks")])
def random_chart(n_clicks):
  return {
  "chart": {
    "caption": "Countries With Most Oil Reserves [2022-23]",
    "subcaption": "In MMbbl = One Million barrels",
    "xaxisname": "Country",
    "yaxisname": "Reserves (MMbbl)",
    "numbersuffix": "K",
    "theme": "candy"
  },
  "data": [
    {
      "label": "Venezuela",
      "value": "303.8"
    },
    {
      "label": "Saudi",
      "value": "297.5"
    }
  ]
}


if __name__ == '__main__':
    app.run_server(debug=True)
