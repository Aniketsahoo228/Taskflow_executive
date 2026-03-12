TaskFlow Executive

A full-stack task management application built with Swiss Utility design principles — clean, functional, and intentional

Overview
TaskFlow Executive is a full-stack MVP task management system featuring JWT-based authentication, complete CRUD operations, and a dashboard designed around Swiss aesthetic principles — Archivo/Manrope typography, International Orange accents, and a Bento grid layout.

Features

Authentication — Register and login with JWT tokens; protected routes on both frontend and backend
Task Management — Create, read, update, and delete tasks with title, description, status, priority, due dates, and categories
Filtering & Search — Filter by status (pending/completed), priority level, and real-time keyword search
Dashboard — Summary statistics with a Bento grid layout for quick situational awareness
Notifications — Toast feedback on all user actions
Persistence — MongoDB for data storage; localStorage for session management


Folder Structure
Taskflow_executive/
│
├── backend/                     # Express.js API server
│   ├── config/
│   │   └── db.js                # MongoDB connection setup
│   │
│   ├── controllers/
│   │   ├── authController.js    # Register / Login logic
│   │   └── taskController.js    # CRUD handlers for tasks
│   │
│   ├── middleware/
│   │   └── authMiddleware.js    # JWT authentication middleware
│   │
│   ├── models/
│   │   ├── User.js              # Mongoose User schema
│   │   └── Task.js              # Mongoose Task schema
│   │
│   ├── routes/
│   │   ├── authRoutes.js        # /api/auth endpoints
│   │   └── taskRoutes.js        # /api/tasks endpoints
│   │
│   ├── .env                     # Environment variables (not committed)
│   ├── package.json
│   └── server.js                # Express server entry point
│
├── frontend/                    # React client application
│   ├── public/
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── components/
│   │   │
│   │   │   ├── Auth/
│   │   │   │   ├── Login.jsx
│   │   │   │   └── Register.jsx
│   │   │   │
│   │   │   ├── Dashboard/
│   │   │   │   ├── Dashboard.jsx     # Stats + Bento grid layout
│   │   │   │   └── StatsCard.jsx
│   │   │   │
│   │   │   ├── Tasks/
│   │   │   │   ├── TaskList.jsx
│   │   │   │   ├── TaskCard.jsx
│   │   │   │   ├── TaskForm.jsx      # Create / edit form
│   │   │   │   └── TaskFilters.jsx   # Status, priority, search bar
│   │   │   │
│   │   │   └── UI/
│   │   │       ├── Toast.jsx
│   │   │       └── Navbar.jsx
│   │   │
│   │   ├── context/
│   │   │   └── AuthContext.jsx      # Global authentication state
│   │   │
│   │   ├── services/
│   │   │   └── api.js               # Axios instance + API calls
│   │   │
│   │   ├── App.jsx                  # App routes + layout
│   │   └── index.js
│   │
│   └── package.json
│
├── tests/                          # Integration and unit tests
├── test_reports/                   # Test execution reports
├── memory/                         # Agent memory / session artifacts
│
├── .emergent/
│   └── backend_test.py             # Python-based backend smoke tests
│
├── design_guidelines.json          # Swiss Utility design token reference
├── test_result.md                  # Latest automated test summary
│
├── .gitignore
└── README.md

Tech Stack
LayerTechnologyFrontendReact, React Router, AxiosBackendNode.js, Express.jsDatabaseMongoDB + MongooseAuthJWT (JSON Web Tokens)StylingCustom CSS — Swiss Utility system (Archivo / Manrope)TestingPython (backend smoke tests)

Getting Started
Prerequisites

Node.js v18+
MongoDB (local or Atlas)
npm or yarn

Backend Setup
bashcd backend
npm install
Create a .env file in /backend:
envPORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret_key
Start the server:
bashnpm run dev
Frontend Setup
bashcd frontend
npm install
npm start
The app will be available at http://localhost:3000.

API Reference
Auth
MethodEndpointDescriptionPOST/api/auth/registerRegister a new userPOST/api/auth/loginLogin and receive JWT token
Tasks
All task routes require Authorization: Bearer <token> in the request header.
MethodEndpointDescriptionGET/api/tasksFetch all tasks for the authenticated userPOST/api/tasksCreate a new taskPUT/api/tasks/:idUpdate an existing taskDELETE/api/tasks/:idDelete a task

Task Schema
json{
  "title": "string (required)",
  "description": "string",
  "status": "pending | completed",
  "priority": "low | medium | high",
  "dueDate": "ISO 8601 date string",
  "category": "string"
}

Design System
TaskFlow Executive uses a Swiss Utility design language:

Fonts — Archivo (headings) + Manrope (body)
Accent — International Orange #FF4500
Layout — Bento grid dashboard, high-density data presentation
Principle — Function first; every element earns its place

Design tokens are documented in design_guidelines.json at the project root.

Testing
Run backend smoke tests:
bashpython backend_test.py
Test results are saved to test_result.md and detailed reports to test_reports/.
Current test coverage:

✅ Auth flows (register, login, invalid credentials)
✅ CRUD operations (create, read, update, delete tasks)
✅ Filter and search behavior
✅ Protected route enforcement


Roadmap

 Drag-and-drop task reordering
 Team collaboration and task assignment
 Email / push notifications for due dates
 Dark mode toggle
 Export tasks to CSV / PDF
 Deployment (Vercel + Railway or Render)


Contributing

Fork the repo
Create a feature branch: git checkout -b feature/your-feature
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/your-feature
Open a Pull Request# Here are your Instructions
