---
title: Urban Heat Reduction Environment
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
---

# Urban Heat Reduction Environment

## Why this matters

Urban heat islands are a major real-world problem caused by dense construction and lack of greenery.
This project demonstrates how **AI agents can optimize tree placement** to reduce city temperatures efficiently.

---

## Live Demo

API Docs:
https://sagar312-urban-heat-env.hf.space/docs

Demo Simulation:
https://sagar312-urban-heat-env.hf.space/demo

---

## Overview

An AI-compatible environment where an agent interacts with a city grid and places trees strategically to minimize temperature.

---

## Features

* 5x5 temperature grid (30–40°C)
* Building constraints (no planting on buildings)
* Tree placement actions
* Reward-based optimization
* AI-friendly API interface

---

## API Endpoints

* `POST /reset` → Initialize environment
* `POST /step` → Perform an action
* `GET /state` → Retrieve current state
* `GET /docs` → Interactive API (Swagger UI)
* `GET /demo` → Quick simulation

---

## Example Flow

1. Reset environment
2. Agent selects a position
3. Tree is planted
4. Temperature reduces
5. Repeat to optimize cooling

---

## Optimization Strategy — Greedy Approach

The agent follows a **greedy optimization strategy**:

* At each step, it selects the grid position with the **highest temperature**
* This ensures **maximum immediate cooling**
* It prioritizes **hotspot reduction over random placement**

This approach is efficient and suitable for **real-time urban planning scenarios**

---

## How it works

1. Initialize temperature grid
2. Identify hottest regions
3. Place trees strategically
4. Reduce surrounding temperature
5. Maximize overall cooling

---

## Example Impact

**Before:**
High temperature zones across the grid

**After:**
Strategic tree placement reduces hotspots significantly

---

## Run Locally

```bash
python inference.py
```

---

## Future Scope

* Smarter AI agents (RL-based optimization)
* Larger city simulations
* Integration with real-world urban data
* Visualization dashboard

---
