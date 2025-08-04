# Deploying Rasa Chatbot on Coolify

This guide explains how to deploy the Rasa chatbot on Coolify.

## Prerequisites

1. Coolify instance running
2. Docker support enabled
3. Domain/subdomain configured

## Deployment Steps

### Option 1: Using Docker Compose (Recommended)

1. **Create a new project in Coolify**
   - Go to your Coolify dashboard
   - Click "New Project"
   - Choose "Docker Compose"

2. **Upload the docker-compose.coolify.yml**
   - Copy the contents of `docker-compose.coolify.yml`
   - Paste it in the Coolify compose editor

3. **Configure Environment Variables**
   - No additional environment variables needed for basic setup
   - All configurations are handled in the compose file

4. **Deploy**
   - Click "Deploy"
   - Wait for the build and deployment process

### Option 2: Using Single Container

1. **Create a new project in Coolify**
   - Choose "Docker Image"
   - Use the main Dockerfile

2. **Configure the container**
   - Port: 5005
   - Health check: `/version`
   - Build context: root directory

3. **Deploy**
   - Click "Deploy"

## Service Configuration

### Main Rasa Server
- **Port**: 5005
- **Health Check**: `GET /version`
- **API Endpoint**: `/webhooks/rest/webhook`

### Action Server (if using custom actions)
- **Port**: 5055
- **Health Check**: `GET /health`

## Accessing the Bot

Once deployed, you can access:

1. **API Endpoint**: `https://your-domain.com/webhooks/rest/webhook`
2. **Web Interface**: `https://your-domain.com/web/`
3. **Health Check**: `https://your-domain.com/version`

## Testing the Deployment

Send a test message to verify the bot is working:

```bash
curl -X POST https://your-domain.com/webhooks/rest/webhook \
     -H "Content-Type: application/json" \
     -d '{"sender": "test", "message": "hello"}'
```

## Troubleshooting

### Common Issues

1. **Build Failures**
   - Check if all files are properly copied
   - Verify Dockerfile syntax
   - Check build logs in Coolify

2. **Health Check Failures**
   - Ensure the service is listening on the correct port
   - Verify health check endpoints are accessible

3. **CORS Issues**
   - The bot is configured with `--cors "*"` for development
   - For production, configure specific origins in `credentials.yml`

### Logs

Check logs in Coolify dashboard:
- Build logs for deployment issues
- Runtime logs for application errors

## Production Considerations

1. **Security**
   - Configure specific CORS origins
   - Use HTTPS
   - Set up proper authentication if needed

2. **Scaling**
   - Monitor resource usage
   - Consider horizontal scaling for high traffic

3. **Monitoring**
   - Set up health checks
   - Monitor response times
   - Track conversation metrics

## Custom Actions

If you're using custom actions:
1. Both services (rasa-server and rasa-actions) will be deployed
2. They communicate internally via Docker network
3. Only the main Rasa server needs to be exposed publicly