# Loop Refactoring Interview
Technical - Coding for Software Engineers


### Notes

Hi Aaron and Chris, thanks for meeting with me today. Our time was short so I
wanted to go ahead and finish up some of the things we spoke about. After
looking through the code for another minute to familiarize myself I took care
of the basics of what I think you were looking for today. 

I ripped through it quickly in the spirit of the interview so there are
definitely some caveats to my approach, and some things not finished; for
example some single responsibility blur in the Order object, or an opportunity
to separate tax logic from product with service classes. I also made sure
existing tests pass, but I didn't create a new test harness.

Thanks again for your time - I hope this helps!

---


### Getting it running

- Pull down the repo and run poetry install in the top level directory (Install python 3.13.2 and Poetry if you need to)
- After that you should be able to run the tests: `poetry run pytest .`


### Instructions

For our technical assessment, we will be asking you to refactor an existing
application. This will take place in the form of a hands on coding exercise in
either php, typescript, or python. The prompt is outlined below. Our goal is to
see how you work in an existing codebase and the technical decisions you make
to leave it better than you found it.


### Problem: Refactor an Existing Order Flow App


Here you find a simple order flow application. It's able to create orders, do
some calculations (totals and taxes), and manage them (approval/reject and
shipment).

The old development team did not find the time to build a proper domain model
but instead preferred to use a procedural style, building this anemic domain
model. Fortunately, they did at least take the time to write unit tests for the
code.

Your new CTO, after many bugs caused by this application, asked you to refactor
this code to make it more maintainable and reliable.

