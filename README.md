# Toy example fastapi and svcs

I want to experiment with
[svcs](https://svcs.hynek.me/en/stable/core-concepts.html) and
[fastapi](https://fastapi.tiangolo.com/advanced/events/) to find a good pattern
for dependency injection (or service location) alongside configuration and testing.

- readable
- robust service replacement for all tests
  - integration
  - mocks
- minimal boilerplate
- teardown (close db connections)

This repo intended to be a super simple example for future experimentation.

Some additional details:

- `pytest`
- `pydantic-settings`
- `pipreqs` to generate requirements
