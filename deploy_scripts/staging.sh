cd sample
docker-compose -f production.yml stop kafka_consumer django traefik
git fetch origin
git checkout main
git pull origin main
docker-compose -f production.yml build
docker-compose -f production.yml up -d django kafka_consumer traefik
docker system prune -f -a
