#!/bin/bash
source backend/myvenv/Scripts/activate
uvicorn backend.main:app

