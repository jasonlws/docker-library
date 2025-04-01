# microsoft/mssql-server

## Docker run

```bash
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=yourStrong(!)Password" -p 1433:1433  --name mssql --hostname mssql -d mcr.microsoft.com/mssql/server:2022-latest
```

## Docker compose 

```bash
docker-compose -f docker-compose.yml --env-file .env up
```

## Customize image

### 1. Go to [jasonlws_mssql-server](https://github.com/jasonlws/docker-library/tree/master/microsoft_mssql-server/jasonlws_mssql-server) folder

### 2. Update your init data

Update [setup.sql](https://github.com/jasonlws/docker-library/blob/master/microsoft_mssql-server/jasonlws_mssql-server/setup.sql) file

```sql
CREATE DATABASE jasonlws;
GO

USE jasonlws;
```

### 3. Build your image from Dockerfile

```bash
docker build -t jasonlws/mssql:2022-latest --build-arg IMAGE_NAME=mcr.microsoft.com/mssql/server --build-arg IMAGE_TAG=2022-latest --no-cache .
```

### 4. Run it

#### A. Docker run

```bash
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=yourStrong(!)Password" -p 1433:1433  --name mssql --hostname mssql -d jasonlws/mssql:2022-latest
```

#### B. Docker compose

```bash
docker-compose -f docker-compose.yml --env-file .env.jasonlws up
```

## General resources

1. [Docker Hub Link](https://hub.docker.com/r/microsoft/mssql-server)
2. [GitHub Link](https://github.com/Microsoft/mssql-docker)
3. [Environment Variables](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-configure-environment-variables)

## License

MIT - a permissive free software license originating at the Massachusetts Institute of Technology (MIT), it puts only very limited restriction on reuse and has, therefore, an excellent license compatibility. It permits reuse within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.

Check the [LICENSE file](https://github.com/jasonlws/docker-library/blob/master/LICENSE) for more details.