import numpy as np
import plotly.graph_objects as go
from scipy.stats import binom


def make_power_figure(n_grid, power, target_power=None):
    # минимальный размер выборки, при котором мощность >= целевой
    min_n = None
    if target_power is not None:
        mask = power >= target_power
        if mask.any():
            min_n = int(n_grid[mask].min())

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=n_grid,
            y=power,
            name="Мощность",
            line=dict(color="orange", width=2, dash="solid"),
            marker=dict(size=6),
            hovertemplate="N = %{x}<br>Power = %{y:.3f}<extra></extra>",
        )
    )

    # заданная мощность
    if target_power is not None:
        fig.add_hline(
            y=target_power,
            line_dash="dash",
            line_color="red",
            annotation_text=f"power = {target_power:.2f}",
            annotation_position="bottom right",
            annotation_font=dict(color="white"),
        )

    # рассчитанный размер выборки, при котором достигается заданная юзером мощность
    if min_n is not None:
        fig.add_vline(
            x=min_n,
            line_dash="dash",
            line_color="white",
            annotation_text=f"N = {min_n}",
            annotation_position="top",
            annotation_font=dict(color="white"),
        )

    fig.update_layout(
        xaxis=dict(
            title="Размер выборки N"
        ),
        yaxis=dict(
            title="Мощность",
            range=[0, 1.05],
            showgrid=True,
            gridcolor="#333333",
            zeroline=False,
        ),
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white"),
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        margin=dict(l=60, r=30, t=50, b=60),
    )

    return fig, min_n
