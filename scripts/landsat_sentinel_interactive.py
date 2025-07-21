import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# 更详细的大气透过率数据（基于真实大气窗口）
wavelength = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 
              1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5,
              10.0, 10.5, 11.0, 11.5, 12.0, 12.5]

transmission = [75, 80, 85, 88, 90, 88, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 15, 20, 25, 30, 35, 40,
                50, 55, 60, 65, 70, 75]

# 详细的卫星波段数据
satellite_bands = {
    "Landsat 9": [
        {"Band": "B1", "Range": (0.43, 0.45), "Resolution": "30 m", "Color": "lightblue", "Description": "Coastal aerosol"},
        {"Band": "B2", "Range": (0.45, 0.51), "Resolution": "30 m", "Color": "blue", "Description": "Blue"},
        {"Band": "B3", "Range": (0.53, 0.59), "Resolution": "30 m", "Color": "green", "Description": "Green"},
        {"Band": "B4", "Range": (0.64, 0.67), "Resolution": "30 m", "Color": "red", "Description": "Red"},
        {"Band": "B5", "Range": (0.85, 0.88), "Resolution": "30 m", "Color": "lightgreen", "Description": "NIR"},
        {"Band": "B6", "Range": (1.57, 1.65), "Resolution": "30 m", "Color": "orange", "Description": "SWIR 1"},
        {"Band": "B7", "Range": (2.11, 2.29), "Resolution": "30 m", "Color": "brown", "Description": "SWIR 2"},
        {"Band": "B8", "Range": (0.50, 0.68), "Resolution": "15 m", "Color": "purple", "Description": "Panchromatic"},
        {"Band": "B9", "Range": (1.36, 1.38), "Resolution": "30 m", "Color": "navy", "Description": "Cirrus"},
        {"Band": "B10", "Range": (10.6, 11.2), "Resolution": "100 m", "Color": "crimson", "Description": "TIRS 1"},
        {"Band": "B11", "Range": (11.5, 12.5), "Resolution": "100 m", "Color": "crimson", "Description": "TIRS 2"}
    ],
    "Sentinel-2": [
        {"Band": "B1", "Range": (0.433, 0.453), "Resolution": "60 m", "Color": "lightblue", "Description": "Coastal aerosol"},
        {"Band": "B2", "Range": (0.458, 0.523), "Resolution": "10 m", "Color": "blue", "Description": "Blue"},
        {"Band": "B3", "Range": (0.543, 0.578), "Resolution": "10 m", "Color": "green", "Description": "Green"},
        {"Band": "B4", "Range": (0.650, 0.680), "Resolution": "10 m", "Color": "red", "Description": "Red"},
        {"Band": "B5", "Range": (0.698, 0.713), "Resolution": "20 m", "Color": "lightgreen", "Description": "Red edge 1"},
        {"Band": "B6", "Range": (0.733, 0.748), "Resolution": "20 m", "Color": "yellow", "Description": "Red edge 2"},
        {"Band": "B7", "Range": (0.773, 0.793), "Resolution": "20 m", "Color": "orange", "Description": "Red edge 3"},
        {"Band": "B8", "Range": (0.785, 0.900), "Resolution": "10 m", "Color": "purple", "Description": "NIR"},
        {"Band": "B8A", "Range": (0.855, 0.875), "Resolution": "20 m", "Color": "forestgreen", "Description": "NIR narrow"},
        {"Band": "B9", "Range": (0.935, 0.955), "Resolution": "60 m", "Color": "navy", "Description": "Water vapour"},
        {"Band": "B10", "Range": (1.365, 1.385), "Resolution": "60 m", "Color": "navy", "Description": "Cirrus"},
        {"Band": "B11", "Range": (1.565, 1.655), "Resolution": "20 m", "Color": "brown", "Description": "SWIR 1"},
        {"Band": "B12", "Range": (2.100, 2.280), "Resolution": "20 m", "Color": "saddlebrown", "Description": "SWIR 2"}
    ]
}

def create_satellite_comparison_chart():
    """创建卫星波段比较图表"""
    
    # 创建子图，左侧显示可见光到近红外，右侧显示热红外
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Visible to SWIR (0.4-2.5 μm)', 'Thermal Infrared (10-12.5 μm)'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}]],
        horizontal_spacing=0.02
    )
    
    # 添加大气透过率曲线
    # 左侧子图：可见光到近红外
    vis_swir_wavelength = [w for w in wavelength if w <= 2.5]
    vis_swir_transmission = [transmission[i] for i, w in enumerate(wavelength) if w <= 2.5]
    
    fig.add_trace(
        go.Scatter(
            x=vis_swir_wavelength, 
            y=vis_swir_transmission,
            mode='lines', 
            name='Atmospheric Transmission',
            line=dict(color='lightgray', width=2),
            fill='tonexty',
            fillcolor='rgba(200,200,200,0.3)'
        ),
        row=1, col=1
    )
    
    # 右侧子图：热红外
    tir_wavelength = [w for w in wavelength if w >= 10]
    tir_transmission = [transmission[i] for i, w in enumerate(wavelength) if w >= 10]
    
    fig.add_trace(
        go.Scatter(
            x=tir_wavelength, 
            y=tir_transmission,
            mode='lines', 
            name='Atmospheric Transmission',
            line=dict(color='lightgray', width=2),
            fill='tonexty',
            fillcolor='rgba(200,200,200,0.3)',
            showlegend=False
        ),
        row=1, col=2
    )
    
    # 添加卫星波段矩形
    for satellite_name, bands in satellite_bands.items():
        for band in bands:
            # 确定波段属于哪个子图
            if band["Range"][1] <= 2.5:
                # 可见光到近红外波段
                fig.add_trace(
                    go.Scatter(
                        x=[band["Range"][0], band["Range"][1], band["Range"][1], band["Range"][0], band["Range"][0]],
                        y=[0, 0, 100, 100, 0],
                        fill="toself",
                        name=f"{satellite_name} {band['Band']} ({band['Resolution']})",
                        fillcolor=band["Color"],
                        line=dict(color=band["Color"], width=1),
                        opacity=0.7,
                        hovertemplate=f"<b>{satellite_name} {band['Band']}</b><br>" +
                                    f"Wavelength: {band['Range'][0]}-{band['Range'][1]} μm<br>" +
                                    f"Resolution: {band['Resolution']}<br>" +
                                    f"Description: {band['Description']}<extra></extra>"
                    ),
                    row=1, col=1
                )
            elif band["Range"][0] >= 10:
                # 热红外波段
                fig.add_trace(
                    go.Scatter(
                        x=[band["Range"][0], band["Range"][1], band["Range"][1], band["Range"][0], band["Range"][0]],
                        y=[0, 0, 100, 100, 0],
                        fill="toself",
                        name=f"{satellite_name} {band['Band']} ({band['Resolution']})",
                        fillcolor=band["Color"],
                        line=dict(color=band["Color"], width=1),
                        opacity=0.7,
                        hovertemplate=f"<b>{satellite_name} {band['Band']}</b><br>" +
                                    f"Wavelength: {band['Range'][0]}-{band['Range'][1]} μm<br>" +
                                    f"Resolution: {band['Resolution']}<br>" +
                                    f"Description: {band['Description']}<extra></extra>",
                        showlegend=False
                    ),
                    row=1, col=2
                )
    
    # 更新布局
    fig.update_layout(
        title={
            'text': 'Satellite Band Comparison with Atmospheric Transmission',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20}
        },
        xaxis_title="Wavelength (μm)",
        yaxis_title="Atmospheric Transmission (%)",
        template="plotly_white",
        height=600,
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.02
        )
    )
    
    # 更新x轴范围
    fig.update_xaxes(range=[0.4, 2.5], row=1, col=1)
    fig.update_xaxes(range=[10, 12.5], row=1, col=2)
    
    # 设置共享y轴
    fig.update_yaxes(range=[0, 100], row=1, col=1)
    fig.update_yaxes(range=[0, 100], row=1, col=2)
    
    # 添加连接线表示波长连续性（在两个子图之间）
    # 在左侧子图添加连接线
    fig.add_shape(
        type="line",
        x0=2.5, y0=0,
        x1=2.5, y1=100,
        line=dict(color="black", width=2),
        xref="x", yref="y",
        row=1, col=1
    )
    
    # 在右侧子图添加连接线
    fig.add_shape(
        type="line",
        x0=10, y0=0,
        x1=10, y1=100,
        line=dict(color="black", width=2),
        xref="x", yref="y",
        row=1, col=2
    )
    
    # 添加连接线标签
    fig.add_annotation(
        x=2.5, y=50,
        text="↔",
        showarrow=False,
        font=dict(size=20, color="black"),
        xref="x", yref="y",
        row=1, col=1
    )
    
    fig.add_annotation(
        x=10, y=50,
        text="↔",
        showarrow=False,
        font=dict(size=20, color="black"),
        xref="x", yref="y",
        row=1, col=2
    )
    
    # 添加波长连续性说明
    fig.add_annotation(
        x=0.5, y=-0.15,
        text="Wavelength Continuity (2.5-10 μm not shown)",
        showarrow=False,
        font=dict(size=14, color="#2c3e50", family="Arial, sans-serif"),
        xref="paper", yref="paper"
    )
    
    return fig

def create_interactive_dashboard():
    """创建交互式仪表板"""
    import dash
    from dash import dcc, html
    from dash.dependencies import Input, Output
    
    app = dash.Dash(__name__)
    
    app.layout = html.Div([
        html.H1("Satellite Spectral Bands and Atmospheric Transmission Comparison", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}),
        
        html.Div([
            html.Div([
                html.Label("Select Satellite:", style={'fontSize': 16, 'fontWeight': 'bold', 'display': 'block', 'marginBottom': '10px'}),
                dcc.Dropdown(
                    id='satellite-dropdown',
                    options=[
                        {'label': 'Landsat 9', 'value': 'Landsat 9'},
                        {'label': 'Sentinel-2', 'value': 'Sentinel-2'},
                        {'label': 'Both Satellites', 'value': 'Both'}
                    ],
                    value='Both',
                    style={'width': '300px', 'margin': '0 auto'}
                )
            ], style={'textAlign': 'center', 'marginBottom': 30})
        ]),
        
        dcc.Graph(id='satellite-comparison-chart'),
        
        html.Div([
            html.H3("Chart Description", style={'color': '#2c3e50'}),
            html.Ul([
                html.Li("Light gray area represents atmospheric transmission, peaks indicate atmospheric windows"),
                html.Li("Colored rectangles represent spectral bands of each satellite"),
                html.Li("Hover over elements to view detailed band information"),
                html.Li("Left panel shows visible to near-infrared bands, right panel shows thermal infrared bands")
            ])
        ], style={'marginTop': 30, 'padding': 20, 'backgroundColor': '#f8f9fa', 'borderRadius': 10})
    ])
    
    @app.callback(
        Output('satellite-comparison-chart', 'figure'),
        Input('satellite-dropdown', 'value')
    )
    def update_chart(selected_satellite):
        if selected_satellite == 'Both':
            return create_satellite_comparison_chart()
        else:
            # 创建只显示选定卫星的图表
            fig = make_subplots(
                rows=1, cols=2,
                subplot_titles=('Visible to SWIR (0.4-2.5 μm)', 'Thermal Infrared (10-12.5 μm)'),
                specs=[[{"secondary_y": False}, {"secondary_y": False}]],
                horizontal_spacing=0.1
            )
            
            # 添加大气透过率曲线
            vis_swir_wavelength = [w for w in wavelength if w <= 2.5]
            vis_swir_transmission = [transmission[i] for i, w in enumerate(wavelength) if w <= 2.5]
            
            fig.add_trace(
                go.Scatter(
                    x=vis_swir_wavelength, 
                    y=vis_swir_transmission,
                    mode='lines', 
                    name='Atmospheric Transmission',
                    line=dict(color='lightgray', width=2),
                    fill='tonexty',
                    fillcolor='rgba(200,200,200,0.3)'
                ),
                row=1, col=1
            )
            
            tir_wavelength = [w for w in wavelength if w >= 10]
            tir_transmission = [transmission[i] for i, w in enumerate(wavelength) if w >= 10]
            
            fig.add_trace(
                go.Scatter(
                    x=tir_wavelength, 
                    y=tir_transmission,
                    mode='lines', 
                    name='Atmospheric Transmission',
                    line=dict(color='lightgray', width=2),
                    fill='tonexty',
                    fillcolor='rgba(200,200,200,0.3)',
                    showlegend=False
                ),
                row=1, col=2
            )
            
            # 只添加选定卫星的波段
            bands = satellite_bands[selected_satellite]
            for band in bands:
                if band["Range"][1] <= 2.5:
                    fig.add_trace(
                        go.Scatter(
                            x=[band["Range"][0], band["Range"][1], band["Range"][1], band["Range"][0], band["Range"][0]],
                            y=[0, 0, 100, 100, 0],
                            fill="toself",
                            name=f"{band['Band']} ({band['Resolution']})",
                            fillcolor=band["Color"],
                            line=dict(color=band["Color"], width=1),
                            opacity=0.7,
                            hovertemplate=f"<b>{band['Band']}</b><br>" +
                                        f"Wavelength: {band['Range'][0]}-{band['Range'][1]} μm<br>" +
                                        f"Resolution: {band['Resolution']}<br>" +
                                        f"Description: {band['Description']}<extra></extra>"
                        ),
                        row=1, col=1
                    )
                elif band["Range"][0] >= 10:
                    fig.add_trace(
                        go.Scatter(
                            x=[band["Range"][0], band["Range"][1], band["Range"][1], band["Range"][0], band["Range"][0]],
                            y=[0, 0, 100, 100, 0],
                            fill="toself",
                            name=f"{band['Band']} ({band['Resolution']})",
                            fillcolor=band["Color"],
                            line=dict(color=band["Color"], width=1),
                            opacity=0.7,
                            hovertemplate=f"<b>{band['Band']}</b><br>" +
                                        f"Wavelength: {band['Range'][0]}-{band['Range'][1]} μm<br>" +
                                        f"Resolution: {band['Resolution']}<br>" +
                                        f"Description: {band['Description']}<extra></extra>",
                            showlegend=False
                        ),
                        row=1, col=2
                    )
            
            fig.update_layout(
                title=f'{selected_satellite} Bands vs Atmospheric Transmission',
                xaxis_title="Wavelength (μm)",
                yaxis_title="Atmospheric Transmission (%)",
                template="plotly_white",
                height=600,
                showlegend=True,
                legend=dict(
                    orientation="v",
                    yanchor="top",
                    y=1,
                    xanchor="left",
                    x=1.02
                )
            )
            
            fig.update_xaxes(range=[0.4, 2.5], row=1, col=1)
            fig.update_xaxes(range=[10, 12.5], row=1, col=2)
            fig.update_yaxes(range=[0, 100], row=1, col=1)
            fig.update_yaxes(range=[0, 100], row=1, col=2)
            
            return fig
    
    return app

if __name__ == "__main__":
    # 创建交互式仪表板
    app = create_interactive_dashboard()
    
    # 运行应用
    print("Starting interactive dashboard...")
    print("Please open http://127.0.0.1:8050 in your browser")
    app.run_server(debug=True, port=8050)
