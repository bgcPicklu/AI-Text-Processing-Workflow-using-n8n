### **AI Text Processing Workflow**

A simple AI workflow application using:

* **Streamlit** → Frontend UI
* **FastAPI** → Backend API
* **n8n** → Workflow automation

The app collects user input from Streamlit, sends it to a FastAPI backend, and then triggers an n8n webhook workflow.

#### **Project Structure**
project-folder/
│
├── app.py               # Streamlit frontend
├── main.py              # FastAPI backend
├── .env                 # Environment variables
├── requirements.txt
└── README.md

#### **Features**
* User-friendly Streamlit interface
* FastAPI backend API
* Generates unique session IDs
* Sends data to n8n webhook
* Environment variable support using .env
* Error handling included

#### **Tech Stack**
* Python
* Streamlit
* FastAPI
* Uvicorn
* Requests
* python-dotenv
* n8n
* Installation

#### **1. Clone the Repository**
git clone https://github.com/your-username/ai-text-processing-workflow.git

cd ai-text-processing-workflow

#### **2. Install Dependencies**
pip install -r requirements.txt

#### **Environment Variables**

Create a .env file in the root directory:
    N8N_WEBHOOK_URL=https://shoumendas.app.n8n.cloud/webhook-test/process

#### **Running the Application**
  ##### **Start FastAPI Backend**
    uvicorn backend.main:app --reload

#### **Start Streamlit Frontend**
  ##### **Open another terminal and run:**
    streamlit run frontend/app.py

#### **API Endpoint**
  ##### **POST** /process
    **Request Body**
      {
        "email": "user@example.com",
        "text": "Hello AI"
      }
    
    **Response**
      {
        "message": "Workflow triggered successfully",
        "session_id": "uuid-generated-id",
        "n8n_response": "response from n8n"
      }

#### **Future Improvements**
* Add database support
* Add authentication
* Add AI model integration
* Docker support
* Deployment on Render/Railway/AWS

#### **Author**
Shoumen Das

#### **License**
This project is licensed under the MIT License.