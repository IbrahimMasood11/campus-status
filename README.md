# Campus Status

Campus Status is a small local project used to practise Git, GitHub and Microsoft Planner workflow.

The project contains:

- JSON configuration files
- standard-library Python scripts
- operational documentation
- a simple static status page

The technical system is deliberately simple. The main purpose is to practise how a team plans, changes, reviews and records work over time.

## Run the local demo site

From the repository root:

```bash
python -m http.server 8080 --directory site
```

On some Windows installations:

```bash
py -m http.server 8080 --directory site
```

Then open:

```text
http://localhost:8080
```

## Validate configuration

```bash
python scripts/validate_config.py
```

or:

```bash
py scripts/validate_config.py
```

## Run the health check

Start the demo site first, then in a second terminal:

```bash
python scripts/health_check.py
```

## Important security rule

Do not commit real passwords, API tokens, SSH private keys, cloud credentials or `.env` files.

Use `.env.example` to document expected configuration names without storing real values.
