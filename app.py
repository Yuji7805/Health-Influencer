import data
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

claims_list = data.link_added_claims()
verified_claims = data.date_updated_claims()
influencers_list = data.influencer_list

categories = ['Sleep', 'Performance', 'Hormones', 'Nutrition', 'Exercise',
              'Stress', 'Cognition', 'Motivation', 'Recovery', 'Mental Health']
journals = [
    "PubMed Central", "Nature", "Science", "Ceil",
    "The Lancet", "New England Journal of Medicine", "JAMA Network"]


# Remove duplicated claims in dictionary array format
def remove_duplicate_claims(claims):
    unique_claims = []
    for claim in claims:
        if claim not in unique_claims:
            unique_claims.append(claim)
    return unique_claims


def score_claims(claims, influencer_id):
    for claim in claims:
        # Score the claims based on the trust score in influencer_list
        for influencer in influencers_list:            
            if influencer['key'] == influencer_id:
                trust_score = influencer['trust_score']                
                claim['score'] = trust_score
                break

        # Add article source link to the claim based on the research on verified claims
        for verified_claim in verified_claims:
            if claim["content"] == verified_claim["content"]:
                claim["link"] = verified_claim["link"]
                break
    return claims


app = Flask(__name__)


@app.route('/analyze', methods=['POST'])
def analyze_influencer():
    data = request.json
    influencer_name = data['influencerName']
    time_range = data['timeRange']
    notes = data['notes']
    journals = data['journals']
    claims_count = data['claimCount']

    # Find influencer id based on influencer name
    influencer_id = next((i for i, inf in enumerate(influencers_list) if
                          inf['influencer'] == influencer_name), None)
    if influencer_id is None:
        return jsonify({'error': 'Influencer not found'})

    # Filter claims_list based on the influencer_id
    influencer_claims = []
    for each in claims_list:
        if each['influencer_id'] == influencer_id:
            influencer_claims.append(each)

    # Filter influencer_claims based on the time range(time range is possible in following options: "last_week", "last_month", "last_year", "all_time")
    delta_days = 0
    if time_range == 'last_week':
        delta_days = 7
    elif time_range == 'last_month':
        delta_days = 30
    elif time_range == 'last_year':
        delta_days = 365
    elif time_range == 'all_time':
        delta_days = 100000
    else:
        raise ValueError("Invalid time range")

    # Calculate the time threshold only once
    time_threshold = datetime.now() - timedelta(days=delta_days)
    filtered_claims = [
        each for each in influencer_claims
        if datetime.strptime(each['timestamp'], '%Y-%m-%d %H:%M:%S') >= time_threshold
    ]

    # Remove duplicated claims
    influencers_claims = remove_duplicate_claims(filtered_claims)
    # Score claims
    claims = score_claims(influencers_claims, influencer_id=influencer_id)

    return jsonify(claims[:claims_count])


@app.route('/influencers', methods=['GET'])
def get_influencers():
    return jsonify(influencers_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
