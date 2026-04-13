# GitHub Actions - Node 24 Compatible Versions (Updated 2025)

```
- name: Checkout Code
uses: actions/checkout@v5

- name: Configure AWS credentials
uses: aws-actions/configure-aws-credentials@v6.1.0

- name: Set up Node.js
uses: actions/setup-node@v4.2.0

- name: Set up Python
uses: actions/setup-python@v5.4.0

- name: Cache dependencies
uses: actions/cache@v4.2.0

- name: Upload Build Artifact
uses: actions/upload-artifact@v4.6.1

- name: Download Build Artifact
uses: actions/download-artifact@v4.1.9

- name: Build and Push Docker image
uses: docker/build-push-action@v6.15.0 

```

