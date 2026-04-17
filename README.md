# Smart Career Assistance

Smart Career Assistance is an AI-powered career guidance platform designed to help users explore career options, understand required skills, identify skill gaps, and track their learning journey over time.

The project is being developed as a full-stack application with a FastAPI backend and a separate frontend currently under development.

## Project Status

Backend development is functional and actively progressing. Core APIs, authentication, machine learning recommendations, and user history features are implemented.

Frontend development and public deployment are planned in the next phase.

## Core Features

### User Authentication
- Secure user signup and login
- JWT-based protected routes
- Environment-based secret key management

### Career Exploration
Users can search careers and receive:

- Required skills
- Suggested roadmap
- Demand level
- Competition level
- Difficulty level
- Practical feasibility assessment

### AI Career Recommendation
Users can enter their current skills and receive:

- Best matching careers
- Confidence scores
- Skill gap analysis
- Career feasibility insights

### User History
Authenticated users can access their previous activity, including:

- Career searches
- Recommendation requests
- Past outputs
- Timestamped records

This creates the foundation for future progress analytics and dashboards.

## Technology Stack

### Backend
- FastAPI
- Python
- SQLAlchemy
- JWT Authentication
- Pydantic

### Database
- Supabase PostgreSQL

### Machine Learning
- Scikit-learn
- Joblib
- Pandas

### Configuration
- python-dotenv

## Project Structure

```text
Smart-Career-Assistance/
│── app/
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── core/
│   └── main.py
│
│── data/
│── requirements.txt
│── README.md
````

## API Modules

### Authentication

* User registration
* User login
* Protected access control

### Career APIs

* Career information lookup
* Skill gap calculation
* AI career prediction
* User history retrieval

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Career-Assistance.git
cd Smart-Career-Assistance
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create .env File

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

### Run Server

```bash
uvicorn app.main:app --reload
```

## Future Development

### Frontend

A dedicated frontend interface is currently under development and will include:

* Modern responsive UI
* User dashboard
* Career reports
* Visual progress charts
* Integrated authentication flow

### Planned Enhancements

* Expanded career dataset
* Better recommendation engine
* Progress scoring system
* Charts and analytics
* Resume guidance features
* Learning path personalization

## Objective

The purpose of this project is to combine practical software engineering, machine learning, and career guidance into a usable real-world platform.

## Author

Developed as an independent project focused on solving practical career discovery and planning problems.

```
```
