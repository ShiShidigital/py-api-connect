import requests
import argparse
import urllib.parse


def create_employer_jobsnyc(employer_name):
    # endpoint URL
    url = "https://api.inklu-connect.app/jobsync/create-employer"
    # URL encoding
    encode_employer = urllib.parse.quote(employer_name)
    # Append to query
    url += f"?organisation={encode_employer}"

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Making POST request
    response = requests.post(url, headers=headers, data=None)

    # Check response
    if response.status_code == 201: # Success
        print(f"Employer {employer_name} created sucessfully")
        print(response.json())
    else:
        print(f"Failed to create employer: {response.status_code}")
        print(response.json())


def main():
    parser = argparse.ArgumentParser(description="Create Employer Jobsync entry on Inklu API.")
    parser.add_argument('employer_name', type=str, help="Employer Name")
    args = parser.parse_args()
    create_employer_jobsnyc(args.employer_name)


if __name__ == "__main__":
    main()