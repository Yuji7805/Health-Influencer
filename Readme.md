# RAG-Health-Influencer

## Overview
This is a Flask application that analyzes the claims made by health influencers and returns the top claims based on the trust score of the influencer.

## Installation
1. Clone the repository

2. Make venv with this command and activate it
`python -m venv venv`
`source venv/bin/activate`
3. Install the required packages using pip
`pip install -r requirements.txt`
4. Run the application using the command `python app.py`

## Usage
The application can be accessed using the following URL:

`http://localhost:5000/analyze`

### Parameters
- `influencerName`: The name of the influencer to analyze
- `timeRange`: The time range to analyze the claims. Possible values are "last_week", "last_month", "last_year", "all_time"
- `notes`: Additional notes about the claims to be analyzed
- `journals`: The journals where the claims were published. Possible values are "PubMed Central", "Nature", "Science", "Ceil", "The Lancet", "New England Journal of Medicine", "JAMA Network"
- `claimCount`: The number of claims to be analyzed

### Response
The response will be a JSON object containing the top claims based on the trust score of the influencer.

## Example
To analyze the claims made by the influencer "Dr. John Doe" in the last week, the following request can be sent:

`http://localhost:5000/analyze`

```json
{
  "influencerName": "Dr. John Doe",
  "timeRange": "last_week",
  "notes": "I am analyzing the claims made by Dr. John Doe in the last week",
  "journals": ["PubMed Central", "Nature", "Science", "Ceil", "The Lancet", "New England Journal of Medicine", "JAMA Network"],
  "claimCount": 5
}
```

The response will be a JSON object containing the top 5 claims based on the trust score of the influencer.

## Contributing
If you want to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Create a pull request to the main repository

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information. 
