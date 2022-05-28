### Exercises

- Create a JavaScript file under /assets, serve it from server.py with the correct content-type, and request it from index.html.
- Basic counter functionality:
  - Make an API call to GET /counter and display the counter.
  - Add a button that calls POST /add, and updates the displayed counter value with the response.
  - Add a button that calls POST /subtract, and updates the displayed counter value with the response.
- Extended functionality:
  - Extend the /add and /subtract endpoints to take a `number` query param, and increment/decrement the counter given that value (defaults to 1 if not present).
  - Add an input box to the webpage, allowing the user to specifiy a number to increment/decrement by.
