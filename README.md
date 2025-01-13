# Pizza App
## Full Stack Developer Candidate - Emilio ("Leo") Segovia

### Instruction to run locally
1. Ensure you have python3 (developed with python 3.12.8) and Node.js (developed with node v23.6.0) on the system where you want to run the app locally.
2. In one terminal tab, run **./run_backend.sh**
3. Create file **frontend/pizza-app/.env.local** and save the following line in it: **NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000** (or whatever URL shows up in the backend terminal output next to **"Uvicorn running on..."**)
4. In another terminal run **./run_frontend.sh** (May take a while to install node dependencies)
5. Open the backend fastAPI interface by opening **http://localhost:8000/docs** in a web browser (or whatever URL shows up in the backend terminal output next to **"Uvicorn running on..."**)
6. Open the frontend interface by opening **http://localhost:3000** in a web browser (or whatever URL shows up in the frontend terminal output next to **"Local: "**)

Note that any issues with unpacking the python venv virtual environment in run_backend.sh may be impacted by your python version.
Likewise, any issues with running **npm install** (within run_frontend.sh) may be affected by your Node version.

### Python pip packages in "myvenv" virtual environment:  <br />
annotated-types   0.7.0      <br />
anyio             4.8.0      <br />
certifi           2024.12.14 <br />
click             8.1.8      <br />
colorama          0.4.6      <br />
fastapi           0.115.6    <br />
greenlet          3.1.1      <br />
h11               0.14.0     <br />
httpcore          1.0.7      <br />
httpx             0.28.1     <br />
idna              3.10       <br />
iniconfig         2.0.0      <br />
packaging         24.2       <br />
pip               24.3.1     <br />
pluggy            1.5.0      <br />
pydantic          2.10.5     <br />
pydantic_core     2.27.2     <br />
sniffio           1.3.1      <br />
SQLAlchemy        2.0.37     <br />
starlette         0.41.3     <br />
typing_extensions 4.12.2     <br />
uvicorn           0.34.0     <br />
