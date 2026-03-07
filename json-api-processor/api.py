import json
api_response= '''
 {
  "id" :"req_123",
  "status": "success",
  "result": {
        "text": "Hello world",
        "confidence" : 0.98
   }

   }
    '''
response_data = json.loads(api_response)

request_id= response_data["id"]
status = response_data["status"]
text_results = response_data["result"]["text"]
confidence_score= response_data["result"]["confidence"]

print("Request ID:", request_id)
print("Status:", status)
print("Text:", text_results)
print("Confidence:", confidence_score)

if confidence_score < 0.9:
    print("Warning: Confidence score is below 0.9")

followup_result ={
    "request_id": request_id,
    "status": status,
    "processed_text": text_results,
    "confidence": confidence_score
}

json_output= json.dumps(followup_result, indent=4)

with open("response.json", "w") as file:
    file.write(json_output)