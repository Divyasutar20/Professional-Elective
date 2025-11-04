# 🌿 Final Premium & Animated Diet & Nutrition Expert System (Light Theme)
# Author: ChatGPT

import ipywidgets as widgets
from IPython.display import display, HTML, clear_output

# --- Page background ---
display(HTML("<style>body{background-color:#f5fff5 !important;}</style>"))

# --- Animated Header ---
display(HTML("""
<div style='background:linear-gradient(90deg,#66BB6A,#43A047,#81C784);padding:20px;border-radius:15px;
            text-align:center;color:white;font-family:"Segoe UI",sans-serif;
            box-shadow:0 4px 12px rgba(0,0,0,0.25);max-width:900px;margin:auto;
            animation:shine 4s linear infinite;background-size:200% 200%;'>
  <style>@keyframes shine {
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
  }</style>
  <h1 style='margin:5px;'>🥗 <b>AI Diet & Nutrition Expert System</b></h1>
  <p style='font-size:17px;'>Your Personalized Health & Nutrition Advisor 💪</p>
</div>
"""))

# --- Inputs (consistent width + no truncation) ---
style = {'description_width': '130px'}
layout = widgets.Layout(width='230px')

name = widgets.Text(placeholder="Enter your name", description="👤 Name:", style=style, layout=layout)
age = widgets.BoundedIntText(value=25, min=1, max=120, description="🎂 Age:", style=style, layout=layout)
gender = widgets.Dropdown(options=['Male','Female'], description="⚧ Gender:", style=style, layout=layout)
weight = widgets.FloatText(value=60, description="⚖️ Weight (kg):", style=style, layout=layout)
height = widgets.FloatText(value=165, description="📏 Height (cm):", style=style, layout=layout)
goal = widgets.Dropdown(options=['Lose','Maintain','Gain'], description="🎯 Goal:", style=style, layout=layout)
condition = widgets.Dropdown(options=['None','Diabetes','Hypertension'], description="🩺 Condition:", style=style, layout=layout)
diet = widgets.Dropdown(options=['Veg','Non-Veg'], description="🥦 Diet Type:", style=style, layout=layout)

# --- Glowing Button ---
btn = widgets.Button(description="✨ Generate My Report ✨", button_style='success',
                     layout=widgets.Layout(width='260px', height='45px'))

# Add glowing animation on hover
display(HTML("""
<style>
button.widget-button {
  border:2px solid #43A047 !important;
  box-shadow:0 0 10px #A5D6A7;
  transition:all 0.3s ease;
}
button.widget-button:hover {
  background:#43A047 !important;
  box-shadow:0 0 20px #66BB6A;
  transform:scale(1.05);
}
</style>
"""))

out = widgets.Output()

# --- Helper function ---
def calc_bmi(w, h): return round(w / ((h / 100) ** 2), 2)

# --- Button click logic ---
def on_click(b):
    with out:
        clear_output()
        bmi = calc_bmi(weight.value, height.value)

        if bmi < 18.5:
            status, color, emoji, msg = ("Underweight","#FFF59D","🥛","Eat more calorie-rich foods like nuts, milk, and rice.")
        elif 18.5 <= bmi < 24.9:
            status, color, emoji, msg = ("Normal","#C8E6C9","✅","Maintain balanced meals with fruits, vegetables, and proteins.")
        elif 25 <= bmi < 29.9:
            status, color, emoji, msg = ("Overweight","#FFE082","⚠️","Reduce fried foods and sugars; add more salads.")
        else:
            status, color, emoji, msg = ("Obese","#FFCDD2","🚫","Follow low-calorie, high-fiber foods and exercise regularly.")

        bmi_bar = f"""
        <div style='background:linear-gradient(90deg,#FFD54F,#81C784,#4CAF50,#FFB300,#E57373);
                    height:18px;border-radius:10px;position:relative;margin:10px 0;'>
          <div style='position:absolute;left:{min(bmi/40*100,100)}%;top:0;bottom:0;width:6px;
                      background:black;border-radius:3px;'></div>
        </div>
        """

        # Health badge
        badge = f"""
        <div style='background:#2E7D32;color:white;display:inline-block;padding:5px 15px;
                    border-radius:20px;margin:10px auto;font-size:14px;'>
          🩺 Health Status: <b>{status}</b>
        </div>
        """

        html = f"""
        <div style='background-color:{color};padding:25px;border-radius:15px;
                    font-family:"Segoe UI",sans-serif;color:#1B5E20;
                    box-shadow:0 4px 12px rgba(0,0,0,0.15);
                    max-width:850px;margin:25px auto;
                    border:4px double #A5D6A7;'>
          <h2 style='color:#2E7D32;text-align:center;'>📋 Health Report for {name.value}</h2>
          <div style='text-align:center;font-size:15px;line-height:1.8;'>
            <b>Age:</b> {age.value} <b>Gender:</b> {gender.value}<br>
            <b>Height:</b> {height.value} cm <b>Weight:</b> {weight.value} kg<br>
            <b>BMI:</b> {bmi} ({emoji} <b>{status}</b>)
          </div>
          {bmi_bar}
          <center>{badge}</center>
          <div style='font-size:15px;text-align:center;'><b>Advice:</b> {msg}</div>
          <hr style='border:1px solid #A5D6A7;margin:12px 0'>
        """

        # Goal & condition advice
        if goal.value.lower()=="lose":
            html += "🎯 <b>Goal:</b> Weight Loss → Eat fewer calories than you burn.<br>"
        elif goal.value.lower()=="gain":
            html += "🎯 <b>Goal:</b> Weight Gain → Add more protein and calorie-dense foods.<br>"
        else:
            html += "🎯 <b>Goal:</b> Maintenance → Keep balanced intake of all nutrients.<br>"

        if condition.value.lower()=="diabetes":
            html += "💉 <b>Condition:</b> Diabetes → Avoid sugar, prefer whole grains & fiber-rich foods.<br>"
        elif condition.value.lower()=="hypertension":
            html += "🩺 <b>Condition:</b> Hypertension → Reduce salt, avoid processed foods.<br>"
        else:
            html += "💪 <b>Condition:</b> None → Stay hydrated and eat colorful veggies.<br>"

        # Diet plan
        html += "<hr style='border:1px solid #A5D6A7;margin:12px 0'><h4 style='color:#388E3C;text-align:center;'>🥗 Suggested Diet Plan</h4>"
        if diet.value.lower()=="veg":
            html += """<center>🌅 <b>Breakfast:</b> Oats + milk + fruits<br>
                       🌞 <b>Lunch:</b> Brown rice + dal + salad<br>
                       🌙 <b>Dinner:</b> Soup + chapati + paneer/tofu</center>"""
        else:
            html += """<center>🌅 <b>Breakfast:</b> Eggs + brown bread + fruit<br>
                       🌞 <b>Lunch:</b> Grilled chicken + rice + salad<br>
                       🌙 <b>Dinner:</b> Fish/egg curry + veggies</center>"""

        html += "<hr style='border:1px solid #A5D6A7;margin:12px 0;text-align:center;'>\
                 <center><b>💧 Tip:</b> Drink 2–3 L water daily & sleep 7–8 hours.</center></div>"
        display(HTML(html))

btn.on_click(on_click)

# --- Input Form (centered + glowing border) ---
form = widgets.VBox(
    [
        widgets.HTML("<h3 style='color:#388E3C;font-family:Segoe UI;text-align:center;'>🧍 Fill Your Details Below:</h3>"),
        widgets.HBox([name, age, gender], layout=widgets.Layout(justify_content='center')),
        widgets.HBox([weight, height, goal], layout=widgets.Layout(justify_content='center')),
        widgets.HBox([condition, diet], layout=widgets.Layout(justify_content='center')),
        widgets.HTML("<br>"),
        widgets.HBox([btn], layout=widgets.Layout(justify_content='center')),
        widgets.HTML("<br>"),
        out
    ],
    layout=widgets.Layout(
        padding="25px",
        border="3px solid #A5D6A7",
        border_radius="20px",
        margin="25px auto",
        width="70%",
        background_color="#FFFFFF",
        box_shadow="0 6px 15px rgba(0,0,0,0.15)"
    )
)

display(HTML("<div style='display:flex;justify-content:center;'>"))
display(form)
display(HTML("</div>"))

# --- Footer with Quote ---
display(HTML("""
<div style='text-align:center;font-family:"Segoe UI";margin-top:15px;
            color:#2E7D32;font-size:13px;'>
  🌸 Developed by <b>Divya Sutar</b> | 2025 Project<br>
  <i>"Your body deserves the best — feed it wisely, nourish it daily."</i>
</div>
"""))
