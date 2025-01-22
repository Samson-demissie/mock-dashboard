from jupyter_dash import JupyterDash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Extended mock humanitarian data for Ethiopia with LONG numbers
data_humanitarian = {
    "Region": ["Addis Ababa", "Oromia", "Amhara", "Tigray", "SNNPR", "Afar"],
    "Population": [12345678, 35067890, 20012345, 6000987, 20012389, 1500123],
    "Literacy Rate": [92, 50, 55, 60, 45, 35],
    "Food Insecurity Rate": [10, 45, 30, 40, 50, 60],
    "IDPs": [56789, 876543, 345678, 2345678, 545678, 98765],
    "Refugees": [10000, 20000, 15000, 50000, 25000, 8000],
    "Malnutrition Rate": [5, 15, 20, 18, 25, 30],
    "Water Access Rate": [90, 60, 65, 70, 50, 40],
}

# Convert data to a DataFrame
mock_data = pd.DataFrame(data_humanitarian)

# Create various visualizations
fig_population_bar = px.bar(
    mock_data,
    x="Region",
    y="Population",
    title="Population by Region"
)
# Force axis to display full integers (no rounding/scientific)
fig_population_bar.update_layout(
    yaxis=dict(tickformat='d'),  # display integers fully
    plot_bgcolor="#FFFFAA",      # mismatch color
    paper_bgcolor="#00FF00",     # bright green paper
    font=dict(color="#FF00FF")   # bright magenta font
)

fig_population_hist = px.histogram(
    mock_data,
    x="Population",
    nbins=5,
    title="Population Distribution (Histogram) - "
)
fig_population_hist.update_layout(
    xaxis=dict(tickformat='d'),
    plot_bgcolor="#FFCCCC", 
    paper_bgcolor="#0000FF",  # bright blue
    font=dict(color="#FFFF00") # bright yellow
)

fig_literacy_line = px.line(
    mock_data,
    x="Region",
    y="Literacy Rate",
    title="Literacy Rate by Region"
)
fig_literacy_line.update_layout(
    yaxis=dict(tickformat='d'),
    plot_bgcolor="#CCCCCC",
    paper_bgcolor="#FFA500",   # orange background
    font=dict(color="#800000") # maroon text
)

fig_food_insecurity = px.line(
    mock_data,
    x="Region",
    y="Food Insecurity Rate",
    markers=True,
    title="Food Insecurity Rate by Region"
)
fig_food_insecurity.update_layout(
    yaxis=dict(tickformat='d'),
    plot_bgcolor="#EEFFEE",
    paper_bgcolor="#FF69B4",  # hot pink
    font=dict(color="#2F4F4F") # dark slate gray
)

fig_idps_bar = px.bar(
    mock_data,
    x="Region",
    y="IDPs",
    title="Internally Displaced Persons (IDPs) by Region"
)
fig_idps_bar.update_layout(
    yaxis=dict(tickformat='d'),
    plot_bgcolor="#C0C0C0",  # silver
    paper_bgcolor="#FFFF00", # yellow
    font=dict(color="#0000FF") # bright blue
)

fig_malnutrition_scatter = px.scatter(
    mock_data,
    x="Malnutrition Rate",
    y="Water Access Rate",
    color="Region",
    title="Malnutrition vs Water Access"
)
fig_malnutrition_scatter.update_layout(
    xaxis=dict(tickformat='d'),
    yaxis=dict(tickformat='d'),
    plot_bgcolor="#FFFFFF",  # plain white
    paper_bgcolor="#7FFFD4", # aquamarine
    font=dict(color="#8B0000") # dark red
)

# Initialize the Dash app
app = JupyterDash(__name__)


app.layout = html.Div([
   
    html.H1(
        "Ethiopia Humanitarian Dashboard",
        style={
            "textAlign": "center",
            "color": "#00FFFF",       # bright cyan
            "fontSize": "60px",
            "backgroundColor": "#FF00FF"  # magenta
        }
    ),

    # Short intro with tiny font that's hard to read
    html.Div("visual overview of various indicators.",
             style={
                 "textAlign": "left",
                 "fontSize": "9px",
                 "color": "#F5F5DC",  # beige text on weird backgrounds
                 "backgroundColor": "#800080"  # purple background
             }
    ),

    # First row of charts in a 2-column grid but containing 3 charts
    html.Div([
        dcc.Graph(figure=fig_population_bar),
        dcc.Graph(figure=fig_literacy_line),
        dcc.Graph(figure=fig_food_insecurity)
    ], style={
        "display": "grid",
        "gridTemplateColumns": "1fr 1fr",  # only 2 columns for 3 charts
        "gap": "10px",
        "marginLeft": "200px",  # excessive left margin
        "backgroundColor": "#FFD700"  # gold-ish
    }),

    # Second row: two charts with uneven widths and more clashing colors
    html.Div([
        html.Div(
            dcc.Graph(figure=fig_idps_bar),
            style={
                "width": "25%", 
                "display": "inline-block",
                "verticalAlign": "top",
                "backgroundColor": "#8A2BE2", # blueviolet
                "border": "4px solid #7FFF00" # chartreuse border
            }
        ),
        html.Div(
            dcc.Graph(figure=fig_malnutrition_scatter),
            style={
                "width": "45%",
                "display": "inline-block",
                "marginLeft": "5px",
                "border": "2px dashed #FF0000", # bright red
                "backgroundColor": "#ADFF2F"    # green-yellow
            }
        ),
    ], style={"marginTop": "20px"}),

    # Third row: single chart with a bizarre color scheme
    html.Div([
        dcc.Graph(figure=fig_population_hist)
    ], style={
        "textAlign": "right",
        "backgroundColor": "#00FA9A",  # medium spring green
        "border": "3px dotted #FF8C00", # dark orange
        "padding": "30px"
    }),

    # Disclaimers with random font sizes/colors
    html.Div([
        html.P(
            "Disclaimer: Data may be inaccurate or outdated.",
            style={
                "fontSize": "27px",
                "color": "#FF0000", 
                "marginLeft": "30px"
            }
        ),
        html.P(
            "Source: Mocked data for demonstration only.",
            style={
                "fontSize": "14px",
                "color": "#8B008B", # dark magenta
                "marginLeft": "100px"
            }
        ),
        html.P(
            "Note: Regions not exhaustive.",
            style={
                "fontSize": "16px",
                "color": "#000080",  # navy
                "marginTop": "50px"
            }
        ),
    ], style={"backgroundColor": "#D3D3D3"}), # lightgray background for disclaimers

    # Final alignment inconsistency
    html.Div(
        "End of Dashboard",
        style={
            "textAlign": "center",
            "color": "#006400",   # dark green
            "fontSize": "16px",
            "backgroundColor": "#B0E0E6" # powder blue
        }
    )
],
style={
    "backgroundColor": "#F0F0F0",  # bland background
    "margin": "0px auto",
    "width": "95%",  
    "border": "5px solid #FA8072"  # salmon colored thick border
})

# Run the app
app.run_server(host='0.0.0.0', port=8000)

