---
title: Urban Heat Reduction Environment
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
---

# Urban Heat Reduction Environment

## Why this matters
Urban heat islands are a real-world problem caused by dense construction and lack of greenery.  
This project demonstrates how AI agents can optimize tree placement to reduce city temperatures.

---

## Live Demo
API Docs:  
https://sagar312-urban-heat-env.hf.space/docs  

Demo Simulation:  
https://sagar312-urban-heat-env.hf.space/demo  

---

## Overview
An AI-compatible environment where an agent plants trees on a grid to minimize temperature.

---

## Features
- 5x5 temperature grid (30–40°C)
- Building constraints
- Tree placement strategy
- Reward-based optimization

---

## API Endpoints

- `POST /reset` → Start environment  
- `POST /step` → Take action  
- `GET /state` → Get current state  
- `GET /docs` → Interactive API  
- `GET /demo` → Quick simulation  

---

## Example Flow

1. Reset environment  
2. Place trees strategically  
3. Observe temperature reduction  
4. Optimize placement  

---

## How it works

1. Environment initializes temperature grid  
2. Agent selects position  
3. Tree reduces nearby temperature  
4. Reward is calculated  
5. Process repeats  

---

## Example Impact

Before:
High temperature zones across grid  

After:
Strategic tree placement reduces hotspots significantly  

---

## Run Locally

```bash
python inference.py