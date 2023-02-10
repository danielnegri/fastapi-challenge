# FastAPI Challenge

The test of a strong engineer isn’t about how much they know now, but how
efficiently learn what they need and apply that to solve a
problem.

In this challenge, we are going to create a REST API for a Loan Amortization
app using the python miniframework FastAPI.

The API should allow a client:

* **Create a user**

* **Create a loan**

* **Fetch loan schedule**

* **Fetch loan summary for a specific month**

A loan record should at least contain the following fields:

Amount
* Annual Interest Rate
* Loan Term in months

The loan schedule endpoint should return an array of length loan_term,
consisting of:
```json
{
  Month: n
  Remaining balance: $xxxx,
  Monthly payment: $xxx
}
```

The loan summary endpoint should accept a month number as a parameter
and return:
* Current principal balance at given month
* The aggregate amount of principal already paid
* The aggregate amount of interest already paid

To calculate the above, you will have to code a function that
generates an amortization schedule. There are plenty of libraries that
can do this for you, but for this challenge, please develop the
function yourself. You may use general libraries, such as numpy, if
you would like.

Scoring of the challenge is based on:
* Proper HTTP methods
* Error handling and validation-API structuring
* Calculation Accuracy
* Git commits

The following items are optional:
- Use pytests or other test framework to test your endpoints and
financial calculations
- Use an ORM + SQL DB to save users and loans. We’d recommend using
SQLAlchemy or SQLModel, with an in-memory instance of SQLite -
but that is up to you.
