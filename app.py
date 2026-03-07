from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    text_result = None
    json_result = None

    if request.method == "POST":

        company = request.form["company"]
        industry = request.form["industry"]
        budget = int(request.form["budget"])

        solar = budget * 0.4
        lighting = budget * 0.3
        packaging = budget * 0.3

        data = {
            "product_mix":[
                "Solar panels",
                "Energy efficient lighting",
                "Recyclable packaging"
            ],

            "budget_allocation":{
                "solar_panels": solar,
                "lighting": lighting,
                "packaging": packaging
            },

            "cost_breakdown":{
                "materials": budget*0.5,
                "installation": budget*0.3,
                "maintenance": budget*0.2
            },

            "impact_summary":
            f"{company} can significantly reduce carbon emissions and improve sustainability in the {industry} sector."
        }

        text_result = f"""
Sustainable Product Mix:
- Solar panels
- Energy efficient lighting
- Recyclable packaging

Budget Allocation:
Solar Panels: {solar}
Lighting: {lighting}
Packaging: {packaging}

Estimated Cost Breakdown:
Materials: {budget*0.5}
Installation: {budget*0.3}
Maintenance: {budget*0.2}

Impact Summary:
{company} can significantly reduce carbon emissions and improve sustainability in the {industry} sector.
"""

        json_result = json.dumps(data, indent=4)

    return render_template("index.html", text_result=text_result, json_result=json_result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)