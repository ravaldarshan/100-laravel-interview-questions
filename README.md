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

### 36. How to order a specific record (e.g., India) first and others after in Laravel?
**Answer:** Use: orderByRaw("name = 'India' DESC")->orderBy('name', 'DESC')

### 37. How do you get the top 3 selling products using Eloquent?
**Answer:** Product::orderBy('sales_count', 'DESC')->take(3)->get();

### 38. How to fetch users who don’t have any posts using Eloquent?
**Answer:** User::doesntHave('posts')->get();

### 39. How to select the latest record per group (e.g., latest order per customer)?
**Answer:** Use subqueries or Laravel 8+ selectRaw with join on max(id) per group.

### 40. How to join two tables and get records even if no match exists?
**Answer:** Use leftJoin: DB::table('users')->leftJoin('orders', 'users.id', '=', 'orders.user_id')->get();

### 41. How to write a dynamic where condition in Laravel only if a parameter is present?
**Answer:** Use when(): ->when($filter, fn($q) => $q->where('status', $filter))

### 42. How to filter records between two dates using Eloquent?
**Answer:** Model::whereBetween('created_at', [$from, $to])->get();

### 43. How to write a subquery in Laravel's Eloquent or Query Builder?
**Answer:** Use addSelect with DB::raw() or subQuery inside closure

### 44. How to paginate an Eloquent result and keep query parameters?
**Answer:** $models = Model::paginate(10)->withQueryString();

### 45. How to eager load a relationship with conditions?
**Answer:** Model::with(['comments' => fn($q) => $q->where('status', 'active')])->get();

### 46. How to pass multiple variables to all views without using compact every time?
**Answer:** Use view()->share('key', $value) in a service provider like AppServiceProvider.

### 47. How to show different layouts based on user role in Blade?
**Answer:** Use @if(auth()->user()->isAdmin()) @include('layouts.admin') @else @include('layouts.user') @endif

### 48. What is the difference between @include, @component, and @yield in Blade?
**Answer:** @include inserts a partial; @component allows slot passing; @yield defines a section to be filled by @section.

### 49. How to use loops and conditionals in Blade to generate a dynamic menu?
**Answer:** Use @foreach and @if with a menu array: @foreach($menu as $item) <li>{{ $item['title'] }}</li> @endforeach

### 50. How to define a route with optional parameters?
**Answer:** Route::get('/user/{id?}', fn($id = null) => ...);

### 51. How to handle route model binding with a different column (e.g., slug)?
**Answer:** Route::get('/post/{post:slug}', [PostController::class, 'show']);

### 52. How to create a RESTful controller and what are the 7 default methods?
**Answer:** Use php artisan make:controller --resource; Methods: index, create, store, show, edit, update, destroy

### 53. How to create a grouped route with a common prefix and middleware?
**Answer:** Route::prefix('admin')->middleware('auth')->group(function() { Route::get('/dashboard', ...); });

### 54. How to create a middleware to block access on weekends?
**Answer:** Create custom middleware, check Carbon::now()->isWeekend() and return abort(403)

### 55. How to share authenticated user data across all controllers?
**Answer:** Use view()->share('user', auth()->user()) in a service provider or middleware.

### 56. How to validate request input based on condition?
**Answer:** Use sometimes or required_if: 'field_a' => 'required_if:field_b,yes'

### 57. How to authorize a request using policy in controller method?
**Answer:** Use $this->authorize('update', $post); inside the controller

### 58. What is the difference between hasOne and belongsTo?
**Answer:** hasOne is defined on the parent model, belongsTo is defined on the child referencing the parent’s key.

### 59. How to define a many-to-many relationship with additional pivot columns?
**Answer:** Define with ->withPivot('column_name') in the relationship method and use belongsToMany.

### 60. How to use withCount() and withSum() in Eloquent?
**Answer:** Use Model::withCount('relation')->withSum('relation', 'amount')->get();

### 61. How to eager load nested relationships (e.g., posts → comments → user)?
**Answer:** Use Model::with('posts.comments.user')->get();

### 62. How to cache an Eloquent query and invalidate it after a new record is created?
**Answer:** Use Cache::remember() and clear it on model events like created/updated.

### 63. How to upload a file and store it in a specific folder with a custom name?
**Answer:** $path = $request->file('image')->storeAs('images', 'custom_name.jpg');

### 64. How to build an API response using Resource classes?
**Answer:** Use return new UserResource($user); or return UserResource::collection($users);

### 65. How to queue an email and send it in the background?
**Answer:** Use Mail::to($user)->queue(new WelcomeMail($user)); and configure queue driver.

### 66. How to broadcast real-time notifications using Laravel Echo & Pusher?
**Answer:** Create event implements ShouldBroadcast, configure broadcasting.php and use Echo on frontend.

### 67. How to write a job that retries 3 times and then fails gracefully?
**Answer:** Set public $tries = 3; and handle failure in failed() method in the job class.

### 68. How to use custom validation rules (e.g., check if a date is a working day)?
**Answer:** Create a custom Rule class using php artisan make:rule WorkingDay and define logic in passes().

### 69. How to trigger an event after a user is created and log the data?
**Answer:** Dispatch event in User::created() model event or controller and handle it in a listener.

---

## 🧠 Contributing

Feel free to fork and suggest new questions or corrections via pull request.


> Made with ❤️ for Laravel developers and learners.
