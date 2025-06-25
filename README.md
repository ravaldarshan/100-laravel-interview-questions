# 📘 Laravel Interview Questions & Answers

### 1. What is the request lifecycle in Laravel?
**Answer:** The request lifecycle in Laravel includes routing, middleware, controller execution, and response. It starts in public/index.php and passes through the HTTP Kernel.

### 2. How many Laravel versions have you worked with, and what is the latest version of Laravel?
**Answer:** Answers will vary. As of 2025, the latest version is Laravel 11.

### 3. What is the difference between old and new versions of Laravel?
**Answer:** Newer versions have better performance, improved syntax, built-in features (like job batching, Octane, etc.), and reduced boilerplate.

### 4. What is Artisan, and how can we use it? Also, explain at least 5 Artisan commands.
**Answer:** Artisan is Laravel's CLI. Examples: `php artisan make:controller`, `migrate`, `route:list`, `queue:work`, `tinker`.

### 5. What is the difference between composer.json and composer.lock?
**Answer:** `composer.json` defines package versions. `composer.lock` records exact installed versions.

### 6. What is Tinker, and what is its use?
**Answer:** Tinker is an interactive REPL used to run PHP/Laravel code in the console.

### 7. What is ORM, and how do we use it in Laravel?
**Answer:** ORM (Object Relational Mapping) is used for database interaction using models. Laravel uses Eloquent as its ORM.

### 8. What is the use of console.php, channels.php, web.php, and api.php?
**Answer:** They define routes: `console.php` for Artisan, `channels.php` for broadcasting, `web.php` for browser routes, `api.php` for API routes.

### 9. What is Laravel Reverb?
**Answer:** Laravel Reverb is a real-time broadcasting server built into Laravel for WebSocket communication.

### 10. What is middleware? What are the types of middleware?
**Answer:** Middleware filters HTTP requests. Types: global, route, group-based (e.g., auth, throttle).

### 11. What is a guard in Laravel? What are the types of guards?
**Answer:** Guards define how users are authenticated. Types: session, token (API), custom.

### 12. What are gates and policies?
**Answer:** Both manage authorization. Gates are closures; policies are classes for models.

### 13. What is the difference between Eloquent and Query Builder?
**Answer:** Eloquent uses models and relationships. Query Builder is more raw and flexible. Use Eloquent for clean model logic, Query Builder for complex joins.

### 14. What is the difference between migrate:fresh and migrate:refresh?
**Answer:** `migrate:fresh` drops all tables. `migrate:refresh` rolls back and re-runs migrations.

### 15. What are factories and seeders in Laravel?
**Answer:** Factories generate fake data; seeders populate the database using those factories.

### 16. How many databases does Laravel support?
**Answer:** Officially: SQLite, MySQL, MariaDB, PostgreSQL, SQL Server. MongoDB via package.

### 17. What are soft deletes in Laravel?
**Answer:** Soft deletes mark records as deleted without removing them from the database.

### 18. What are events and listeners in Laravel?
**Answer:** Events are actions; listeners handle them. Useful for decoupling logic (e.g., after user registration).

### 19. What is the service container in Laravel?
**Answer:** The service container is Laravel’s dependency injection system for resolving classes and services.

### 20. What is a model observer?
**Answer:** Observers watch model events like created, updated, deleted, etc.

### 21. What are mutators and accessors in Laravel?
**Answer:** They modify model data on get/set using `getXAttribute` and `setXAttribute`.

### 22. What are API resources, route resources, and controller resources in Laravel?
**Answer:** API resources format responses. Route resources define RESTful routes. Controller resources handle resource logic.

### 23. Why do we use the APP_KEY in Laravel?
**Answer:** It is used for encryption and hashing in sessions, cookies, etc.

### 24. What are the official packages provided by Laravel?
**Answer:** Sanctum, Passport, Scout, Cashier, Breeze, Jetstream, Socialite, Dusk, Valet, Fortify, etc.

### 25. What are the most commonly used API status codes?
**Answer:** 200 OK, 201 Created, 301 Redirect, 401 Unauthorized, 403 Forbidden, 404 Not Found, 422 Validation Error, 500 Server Error

### 26. What is the .env file used for?
**Answer:** To manage environment-specific variables like DB credentials, API keys, and app config.

### 27. What is dependency injection in Laravel?
**Answer:** Injecting class dependencies into a class method or constructor automatically via the service container.

### 28. What is SQL injection, and how does Laravel protect against it?
**Answer:** SQL injection is malicious SQL input. Laravel uses prepared statements and query binding to prevent it.

### 29. What is the difference between bind and singleton in Laravel?
**Answer:** `bind()` creates a new instance every time. `singleton()` returns the same instance.

### 30. What are service providers in Laravel?
**Answer:** They bootstrap services like route, DB, events. Registered in `config/app.php`.

### 31. What are services, traits, and helper classes in Laravel?
**Answer:** Services encapsulate logic, traits reuse code in classes, helpers provide global functions.

### 32. What is loosely coupled vs. tightly coupled code in Laravel?
**Answer:** Loosely coupled code depends on interfaces or abstractions; tightly coupled depends on specific classes.

### 33. How do you load one million records efficiently in Laravel?
**Answer:** Use `chunk()`, `cursor()`, or raw DB queries to reduce memory usage.

### 34. What is eager loading in Laravel? What is the N+1 problem?
**Answer:** Eager loading loads related models to avoid N+1 queries. Use `with()` to fix it.

### 35. What is overlapping in Laravel?
**Answer:** Could refer to overlapping route patterns, job attempts, or schedule clashes. Please clarify context.

### 36. What are the core types of OOP?
**Answer:** Encapsulation, Inheritance, Polymorphism, Abstraction. Others include: constructor, destructor, static, traits, namespaces, magic methods.


---

## 🧠 Contributing

Feel free to fork and suggest new questions or corrections via pull request.


> Made with ❤️ for Laravel developers and learners.
