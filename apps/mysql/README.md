# Template

## Docker run

```bash
docker run -e "MYSQL_ROOT_PASSWORD=yourStrong(!)Password" -p 3306:3306  --name mysql --hostname mysql -d mysql:9.2.0
```

## Docker compose 

```bash
docker-compose -f docker-compose.yml --env-file .env up
```

## Customize image

### 1. Go to [jasonlws_mysql](https://github.com/jasonlws/docker-library/tree/master/mysql/jasonlws_mysql) folder

### 2. Update your init data

Update [setup.sql](https://github.com/jasonlws/docker-library/blob/master/mysql/jasonlws_mysql/setup.sql) file

```sql
CREATE DATABASE IF NOT EXISTS `jasonlws` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GO
USE `jasonlws`;
GO
```

### 3. Build your image from Dockerfile

```bash
docker build -t jasonlws/mysql:9.2.0 --build-arg IMAGE_NAME=mysql --build-arg IMAGE_TAG=9.2.0 --no-cache .
```

### 4. Run it

#### A. Docker run

```bash
docker run -e "MYSQL_ROOT_PASSWORD=yourStrong(!)Password" -p 3306:3306  --name mysql --hostname mysql -d jasonlws/mysql:9.2.0
```

#### B. Docker compose

```bash
docker-compose -f docker-compose.yml --env-file .env.jasonlws up
```

## General resources

1. [Docker Hub Link](https://hub.docker.com/_/mysql)
2. [GitHub Link](https://github.com/docker-library/mysql)
3. [Environment Variables](https://dev.mysql.com/doc/refman/9.2/en/environment-variables.htmls)


## License

MIT - a permissive free software license originating at the Massachusetts Institute of Technology (MIT), it puts only very limited restriction on reuse and has, therefore, an excellent license compatibility. It permits reuse within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.

Check the [LICENSE file](https://github.com/jasonlws/docker-library/blob/master/LICENSE) for more details.