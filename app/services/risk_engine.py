def calculate_reliability_score(
    delivery_score,
    quality_score,
    payment_score,
    compliance_score
):

    score = (
        delivery_score +
        quality_score +
        payment_score +
        compliance_score
    ) / 4

    return round(score, 2)



def calculate_risk_level(score):

    if score >= 80:
        return "Low"

    elif score >= 50:
        return "Medium"

    else:
        return "High"