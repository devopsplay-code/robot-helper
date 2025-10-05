import os

# GitHub gives us the username in an environment variable
username = os.getenv("GITHUB_ACTOR", "stranger")

print(f"Hello, {username}! 👋🤖")
