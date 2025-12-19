import plotly.graph_objects as go

def resume_score_chart(score):
    """
    Gauge chart for resume score
    """
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Resume Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 40], 'color': "red"},
                {'range': [40, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "green"}
            ]
        }
    ))
    return fig


def skill_gap_chart(matched, missing):
    """
    Bar chart for skill match vs missing
    """
    fig = go.Figure(data=[
        go.Bar(name='Matched Skills', x=['Skills'], y=[len(matched)]),
        go.Bar(name='Missing Skills', x=['Skills'], y=[len(missing)])
    ])
    fig.update_layout(
        title="Skill Gap Overview",
        barmode='group',
        yaxis_title="Number of Skills"
    )
    return fig


def sentiment_confidence_chart(confidence):
    """
    Confidence score bar chart
    """
    fig = go.Figure(go.Bar(
        x=["Interview Answer Confidence"],
        y=[confidence * 100]
    ))
    fig.update_layout(
        yaxis_title="Confidence (%)",
        yaxis_range=[0, 100],
        title="Interview Confidence Level"
    )
    return fig
