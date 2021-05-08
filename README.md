# Barcode Bank

Barcode Bank is a dockerized FastAPI & PostgreSQL REST API that can used to get the disposal information based of the barcode. 

## Prerequisites

Make sure you install Docker on your computer at using [Docker's instructions](https://docs.docker.com/get-docker/) depending on your operating system.

You also need Docker Compose as well. If you use Windows or Mac, it is already included in the install with Docker. Otherwise, you should follow these instructions to install [Docker Compose](https://docs.docker.com/compose/install/).

## Installation

Clone this repo to your local machine using ```git clone https://github.com/zotbins/Barcode_Bank.git```

Inside that folder, create an ```.env``` using ```.env.example``` as a template.

### Starting Your Docker Containers

Now, you can start your docker containers using the command ```docker-compose up -d```

You should be able to access your API by going to the link determined by their ```HOST``` & ```PORT``` enviromental variables. 

You can stop your docker containers using ```docker-compose down```

### Migrating Your Database

Your database tables has not been properly created yet, so we will use Alembic to migrate your database.

You need to access your FastAPI Docker container, so you would need the ID of the process, so run the command

```
docker ps
```

You should see an output similar to 
```
CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS                    NAMES
6095b199b38f   barcode_bank_server   "/start.sh"              28 minutes ago   Up 28 minutes   0.0.0.0:80->80/tcp       barcode_bank_server_1
b0d71c79c22b   postgres:13-alpine    "docker-entrypoint.s…"   4 hours ago      Up 28 minutes   0.0.0.0:5432->5432/tcp   barcode_bank_db_1    
```

Copy the ID of the container running our server. Based off the example, you can now migrate your database by using the command

```
docker exec -it 6095b199b38f alembic upgrade head
```

To make sure the database has been modified correctly, go to the PostgreSQL container. Based off the example, you run the command filling in the spaces with the appropriate enviromental variables
```
docker exec -it b0d71c79c22b psql -U POSTGRES_USER --db=POSTGRES_DB
```

Afterwards, if you run
```
\d barcodes 
```

If you see 3 columns for the barcode table, you successfully migrated your database! 

You have successfully set up Barcode Bank!


