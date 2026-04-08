---
title: Urban Heat Reduction Environment
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
---

# Urban Heat Reduction Environment

## Overview

This project simulates an urban heat mitigation system where an AI agent plants trees to reduce temperature.

## Motivation

Urban heat islands are caused by dense construction and lack of greenery.

## Environment Design

### State

* 5x5 temperature grid (30-40°C)
* Building map (0 = empty, 1 = building)
* Tree placements

### Actions

* Plant a tree at (x, y)

### Constraints

* Limited trees
* Cannot plant on buildings
* Cannot reuse same location

### Reward

* Based on temperature reduction
* Penalizes invalid actions

## Tasks

* Easy: cool hotspots
* Medium: reduce average temperature
* Hard: optimize placement

## Run

```bash
python inference.py
```
