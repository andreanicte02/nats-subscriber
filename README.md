-Este es un subscriber basico de nats

-Para poder utilizar el servicio de nats, lo ideal es crear una vm en la nube (utilize una dist debian)

-Instalar docker 

> sudo apt-get update

> sudo apt-get install docker.io

> sudo systemctl start docker

-Descargar la imagen de nats-streaming

> docker pull nats-streaming

-Crear el contenedor

> docker run -p 4223:4223 -p 8223:8223 nats-streaming -p 4223 -m 8223