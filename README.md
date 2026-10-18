# AI Cloud Architecture Advisor

Describe your app idea in plain English.
AI recommends the right AWS services, architecture flow, cost estimate, and explains why.

Built with Amazon Bedrock + Python. Just 40 lines of code.

## How It Works

1. You describe what you want to build
2. AI analyzes your requirements
3. Returns recommended AWS services, architecture flow, and estimated cost

## Tech Stack

- Amazon Bedrock (AI brain)
- Amazon Nova Micro (AI model)
- Python 3 + Boto3
- IAM Role for permissions
- Converse API

## Setup

### Step 1 — Install
sudo yum install python3-pip -y
pip3 install boto3

### Step 2 — IAM Permission
Attach AmazonBedrockFullAccess to your EC2 role

### Step 3 — Create vi file and Run
vi advisor.py ( Paste the code and save the file )
python3 advisor.py

## Sample Prompts

- "E-commerce site with payments"
- "Real-time chat app for 1000 users"
- "ML model serving API"
- "Food delivery app with live tracking"
- "IoT dashboard for 10K devices"

## Sample Output

See [sample_output.md](sample_output.md) for full examples.

## Author

Gouri Andhare — AWS Cloud Engineer | 5x AWS Certified

## License

MIT
