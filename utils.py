import base64
from pathlib import Path

import altair as alt
import streamlit as st
import datetime as dt

# def streamlit_theme():
#     font = "IBM Plex Mono"
#     primary_color = "#F63366"
#     font_color = "#262730"
#     grey_color = "#f0f2f6"
#     base_size = 16
#     lg_font = base_size * 1.25
#     sm_font = base_size * 0.8  # st.table size
#     xl_font = base_size * 1.75  # noqa
#
#     config = {
#         "config": {
#             "arc": {"fill": primary_color},
#             "area": {"fill": primary_color},
#             "circle": {"fill": primary_color, "stroke": font_color, "strokeWidth": 0.5},
#             "line": {"stroke": primary_color},
#             "path": {"stroke": primary_color},
#             "point": {"stroke": primary_color},
#             "rect": {"fill": primary_color},
#             "shape": {"stroke": primary_color},
#             "symbol": {"fill": primary_color},
#             "title": {
#                 "font": font,
#                 "color": font_color,
#                 "fontSize": lg_font,
#                 "anchor": "start",
#             },
#             "axis": {
#                 "titleFont": font,
#                 "titleColor": font_color,
#                 "titleFontSize": sm_font,
#                 "labelFont": font,
#                 "labelColor": font_color,
#                 "labelFontSize": sm_font,
#                 "gridColor": grey_color,
#                 "domainColor": font_color,
#                 "tickColor": "#fff",
#             },
#             "header": {
#                 "labelFont": font,
#                 "titleFont": font,
#                 "labelFontSize": base_size,
#                 "titleFontSize": base_size,
#             },
#             "legend": {
#                 "titleFont": font,
#                 "titleColor": font_color,
#                 "titleFontSize": sm_font,
#                 "labelFont": font,
#                 "labelColor": font_color,
#                 "labelFontSize": sm_font,
#             },
#             "range": {
#                 "category": ["#f63366", "#fffd80", "#0068c9", "#ff2b2b", "#09ab3b"],
#                 "diverging": [
#                     "#850018",
#                     "#cd1549",
#                     "#f6618d",
#                     "#fbafc4",
#                     "#f5f5f5",
#                     "#93c5fe",
#                     "#5091e6",
#                     "#1d5ebd",
#                     "#002f84",
#                 ],
#                 "heatmap": [
#                     "#ffb5d4",
#                     "#ff97b8",
#                     "#ff7499",
#                     "#fc4c78",
#                     "#ec245f",
#                     "#d2004b",
#                     "#b10034",
#                     "#91001f",
#                     "#720008",
#                 ],
#                 "ramp": [
#                     "#ffb5d4",
#                     "#ff97b8",
#                     "#ff7499",
#                     "#fc4c78",
#                     "#ec245f",
#                     "#d2004b",
#                     "#b10034",
#                     "#91001f",
#                     "#720008",
#                 ],
#                 "ordinal": [
#                     "#ffb5d4",
#                     "#ff97b8",
#                     "#ff7499",
#                     "#fc4c78",
#                     "#ec245f",
#                     "#d2004b",
#                     "#b10034",
#                     "#91001f",
#                     "#720008",
#                 ],
#             },
#         }
#     }
#     return config

# def streamlit_theme_alt():
#     font = "IBM Plex Mono"
#     primary_color = "#F63366"
#     font_color = "#262730"
#     grey_color = "#f0f2f6"
#     base_size = 16
#     lg_font = base_size * 1.25
#     sm_font = base_size * 0.8  # st.table size
#     xl_font = base_size * 1.75  # noqa
#
#     config = {
#         "config": {
#             "view": {"fill": grey_color},
#             "arc": {"fill": primary_color},
#             "area": {"fill": primary_color},
#             "circle": {"fill": primary_color, "stroke": font_color, "strokeWidth": 0.5},
#             "line": {"stroke": primary_color},
#             "path": {"stroke": primary_color},
#             "point": {"stroke": primary_color},
#             "rect": {"fill": primary_color},
#             "shape": {"stroke": primary_color},
#             "symbol": {"fill": primary_color},
#             "title": {
#                 "font": font,
#                 "color": font_color,
#                 "fontSize": lg_font,
#                 "anchor": "start",
#             },
#             "axis": {
#                 "titleFont": font,
#                 "titleColor": font_color,
#                 "titleFontSize": sm_font,
#                 "labelFont": font,
#                 "labelColor": font_color,
#                 "labelFontSize": sm_font,
#                 "grid": True,
#                 "gridColor": "#fff",
#                 "gridOpacity": 1,
#                 "domain": False,
#                 # "domainColor": font_color,
#                 "tickColor": font_color,
#             },
#             "header": {
#                 "labelFont": font,
#                 "titleFont": font,
#                 "labelFontSize": base_size,
#                 "titleFontSize": base_size,
#             },
#             "legend": {
#                 "titleFont": font,
#                 "titleColor": font_color,
#                 "titleFontSize": sm_font,
#                 "labelFont": font,
#                 "labelColor": font_color,
#                 "labelFontSize": sm_font,
#             },
#             "range": {
#                 "category": ["#f63366", "#fffd80", "#0068c9", "#ff2b2b", "#09ab3b"],
#                 "diverging": [
#                     "#850018",
#                     "#cd1549",
#                     "#f6618d",
#                     "#fbafc4",
#                     "#f5f5f5",
#                     "#93c5fe",
#                     "#5091e6",
#                     "#1d5ebd",
#                     "#002f84",
#                 ],
#                 "heatmap": [
#                     "#ffb5d4",
#                     "#ff97b8",
#                     "#ff7499",
#                     "#fc4c78",
#                     "#ec245f",
#                     "#d2004b",
#                     "#b10034",
#                     "#91001f",
#                     "#720008",
#                 ],
#                 "ramp": [
#                     "#ffb5d4",
#                     "#ff97b8",
#                     "#ff7499",
#                     "#fc4c78",
#                     "#ec245f",
#                     "#d2004b",
#                     "#b10034",
#                     "#91001f",
#                     "#720008",
#                 ],
#                 "ordinal": [
#                     "#ffb5d4",
#                     "#ff97b8",
#                     "#ff7499",
#                     "#fc4c78",
#                     "#ec245f",
#                     "#d2004b",
#                     "#b10034",
#                     "#91001f",
#                     "#720008",
#                 ],
#             },
#         }
#     }
#     return config
#
# category_large = [
#     "#f63366",
#     "#0068c9",
#     "#fffd80",
#     "#7c61b0",
#     "#ffd37b",
#     "#ae5897",
#     "#ffa774",
#     "#d44a7e",
#     "#fd756d",
# ]
#
# alt.themes.register("streamlit", streamlit_theme)
# alt.themes.enable("streamlit")

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_html(path, style, styling_class):
    return f"<img src='data:image/png;base64,{img_to_bytes(path)}' style={style} class={styling_class}>"

@st.cache
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def gantt_chart(data):
    today = dt.datetime.now()
    clamp_max = (today + dt.timedelta(days=30*4)).strftime('%Y-%m-%d')
    clamp_min = (today - dt.timedelta(days=30*12)).strftime('%Y-%m-%d')
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('start:T', axis=alt.Axis(title='', orient='top', format='%b %y'),
                scale=alt.Scale(domain=(clamp_min, clamp_max), clamp=True)),
        x2='end:T',
        y=alt.Y('org:N', sort=None, axis=alt.Axis(title='')),
        color=alt.Color('color', scale=None),
        tooltip=['role', 'start', 'end', 'location', 'description'],
    ).properties(height=300).interactive()

    line = alt.Chart(data).mark_rule().encode(
        x='now:T'
    ).interactive()

    return chart+line

def language_chart(data):
    chart = alt.Chart(data).mark_bar(opacity=0.5).encode(
        x=alt.X('level:Q', axis=alt.Axis(title='')),
        y=alt.Y('language:N', sort='-x', axis=alt.Axis(title='')),
        tooltip=['proficiency (LinkedIn)', 'speaking proficiency', 'comments'],
    )

    text = chart.mark_text(
        align='right',
        baseline='middle',
        font="IBM Plex Mono",
        dx=-3
    ).encode(text='speaking proficiency')

    return alt.layer(chart, text).configure_view(strokeWidth=0).properties(width=660)

def coding_language_chart(data):
    chart = alt.Chart(data).mark_bar(opacity=0.5).encode(
        x=alt.X('level:Q', axis=alt.Axis(title=''), scale=alt.Scale(domain=(0,100))),
        y=alt.Y('programming language:N', sort='-x', axis=alt.Axis(title='')),
        tooltip=['comments']
    )

    text = chart.mark_text(
        align='center',
        baseline='middle',
        font='IBM Plex Mono',
        dx=0
    ).encode(text='definition')

    return alt.layer(chart, text).configure_view(strokeWidth=0).properties(width=660)


def date_axis(year, month, day):
    return dt.datetime(year, month, day)