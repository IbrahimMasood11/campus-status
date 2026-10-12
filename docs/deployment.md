# Deployment notes

For the lab demo, run the status site locally:

```bash
python -m http.server 8080 --directory site
```

The configured port is stored in `config/service.json`.

If the configuration and the running command disagree, the health check may fail.
