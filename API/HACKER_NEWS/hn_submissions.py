from operator import itemgetter
import requests
import time

# Make an API call to retrieve the top stories IDs and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# Process the JSON response to get a list of submission IDs
submission_ids = r.json()
submission_dicts = []

# Loop through the first 30 submission IDs
for submission_id in submission_ids[:30]:
    # Make a separate API call to retrieve details for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id} status: {r.status_code}")
    
    # Convert the response to JSON format
    response_dict = r.json()
    
    # Build a dictionary for each article with title, link, and number of comments
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),  # Use 0 if 'descendants' is missing
    }
    submission_dicts.append(submission_dict)

    # Optional: Add a delay to avoid hitting the rate limit
    time.sleep(0.5)

# Sort the list of dictionaries by number of comments in descending order
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Print the title, discussion link, and number of comments for each submission
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
