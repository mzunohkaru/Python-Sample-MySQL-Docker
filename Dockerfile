FROM python:3.9

# 新しいユーザーmyuserを作成し、そのユーザーとして以降の命令を実行
# RUN adduser --disabled-password --gecos '' myuser

RUN apt update&& apt install -y python3-pip

# デフォルトでrootユーザーとして実行されており、コンテナ内部からホストシステムに対する攻撃が可能なため、非rootユーザーを指定することで、セキュリティの向上を図る
# USER myuser

WORKDIR /app
# Dockerコンテナ内にディレクトリを作り、そこへ移動する

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/ .
