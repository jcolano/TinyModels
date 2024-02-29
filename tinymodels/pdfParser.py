import requests
import base64
import json
import time

class pdfParser:
    def __init__(self):
        self.api_endpoint = 'https://tinymodels.ws/tmapi.svc/pdfParser/get_text'

    def getText(self, filename):
        # Encode the PDF file to base64
        with open(filename, 'rb') as file:
            file_base64 = base64.b64encode(file.read()).decode('utf-8')

        # Prepare the request data
        data = json.dumps({'FileBase64': file_base64})
        headers = {'Content-Type': 'application/json'}

        # Step 1: Upload the file
        response = requests.post(self.api_endpoint, data=data, headers=headers)
        if response.status_code != 200:
            raise Exception("Error uploading file")

        # Extract the job ID
        job_id = response.json()['JobId']

        # Step 2: Poll for completion
        text = self._poll_for_completion(job_id)
        return text

    def _poll_for_completion(self, job_id):
        poll_endpoint = f"{self.api_endpoint}/{job_id}"  # Adjust if your service uses a different endpoint for polling
        while True:
            response = requests.get(poll_endpoint)
            if response.status_code == 200 and response.json()['Status'] == 'completed':
                return response.json()['Text']
            elif response.json()['Status'] == 'error':
                raise Exception("Error processing file")
            time.sleep(1)  # Wait for 1 second before polling again
