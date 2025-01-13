# Pizza App
## Full Stack Developer Candidate - Emilio ("Leo") Segovia

### View the Deployed App
The Frontend is deployed to: https://pizza-app-1073187497320.us-west4.run.app
The Backend is deployed to:  https://pizza-app-backend-1073187497320.us-west4.run.app/docs

### Instruction to run locally
1. Create file **frontend/.env.local** and save the following line in it: **NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8080**
2. If you have docker installed, then at the root where docker-compose.yml is, run: **docker-compose up**, verify that uvicorn is running on the URL specified in **frontend/.env.local**
3. Ensure you have python3 (developed with python 3.12.8) and Node.js (developed with node v23.6.0) on the system where you want to run the app locally.
4. In one terminal tab, run **./run_backend.sh**
5. Ensure that **frontend/.env.local** exists and has the line: **NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8080** (or whatever URL shows up in the backend terminal output next to **"Uvicorn running on..."**)
6. In another terminal run **./run_frontend.sh** (May take a while to install node dependencies)
7. Open the backend fastAPI interface by opening **http://localhost:8080/docs** in a web browser (or whatever URL shows up in the backend terminal output next to **"Uvicorn running on..."**)
8. Open the frontend interface by opening **http://localhost:3000** in a web browser (or whatever URL shows up in the frontend terminal output next to **"Local: "**)

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

## App Overview
This app allows users to create/update/delete a pizza and adjust the toppings on it. It also allows users to create/update/delete toppings that are available for pizzas. For the backend I chose python because I have experience wth python backends and it's very easy to prototype with FastAPI which was perfect for efficient development. The backend implements the create/update/delete API for both pizzas and available toppings very clearly and is easy to maintain.<br/><br/>

For the frontend, I chose react and used the Next.js react framework to setup the per react.dev documentation. After getting the backend working, I made a simple frontend in a single page.tsx file including all components and styles. Ideally I would break these up into modular and maintainable separate files but given the limited time I had to develop this, I implemented core functionality without frontend cleanup.<br/><br/>

For the backend tests, I spent a good amount of time implementing the code but didn't have enough time to get the database to properly cleanup between tests. The unitttest framework is suppsoed to ensure the database is empty before each test but that is not the case so the tests report errrors. However, the baseline is there and shows how I would unittest. There are other frameowrks for deveoping standalone unit tests including pytest and I would use whatever my team is using. But I like how these tests can run without having to run any server.
