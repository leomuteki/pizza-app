#!/bin/bash
source backend/myvenv/Scripts/activate
python -m unittest backend.app.test_main
