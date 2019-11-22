#!/usr/bin/env bash
echo '🎶 [SearchLy] Shutting down last containers'
docker-compose -f db/docker-compose.yml down
echo '🎶 [SearchLy] Building and kicking off the PostgresSQL DB container'
docker-compose -f db/docker-compose.yml up -d --build
echo '🎶 [SearchLy] Sleeping 5 seconds for letting the DB initializes'
sleep 5
echo '🎶 [SearchLy] Creating DDL Base'
docker run -it --rm --network searchly searchly_db psql -h searchly_db -U postgres postgres -f /tmp/create_ddl_base.sql
echo '🎶 [SearchLy] DDL Base created'
echo '🎶 [SearchLy] Creating DDL SearchLy (v1)'
docker run -it --rm --network searchly searchly_db psql -h searchly_db -U searchly searchly -f /tmp/create_ddl_searchly_v1.sql
echo '🎶 [SearchLy] DDL SearchLy (v1) created'
echo '🎶 [SearchLy] Done!'