# Alfa Bot Hoster (ABH)

Deploy your Python bots instantly on Railway.com with Firebase Auth + Realtime DB.

## Files

- `index.html` — Full frontend web app
- `Dockerfile` — For Railway deployment
- `bot.py` — Sample bot template
- `requirements.txt` — Python dependencies

## Railway Deploy Steps

1. Push all files to a GitHub repo
2. Go to railway.com → New Project → Deploy from GitHub
3. Select your repo — Railway auto-detects Dockerfile
4. Set environment variables if needed (e.g. BOT_TOKEN)
5. Deploy! Your site will be live at `yourapp.railway.app`

## Firebase Setup

The app uses your Firebase project:
- Auth: Email/Password (enable in Firebase Console)
- Realtime DB: Rules set to authenticated users only
- Storage: For uploading bot files

## Firebase Realtime DB Rules (paste in Firebase Console)

```json
{
  "rules": {
    "users": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid"
      }
    }
  }
}
```

## Firebase Storage Rules

```
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{uid}/{allPaths=**} {
      allow read, write: if request.auth != null && request.auth.uid == uid;
    }
  }
}
```
