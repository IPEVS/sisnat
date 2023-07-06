aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 793035497814.dkr.ecr.us-east-2.amazonaws.com
docker build -t sisnat/sisnat_nginx .
docker tag sisnat/sisnat_nginx:latest 793035497814.dkr.ecr.us-east-2.amazonaws.com/sisnat/sisnat_nginx:latest
docker push 793035497814.dkr.ecr.us-east-2.amazonaws.com/sisnat/sisnat_nginx:latest
