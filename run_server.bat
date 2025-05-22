@echo off
set HOST_PORT=8100

echo Root: http://localhost:%HOST_PORT%
echo Swagger: http://localhost:%HOST_PORT%/docs
uvicorn main:app --host 0.0.0.0 --port %HOST_PORT%

pause
