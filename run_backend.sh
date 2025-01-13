#!/bin/bash
source backend/myvenv/Scripts/activate
uvicorn backend.app.main:app
