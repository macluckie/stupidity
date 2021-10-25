#!/bin/bash
where=$(pwd)
echo $where 
cd $where
docker-compose down 
docker-compose up -d
exit 0
