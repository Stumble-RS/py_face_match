# py_face_match

Study and improve later on for lewd image handling & faster face recognition. [LINK](https://superfastpython.com/multiprocessing-pool-python/#How_to_Use_Poolmap_async)

## Installation

```bash
source venv/bin/activate
flask --app main run
flask run
gunicorn -w 4 'main:app'

# to close
deactivate
```

Updating:
```bash
docker build -t stumble-facematch --platform linux/amd64 .
docker tag stumble-facematch:latest public.ecr.aws/n0u1m4r2/stumble-face-match:latest
docker push public.ecr.aws/n0u1m4r2/stumble-face-match:latest
```
