# Cloud Native Delivery Platform

A hands-on DevOps engineering project focused on building an automated, secure, and observable application delivery workflow.

## Overview

The goal of this project is to demonstrate how an application can move from source code to a running Kubernetes deployment through a reproducible and automated process.

A lightweight Python API (`uptime-api`) serves as the sample application. The main focus is not application development, but the infrastructure, automation, security, and operational practices required to deploy and maintain it.

## Planned Architecture

The project will progressively integrate:

- **Docker** – Application containerization
- **Kubernetes** – Application orchestration and networking
- **Helm** – Application packaging and deployment
- **Terraform & Azure** – Infrastructure as Code
- **GitHub Actions** – Continuous integration and delivery
- **Prometheus & Grafana** – Monitoring and observability

The initial deployment target is a self-hosted Kubernetes cluster.

## Project Goals

- Build a reproducible application deployment process.
- Automate testing, image builds, and deployments.
- Apply Kubernetes security and reliability best practices.
- Implement monitoring and basic alerting.
- Practice troubleshooting, deployment failures, and rollback procedures.
- Document architectural decisions and operational workflows.

## Project Status

**Status: Early development**

The project is being developed incrementally. Features and infrastructure will be introduced through small, focused changes, with each milestone building on the previous one.

## Purpose

This is a personal learning and portfolio project focused on practical DevOps and Platform Engineering skills.