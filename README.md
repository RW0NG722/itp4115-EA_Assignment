# itp4115-EA_Assignment

vue3 + flask, rebuild https://www.cinema.com.hk

## Front end environment and use

nodejs : 22.14.0
pnpm 9.12.2

`pnpm i` install the dependences

`pnpm vite` run

Go to http://localhost:5173/ on your browser

## Backend environment and use

python3.12.6
Flask2.3.3
MySQL5.7.26

create database via `cinema0.sql`

`pip install -r requirements.txt` install the requirements

`flask run -h 0.0.0.0` run the flask

## New codespace startup code:

docker pull mysql:8.0.42

docker run --name mysql-container \
-e MYSQL_ROOT_PASSWORD=123456 \
-e MYSQL_ROOT_HOST=% \
-e MYSQL_DATABASE=cinema \
-p 3306:3306 \
-d mysql:8.0.42

~~docker exec mysql-container mysql -uroot -p123456 -e "SELECT 1;"~~

if grep -qE '^127.0.0.1\s+db(\s|$)' /etc/hosts; then echo 'hosts entry exists'; else echo '127.0.0.1 db' | sudo tee -a /etc/hosts >/dev/null || echo 'sudo failed'; fi

~~getent hosts db || grep -n 'db' /etc/hosts || true~~

cd cinema_back_end/

docker exec -i mysql-container mysql -uroot -p123456 cinema < cinema0.sql && echo 'sql import done'

### Backend setup and run:

cd /workspaces/itp4115-EA_Assignment/cinema_back_end && python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
cd /workspaces/itp4115-EA_Assignment/cinema_back_end && . .venv/bin/activate && flask run -h 0.0.0.0 -p 5000

### Frontend setup and run in different terminal:

cd /workspaces/itp4115-EA_Assignment/cinema_front_end && pnpm install

cd /workspaces/itp4115-EA_Assignment/cinema_front_end && pnpm dev --host 0.0.0.0 --port 5173


## After codespace rebot
docker ps -all

docker rm xxxxx

docker run --name mysql-container \
-e MYSQL_ROOT_PASSWORD=123456 \
-e MYSQL_ROOT_HOST=% \
-e MYSQL_DATABASE=cinema \
-p 3306:3306 \
-d mysql:8.0.42

~~docker exec mysql-container mysql -uroot -p123456 -e "SELECT 1;"~~

~~getent hosts db || grep -n 'db' /etc/hosts || true~~

cd cinema_back_end/

if grep -qE '^127.0.0.1\s+db(\s|$)' /etc/hosts; then echo 'hosts entry exists'; else echo '127.0.0.1 db' | sudo tee -a /etc/hosts >/dev/null || echo 'sudo failed'; fi

docker exec -i mysql-container mysql -uroot -p123456 cinema < cinema0.sql && echo 'sql import done'

### Backend setup and run:

cd /workspaces/itp4115-EA_Assignment/cinema_back_end && python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

cd /workspaces/itp4115-EA_Assignment/cinema_back_end && . .venv/bin/activate && flask run -h 0.0.0.0 -p 5000

### Frontend setup and run in different terminal:

cd /workspaces/itp4115-EA_Assignment/cinema_front_end && pnpm install

cd /workspaces/itp4115-EA_Assignment/cinema_front_end && pnpm dev --host 0.0.0.0 --port 5173
