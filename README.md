---
title: Urban Heat Reduction Environment
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
---

#  Urban Heat Reduction Environment

##  Live API
https://sagar312-urban-heat-env.hf.space/docs

---

## Overview
This project simulates an urban heat mitigation system where an AI agent plants trees to reduce temperature in a city grid.

---

## Features
- 5x5 temperature grid (30–40°C)
- Building constraints
- Intelligent tree placement
- Reward-based optimization

---

## API Endpoints

- `POST /reset` → Start environment  
- `POST /step` → Take action  
- `GET /state` → Get current state  
- `GET /docs` → Interactive API  

---

## Example Flow

1. Reset environment  
2. Place tree using `/step`  
3. Observe temperature reduction  

---

## Run Locally
```bash
python inference.py
