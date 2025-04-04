# Kubernetes HPA with Custom Metrics 

This project demonstrates how to autoscale a Python-based Kubernetes application using a custom Prometheus metric (`http_request_count`) with Horizontal Pod Autoscaler (HPA), Prometheus Adapter, and K3D.

## 🧱 Stack

- K3D (lightweight Kubernetes in Docker)
- Python Flask app exposing Prometheus metrics
- Prometheus
- Prometheus Adapter (for custom metrics API)
- Kubernetes HPA (Horizontal Pod Autoscaler)
- Grafana (optional, for observability)
- Load testing tool like hey to generate traffic and test it
