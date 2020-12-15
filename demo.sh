echo Launching docker containers
sudo docker-compose up -d --build
sleep 5

echo calling demo API
curl "localhost:8000/users/"
echo ""

echo showing remote log file captured in kiroku service
sudo docker exec -t remote_logger_demo_kiroku_1 cat /var/log/remote/remote_logger_demo_api_1.remote_logger_demo_default.log

echo bringing down docker containers
sudo docker-compose down
