# HealthQueue | DevOps Capstone Portfolio

**A healthcare-inspired reference project showcasing automated delivery, infrastructure as code, Kubernetes, GitOps, and operational reliability.**

> Portfolio demonstration with synthetic data. Designed as an educational architecture, not a live clinical service.

## Project Summary
HealthQueue brings together the DevOps practices I developed in CST 365. The project organizes a healthcare appointment API reference workflow around source control, automated validation, containerization, infrastructure configuration, Kubernetes deployment manifests, and GitOps operations. It illustrates how an engineering team can develop a delivery process that emphasizes consistency, traceability, and maintainability.

## Problem Statement
A health-technology organization needs a way to evolve its appointment service while coordinating development, security, infrastructure, and operations. Untracked configuration changes and manual releases can make services difficult to maintain. HealthQueue addresses this design problem through version-controlled configuration and automation-oriented practices.

## Technologies Used
| Area | Technologies / concepts |
| --- | --- |
| Source and automation | Git, GitHub, GitHub Actions, CI/CD |
| Application and containerization | Python API, Docker, container registry concepts |
| Infrastructure | OpenTofu, declarative resources, variables and outputs |
| Orchestration and GitOps | Kubernetes manifests, Argo CD |
| Security | Container hardening, secret-handling principles, vulnerability scanning concepts |
| Reliability | Health checks, monitoring and observability planning, DORA/SLO concepts |

## Architecture Overview

    Developer updates repository
                |
                v
        GitHub source control
                |
                v
        GitHub Actions CI/CD
      (validation, build, checks)
                |
                v
         Container image
                |
                v
     Kubernetes configuration <---- Argo CD GitOps reconciliation
                |
                v
     Appointment API / service

OpenTofu defines supporting infrastructure resources.
Health checks and SRE practices guide operational validation.

The diagram communicates the project's intended delivery design; the status of any individual automated step should be established from its actual run logs before describing it as successfully executed.

## Key Design Decisions
1. **Git-centered changes:** Treat the repository as the shared record for application and deployment configuration, making changes easier to review and explain.
2. **Repeatable automation:** Use CI/CD configuration to structure checks and container-build work rather than relying entirely on manual steps.
3. **Declarative infrastructure:** Represent required infrastructure using OpenTofu so that changes are documented and can be reviewed before application.
4. **Kubernetes and GitOps:** Separate desired deployment configuration from operational reconciliation using manifests and Argo CD.
5. **Security and reliability from the start:** Apply container hardening and health-check practices; avoid committing credentials or sensitive healthcare information.

## Challenges and How I Approached Them
Connecting CI/CD, containers, Kubernetes, and GitOps taught me to examine the whole delivery path rather than view each tool separately. I practiced interpreting build and deployment behavior, adjusting configuration, and troubleshooting Kubernetes workloads. These experiences improved my ability to approach technical challenges methodically, communicate design choices, and identify the evidence needed to assess a release.

## Outcomes and Professional Skills Demonstrated
- Organized multiple DevOps tools around one realistic health-tech use case.
- Practiced source control and automation-oriented deployment workflows.
- Developed familiarity with infrastructure-as-code and declarative Kubernetes configuration.
- Applied security-conscious configuration and reliability concepts.
- Strengthened technical documentation, problem solving, and communication skills.

**Evidence standard:** Repository configuration demonstrates implementation work. Live operating status, security results, availability, and deployment performance are established by actual workflow logs, cluster status, and test outputs—not inferred from the presence of files.

## Validation and Reproduction
For a clean validation, review the current repository's application setup instructions and execute these checks in an authorized development environment:

1. Run the application's documented tests and capture the results.
2. Review GitHub Actions execution details for the latest commit.
3. Validate OpenTofu configuration with `tofu fmt -check` and `tofu validate` after initialization (do not apply cloud resources without approved credentials and cost controls).
4. Review Kubernetes manifests and verify workload health using `kubectl get pods -A` and relevant logs.
5. Inspect Argo CD application status and check the deployed API's documented health endpoint.
6. Record confirmed outcomes and screenshots in a future `docs/evidence/` folder.

Do not include real patient information, cloud credentials, tokens, or private keys in this repository.

## Next Iteration
- Expand automated test coverage and strengthen CI checks.
- Add a safe `.env.example` where configuration is required and document prerequisite credentials.
- Record reproducible evidence of CI, container scanning, and deployment verification.
- Explore staged promotions, rollback procedures, dashboards, and actionable alerts.
- Use measured DORA and service-level indicators to evaluate improvement over time.

## Career Connection
HealthQueue highlights skills relevant to **entry-level DevOps, platform operations, and cloud support roles in health technology**. In an interview, I would walk through the architecture, explain the trade-offs of GitOps and IaC, describe my troubleshooting process, and discuss the operational checks I would use before promoting a change.

## Course Learning Connection
The project brings together CI/CD design, security, infrastructure automation, container orchestration, GitOps, and SRE principles introduced throughout CST 365. It reflects my growth from understanding individual tools to seeing how technical choices work together in a delivery lifecycle.
