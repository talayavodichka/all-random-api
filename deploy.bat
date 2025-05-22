@echo off
set IMAGE_NAME=all-random-api
set CONTAINER_NAME=all-random-api
set HOST_PORT=8100
set CONTAINER_PORT=8000

echo [1/5] Stopping and removing previous container...
docker stop %CONTAINER_NAME% 2> nul || echo Container does not exist, skipping...
docker rm %CONTAINER_NAME% 2> nul || echo Container removal skipped...

echo [2/5] Removing old image...
docker rmi %IMAGE_NAME% 2> nul || echo Image does not exist, skipping...

echo [3/5] Building new Docker image...
docker build -t %IMAGE_NAME% .

echo [4/5] Starting container...
docker run -d -p %HOST_PORT%:%CONTAINER_PORT% --name %CONTAINER_NAME% %IMAGE_NAME%

echo [5/5] Service info:
echo --------------------------------------
echo Root: http://localhost:%HOST_PORT%
echo Swagger: http://localhost:%HOST_PORT%/docs
echo --------------------------------------

timeout /t 3 /nobreak > nul
docker logs %CONTAINER_NAME%
pause
