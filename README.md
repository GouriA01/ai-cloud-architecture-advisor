
# AI Cloud Architecture Advisor

A beginner-friendly AI-powered tool that recommends AWS architectures for your app ideas in seconds, using Amazon Bedrock and Amazon Nova Micro.

Built for **students and freshers** learning AWS.

## What It Does

Describe your app idea in plain English. The AI recommends:
- The right AWS services and **why** each one fits
- Architecture flow (how services connect)
- Estimated monthly cost (rough ballpark, not Pricing Calculator figures)
- A text-based architecture diagram

## Environment

This project is built and tested on the following setup:
- **OS:** Amazon Linux (EC2 instance)
- **Region:** us-east-1 (N. Virginia)
- **Runtime:** Python 3 with Boto3
- **AI Model:** Amazon Nova Micro via Bedrock (`us.amazon.nova-micro-v1:0`)

> **Note:** This guide focuses on Amazon Linux EC2 in us-east-1. If you are using a different OS or region, the commands and model ID may differ.

## Prerequisites

- An AWS account with an Amazon Linux EC2 instance running in **us-east-1**
- An IAM role attached to your EC2 instance
- **Amazon Nova Micro enabled** in us-east-1 under **Bedrock → Model access**

> **Important:** Model access is not always auto-enabled. Go to the Amazon Bedrock console → Model access → ensure Amazon Nova Micro is enabled in us-east-1 before running the script.

## Setup (5 Steps)

### Step 1 — Install Python packages on your Amazon Linux EC2

SSH into your EC2 instance and run these two commands separately:

```bash
sudo yum install python3-pip -y
```
```bash
pip3 install boto3
```

> **Note:** These are two separate commands. Run them one at a time. Running them on a single line will cause errors.

### Step 2 — Add IAM permissions

Go to IAM Console → Roles → Select your EC2 instance role → Attach the `AmazonBedrockFullAccess` policy.

### Step 3 — Enable model access if not already enabled (Usually Access Model is already enabled)

Go to the **Amazon Bedrock console** in **us-east-1** → **Model access** → Enable **Amazon Nova Micro**.

This is required before the script can call the model.

### Step 4 — Create the Python script

```bash
vi advisor.py
```

Paste the contents of `advisor.py` from this repo and save the file.

### Step 5 — Run it

```bash
python3 advisor.py
```

Try prompts like:
- "E-commerce site with payments"
- "ML model serving API"
- "Video streaming platform"
- "IoT dashboard for 10K devices"

## Tech Stack

| Component | Purpose |
|-----------|---------|
| **Amazon Bedrock** | AI inference engine |
| **Amazon Nova Micro** | Language model (fast, lightweight) |
| **Python 3 + Boto3** | Script and AWS SDK |
| **IAM Role** | Permissions for Bedrock access |
| **Converse API** | Sends prompts to Bedrock |
| **Amazon Linux EC2** | Runtime environment (us-east-1) |

## Model ID Note

The script uses `us.amazon.nova-micro-v1:0`, which is a **US cross-region inference profile**. This means Bedrock can route your request across US regions (us-east-1, us-east-2, us-west-2) for better availability.

This is different from `amazon.nova-micro-v1:0` (single-region, stays in the exact region you call from).

Since this project runs on EC2 in **us-east-1**, the `us.` prefix works perfectly. If you are retyping the model ID, use the exact form shown in the code to avoid validation errors.

## Important Caveats

- **Cost estimates are illustrative.** The AI returns rough ballpark numbers (e.g., "~$200/month for 10K users"). These are not based on the AWS Pricing Calculator. Always verify with the [AWS Pricing Calculator](https://calculator.aws/) for real estimates.
- **Always verify service names.** Small models like Nova Micro may occasionally reference services that don't exist (e.g., "Amazon Web Sockets" instead of "API Gateway WebSocket API"). Double-check every recommendation.
- **AI doesn't know your context.** It doesn't know your budget, compliance requirements, team size, or existing infrastructure. Treat recommendations as a starting point, not a final architecture.

## Example Output

**Input:** "Build a food delivery app with live tracking"

**Output:**
- **Frontend:** CloudFront + S3 for web app hosting
- **Backend:** API Gateway + Lambda for serverless compute
- **Database:** DynamoDB for orders and menus
- **Tracking:** Amazon Location Service for live GPS
- **Notifications:** SNS for order updates
- **Auth:** Cognito for user login
- **Estimated cost:** ~$200/month for 10K users

> The actual model output may vary. The prompt is tuned to pick one service per layer, but results depend on the model's interpretation.

## License

MIT
