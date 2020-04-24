# python-profiling-example
A simple example of using cProfile


Usage

```
python app.py
```

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
         5 function calls in 1.567 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.567    1.567 <string>:1(<module>)
        1    0.063    0.063    1.567    1.567 app.py:8(hi)
        1    0.000    0.000    1.567    1.567 {built-in method builtins.exec}
        1    1.504    1.504    1.504    1.504 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


127.0.0.1 - - [24/Apr/2020 13:24:18] "GET / HTTP/1.1" 200 -

```


