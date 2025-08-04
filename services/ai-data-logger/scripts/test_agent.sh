#!/bin/bash

# Test script for AI Data Logger API
# Usage: ./test_agent.sh [custom_prompt]

set -e

API_URL="http://localhost:8001"
CUSTOM_PROMPT="$1"

# Test prompts
if [ -n "$CUSTOM_PROMPT" ]; then
    PROMPTS=("$CUSTOM_PROMPT")
else
    PROMPTS=(
        "I spent 20 minutes in a 174F sauna at 10:12 am on 2025-07-28"
        "Yesterday at 3pm my blood pressure was 120/80 and heart rate was 65"
        "This morning I weighed 185 lbs with 22% body fat, 85 lbs muscle mass, and 0.38 water ratio"
        "I did a sauna session for 30 minutes this morning and my BP was 118/75 with pulse 70 afterwards"
    )
fi

echo "Testing AI Data Logger API at $API_URL"
echo "============================================"

# Health check first
echo -e "\n🔍 Health check..."
curl -s "$API_URL/health" | jq '.' || echo "Health check failed"

# Test each prompt
for prompt in "${PROMPTS[@]}"; do
    echo -e "\n" "="*60
    echo "📝 Testing prompt: $prompt"
    echo "="*60
    
    # Create JSON payload
    json_payload=$(jq -n --arg content "$prompt" '{
        messages: [
            {
                role: "user",
                content: $content
            }
        ]
    }')
    
    # Make the API call with timeout and better error handling
    echo -e "\n🚀 Sending request..."
    echo "📤 Payload: $json_payload"
    
    response=$(curl -s --max-time 120 --connect-timeout 5 \
        -X POST "$API_URL/chat" \
        -H "Content-Type: application/json" \
        -d "$json_payload" \
        -w "HTTP_STATUS:%{http_code}" \
        2>&1)
    
    # Check if curl succeeded
    if [ $? -ne 0 ]; then
        echo "❌ Curl failed: $response"
        continue
    fi
    
    # Extract HTTP status and response body
    http_status=$(echo "$response" | grep -o "HTTP_STATUS:[0-9]*" | cut -d: -f2)
    response_body=$(echo "$response" | sed 's/HTTP_STATUS:[0-9]*$//')
    
    echo "📊 HTTP Status: $http_status"
    
    # Pretty print the response
    echo -e "\n📋 Response:"
    if [ -n "$response_body" ]; then
        echo "$response_body" | jq '.' 2>/dev/null || echo "$response_body"
    else
        echo "Empty response"
    fi
    
    echo -e "\n⏱️  Waiting 2 seconds before next request..."
    sleep 2
done

echo -e "\n✅ Test completed!"