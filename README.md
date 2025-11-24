# 🧠 Patient Microservice

This repository contains **Microservice 3** of our team project: the **Patient Profile
This service is designed **API-first**, using **Swagger (OpenAPI 3.0)** to describe the endpoints before implementing any backend code.

---

## 🧩 API Specification
The complete API design lives in [`openapi.yaml`](./openapi.yaml).  
You can view it in:
- **SwaggerHub:** [patient-micro-service v0.1.0](https://app.swaggerhub.com/apis/columbiauniversity-6bc/patient-micro-service/0.1.0)
- **Swagger Editor:** [https://editor.swagger.io](https://editor.swagger.io) → *File → Import File → select `openapi.yaml`*
- **Local mock:** see below for Prism instructions.
**Version:** `0.1.0`  
**Status:** Draft / Sprint 1 deliverable  

---

## 🔗 Resources and Paths

### 👤 Patients
| Method | Path | Description |
|:------:|:-----|:------------|
| `GET` | `/patients` | List all patients |
| `POST` | `/patients` | Create a new patient |
| `GET` | `/patients/{patientId}` | Retrieve a specific patient |
| `PUT` | `/patients/{patientId}` | Update a patient’s information |
| `DELETE` | `/patients/{patientId}` | Delete a patient record |

---

###🚀 Run FastAPI / Microservice
| Command | Description |
|:------:|:------------|
| `uvicorn main:app --reload --host 0.0.0.0 --port 8000` | Start the FastAPI server|
| `curl http://127.0.0.1:8000/patients` | Send GET request (check service is up) |
| `curl -X POST "http://127.0.0.1:8000/patients" -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "age": 30, "condition": "Flu"}'` | POST request |
| `curl -X PUT "http://127.0.0.1:8000/patients/f0499557-8099-45c2-919b-a4b17bf6e276" -H "Content-Type: application/json" -d '{"first_name":"Aris"}'` | Modify the patient tuple in database|
| `source .venv/bin/activate` | activate the .venv environment |
| `curl -i http://127.0.0.1:8000/patients/<id>` | Retrieving patient by patient id|
| `curl -i "http://127.0.0.1:8000/patients/patient-d" -H 'If-None-Match: W/"<your-etag-here>"' ` | chekcing wether or not is been modified |
| `curl -i "http://127.0.0.1:8000/patients?limit=2&offset=0"` | pagination to specify the number of tuple return and number of tuple to skip |

---

### 📊 Usage of Mysql Database
| Command | Description |
|:------:|:------------|
| `sudo service mysql start` | Start MySQL |
| `sudo service mysql stop` | Stop MySQL |
| `sudo service mysql restart` | Restart MySQL |
| `mysql -h 10.128.0.5 -u appuser -p` | Log into the MySQL database running on another VM (IP: 10.128.0.5) (password: 12345) |
