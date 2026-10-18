# Sample Outputs

## Example 1: Food Delivery App

**Input:** "Food delivery app with live tracking"

**AI Recommendation:**
- Frontend: CloudFront + S3
- Backend: API Gateway + Lambda
- Database: DynamoDB for orders
- Tracking: Amazon Location Service
- Notifications: SNS for order updates
- Auth: Cognito
- Estimated cost: ~$200/month for 10K users

## Example 2: Real-time Chat App

**Input:** "Real-time chat app for 1000 users"

**AI Recommendation:**
- WebSocket: API Gateway WebSocket API
- Compute: Lambda for message handling
- Storage: DynamoDB for chat history
- Real-time: AppSync for pub/sub
- Auth: Cognito
- Estimated cost: ~$50/month
