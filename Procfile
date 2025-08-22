web: uvicorn app:app --host 0.0.0.0 --port $PORT

# Step 1: Check if Git is installed
# Run this command. If you get an error, install Git from https://git-scm.com/downloads
git --version

# Step 2: Go inside your FastAPI project folder (make sure app.py, requirements.txt, Procfile are here)
cd path/to/fastapi-math-api

# Step 3: Initialize a Git repository
git init

# Step 4: Configure your GitHub username and email (needed for commits)
git config --global user.name "YourGitHubUsername"
git config --global user.email "your-email@example.com"

# Step 5: Add all files to staging
git add .

# Step 6: Commit files with a message
git commit -m "Initial FastAPI commit"

# Step 7: Connect to GitHub repo (replace URL with your repo URL)
git remote add origin https://github.com/YOUR-USERNAME/fastapi-math-api.git

# Step 8: Push your code to GitHub (main branch)
git branch -M main
git push -u origin main

# Tip: If push fails due to authentication, use a GitHub Personal Access Token instead of a password.

