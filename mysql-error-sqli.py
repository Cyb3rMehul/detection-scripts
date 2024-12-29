import requests

# This script is generated using getAI
# Define the target URL
url = "http://example.com/login"  # Replace with the actual target URL

# Load the payloads from the wordlist file
with open("sql_injection_wordlist.txt", "r") as file:
    payloads = [line.strip() for line in file]

# Specify other POST data parameters if required
post_data_template = {
    "password": "test_password"  # Adjust or add other parameters as needed
}

# Function to detect a potential SQL injection exploit
def is_sql_injection_successful(response):
    # Define indicators of successful injection
    success_indicators = [
        "syntax error", "mysql", "sql", "unclosed quotation mark",
        "unknown column", "ODBC", "error in your SQL syntax",
        "warning: mysql"  # Add more error messages based on observations
    ]
    
    # Check the response content for any indicator
    for indicator in success_indicators:
        if indicator.lower() in response.text.lower():
            return True
    return False

# Iterate over the payloads and send POST requests
for payload in payloads:
    print(f"Testing payload: {payload}")
    
    # Prepare the POST data with the payload injected into the username
    post_data = post_data_template.copy()
    post_data["username"] = payload

    try:
        # Send the POST request
        response = requests.post(url, data=post_data)

        # Check if the injection was successful
        if is_sql_injection_successful(response):
            print(f"Potential SQL Injection found with payload: {payload}")
        else:
            print("No success with this payload.")
    except Exception as e:
        print(f"Error occurred with payload {payload}: {e}")
