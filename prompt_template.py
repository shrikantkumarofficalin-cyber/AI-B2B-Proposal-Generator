def generate_prompt(company, industry, budget):

    prompt = f"""
You are a sustainability consultant.

Create a B2B sustainability proposal for:

Company: {company}
Industry: {industry}
Budget: {budget}

Generate:

1. Suggested sustainable product mix
2. Budget allocation
3. Estimated cost breakdown
4. Impact positioning summary

Return output in JSON format.

Example JSON structure:

{{
 "product_mix": [],
 "budget_allocation": {{}},
 "cost_breakdown": {{}},
 "impact_summary": ""
}}

"""

    return prompt