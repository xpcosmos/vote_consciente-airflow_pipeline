#!/bin/bash


# ---------------------------------
# Script: iniciar-ambiente
# Autor: Mikeias oliveira <mikeias.d.s.o@gmail.com>
# Versão: 0.1
# ---------------------------------
# Uso: Iniciar ambiente do Airflow
# ---------------------------------

source .env/bin/activate
export AIRFLOW_HOME=$(pwd)/airflow;


airflow webserver;