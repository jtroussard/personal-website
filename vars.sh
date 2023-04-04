#!/bin/bash
export APP_DIR=/home/$(whoami)/service/personal-website/
export VENV_DIR=/home/$(whoami)/service/personal-website/venv/
export WORKER_COUNT=$((($(nproc)/2)+1))