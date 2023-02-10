# Tutorial - User Guide - Intro

## Run the code

To run any of the examples, copy the commands to a terminal, and start uvicorn with:

```bash
$ docker build --rm -t fastapi-challenge .
$ docker run -it --rm -p 8000:80 fastapi-challenge
```

## Login with an Admin (superuser)

```bash
$ curl --location --request POST 'localhost:8000/api/v1/auth/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'username=admin@example.com' \
    --data-urlencode 'password=admin'

# Response: 201 Created
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzM3MjgwNjksInN1YiI6InVfNzg0Y2FhYWNiODRjIn0.S8IQZI_x_LQTQyc0rZpaA9lRDVbidAlV0CWAd3fzYdk",
    "token_type": "bearer"
}
```

## Create a user

Only admin users have access to creating users. Make sure to login as an admin
and use the access token to create a new user.

```bash
$ curl --location --request POST 'localhost:8000/api/v1/users' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzM3MjgwNjksInN1YiI6InVfNzg0Y2FhYWNiODRjIn0.S8IQZI_x_LQTQyc0rZpaA9lRDVbidAlV0CWAd3fzYdk' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "email": "john.stewart@example.com",
        "password": "zP6ajmjv"
    }'

# Response: 201 Created
{
    "email": "john.stewart@example.com",
    "is_active": true,
    "is_superuser": false,
    "full_name": null,
    "id": "u_df6ca3fa84f6",
    "created_at": "2022-12-30T20:33:02.877207",
    "updated_at": "2022-12-30T20:33:02.877211"
}
```

### Get a user by ID

```bash
$ curl --location --request GET 'localhost:8000/api/v1/users' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzM3MjgwNjksInN1YiI6InVfNzg0Y2FhYWNiODRjIn0.S8IQZI_x_LQTQyc0rZpaA9lRDVbidAlV0CWAd3fzYdk' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'username="john.stewart@example.com"' \
    --data-urlencode 'password=secret'


# Response: 200 OK
[
    {
        "email": "admin@example.com",
        "is_active": true,
        "is_superuser": true,
        "full_name": "Administrator",
        "id": "u_784caaacb84c",
        "created_at": "2022-12-30T20:26:20.874815",
        "updated_at": "2022-12-30T20:26:20.874840"
    },
    {
        "email": "john.stewart@example.com",
        "is_active": true,
        "is_superuser": false,
        "full_name": null,
        "id": "u_df6ca3fa84f6",
        "created_at": "2022-12-30T20:33:02.877207",
        "updated_at": "2022-12-30T20:33:02.877211"
    }
]
```

### Update a user

```bash
$ curl --location --request PUT 'localhost:8000/api/v1/users/u_df6ca3fa84f6' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzM3MjgwNjksInN1YiI6InVfNzg0Y2FhYWNiODRjIn0.S8IQZI_x_LQTQyc0rZpaA9lRDVbidAlV0CWAd3fzYdk' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "full_name": "John Stewart"
    }'


# Response: 200 OK
{
    "email": "john.stewart@example.com",
    "is_active": true,
    "is_superuser": false,
    "full_name": "John Stewart",
    "id": "u_df6ca3fa84f6",
    "created_at": "2022-12-30T20:33:02.877207",
    "updated_at": "2022-12-30T20:38:32.315793"
}
```

## Login with a normal user

```bash
$ curl --location --request POST 'localhost:8000/api/v1/auth/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'username="john.stewart@example.com"' \
    --data-urlencode 'password=zP6ajmjv'

# Response: 201 Created
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzM3MjkwNjUsInN1YiI6InVfYmI4YTIzNmNhMDVjIn0.8ngFy7VL9Oj1Lw5MgruSqUdMu5pd38yo-peo8EMUqDs",
    "token_type": "bearer"
}
```

## Create a loan

```bash
$ curl --location --request POST 'localhost:8000/api/v1/loans' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzM3MjkwNjUsInN1YiI6InVfYmI4YTIzNmNhMDVjIn0.8ngFy7VL9Oj1Lw5MgruSqUdMu5pd38yo-peo8EMUqDs' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Small Loan",
    "amount_cents": 10000,
    "annual_interest_rate": 0.1,
    "term_months": 24,
    "due_monthly_starting": "2023-01-01"
}'

# Response: 201 Created
{
    "user_id": "u_2df8c1a1a0d9",
    "title": "Small Loan",
    "amount_cents": 10000,
    "annual_interest_rate": 0.1,
    "currency": "USD",
    "term_months": 24,
    "due_monthly_starting": "2023-01-01",
    "is_active": true,
    "id": "l_68281fc97a6c",
    "created_at": "2022-12-30T20:50:32.130443",
    "updated_at": "2022-12-30T20:50:32.130446"
}
```

## List loans

```bash
$ curl --location --request GET 'localhost:8000/api/v1/loans' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzM3MjkwNjUsInN1YiI6InVfYmI4YTIzNmNhMDVjIn0.8ngFy7VL9Oj1Lw5MgruSqUdMu5pd38yo-peo8EMUqDs'

# Response: 200 OK
[
    {
        "user_id": "u_2df8c1a1a0d9",
        "title": "Small Loan",
        "amount_cents": 10000,
        "annual_interest_rate": 0.1,
        "currency": "USD",
        "term_months": 24,
        "due_monthly_starting": "2023-01-01",
        "is_active": true,
        "id": "l_68281fc97a6c",
        "created_at": "2022-12-30T20:50:32.130443",
        "updated_at": "2022-12-30T20:50:32.130446"
    }
]
```

## List loan schedules

```bash
$ curl --location --request GET 'localhost:8000/api/v1/loans/l_68281fc97a6c/schedule' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzM3MjkwNjUsInN1YiI6InVfYmI4YTIzNmNhMDVjIn0.8ngFy7VL9Oj1Lw5MgruSqUdMu5pd38yo-peo8EMUqDs'

# Response: 200 OK
[
    {
        "loan_id": "l_68281fc97a6c",
        "month": 1,
        "due": "2023-01-01",
        "amount_cents": 461,
        "interest_cents": 83,
        "principal_cents": 378,
        "balance_cents": 9622,
        "status": "scheduled",
        "id": "ls_0994f635730c",
        "created_at": "2022-12-30T20:50:32.134452",
        "updated_at": "2022-12-30T20:50:32.134455"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 2,
        "due": "2023-02-01",
        "amount_cents": 461,
        "interest_cents": 80,
        "principal_cents": 381,
        "balance_cents": 9241,
        "status": "scheduled",
        "id": "ls_5015812b4c9f",
        "created_at": "2022-12-30T20:50:32.138419",
        "updated_at": "2022-12-30T20:50:32.138422"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 3,
        "due": "2023-03-01",
        "amount_cents": 461,
        "interest_cents": 77,
        "principal_cents": 384,
        "balance_cents": 8856,
        "status": "scheduled",
        "id": "ls_5f086a931155",
        "created_at": "2022-12-30T20:50:32.141090",
        "updated_at": "2022-12-30T20:50:32.141093"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 4,
        "due": "2023-04-01",
        "amount_cents": 461,
        "interest_cents": 74,
        "principal_cents": 388,
        "balance_cents": 8469,
        "status": "scheduled",
        "id": "ls_37a81476022d",
        "created_at": "2022-12-30T20:50:32.143537",
        "updated_at": "2022-12-30T20:50:32.143539"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 5,
        "due": "2023-05-01",
        "amount_cents": 461,
        "interest_cents": 71,
        "principal_cents": 391,
        "balance_cents": 8078,
        "status": "scheduled",
        "id": "ls_836210339a78",
        "created_at": "2022-12-30T20:50:32.145993",
        "updated_at": "2022-12-30T20:50:32.145996"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 6,
        "due": "2023-06-01",
        "amount_cents": 461,
        "interest_cents": 67,
        "principal_cents": 394,
        "balance_cents": 7683,
        "status": "scheduled",
        "id": "ls_8a777004c15c",
        "created_at": "2022-12-30T20:50:32.148336",
        "updated_at": "2022-12-30T20:50:32.148339"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 7,
        "due": "2023-07-01",
        "amount_cents": 461,
        "interest_cents": 64,
        "principal_cents": 397,
        "balance_cents": 7286,
        "status": "scheduled",
        "id": "ls_a67928396a2a",
        "created_at": "2022-12-30T20:50:32.150678",
        "updated_at": "2022-12-30T20:50:32.150681"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 8,
        "due": "2023-08-01",
        "amount_cents": 461,
        "interest_cents": 61,
        "principal_cents": 401,
        "balance_cents": 6885,
        "status": "scheduled",
        "id": "ls_dceba3be4e7a",
        "created_at": "2022-12-30T20:50:32.153024",
        "updated_at": "2022-12-30T20:50:32.153027"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 9,
        "due": "2023-09-01",
        "amount_cents": 461,
        "interest_cents": 57,
        "principal_cents": 404,
        "balance_cents": 6481,
        "status": "scheduled",
        "id": "ls_510c0ef742d2",
        "created_at": "2022-12-30T20:50:32.155618",
        "updated_at": "2022-12-30T20:50:32.155621"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 10,
        "due": "2023-10-01",
        "amount_cents": 461,
        "interest_cents": 54,
        "principal_cents": 407,
        "balance_cents": 6074,
        "status": "scheduled",
        "id": "ls_30fa84dc9328",
        "created_at": "2022-12-30T20:50:32.158009",
        "updated_at": "2022-12-30T20:50:32.158011"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 11,
        "due": "2023-11-01",
        "amount_cents": 461,
        "interest_cents": 51,
        "principal_cents": 411,
        "balance_cents": 5663,
        "status": "scheduled",
        "id": "ls_ab1788f76d33",
        "created_at": "2022-12-30T20:50:32.160190",
        "updated_at": "2022-12-30T20:50:32.160192"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 12,
        "due": "2023-12-01",
        "amount_cents": 461,
        "interest_cents": 47,
        "principal_cents": 414,
        "balance_cents": 5249,
        "status": "scheduled",
        "id": "ls_39d41f4f349c",
        "created_at": "2022-12-30T20:50:32.162358",
        "updated_at": "2022-12-30T20:50:32.162361"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 13,
        "due": "2024-01-01",
        "amount_cents": 461,
        "interest_cents": 44,
        "principal_cents": 418,
        "balance_cents": 4831,
        "status": "scheduled",
        "id": "ls_da409bbae6a9",
        "created_at": "2022-12-30T20:50:32.164713",
        "updated_at": "2022-12-30T20:50:32.164716"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 14,
        "due": "2024-02-01",
        "amount_cents": 461,
        "interest_cents": 40,
        "principal_cents": 421,
        "balance_cents": 4410,
        "status": "scheduled",
        "id": "ls_f5102b5113af",
        "created_at": "2022-12-30T20:50:32.167164",
        "updated_at": "2022-12-30T20:50:32.167167"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 15,
        "due": "2024-03-01",
        "amount_cents": 461,
        "interest_cents": 37,
        "principal_cents": 425,
        "balance_cents": 3985,
        "status": "scheduled",
        "id": "ls_4a7b7bb481bd",
        "created_at": "2022-12-30T20:50:32.169456",
        "updated_at": "2022-12-30T20:50:32.169459"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 16,
        "due": "2024-04-01",
        "amount_cents": 461,
        "interest_cents": 33,
        "principal_cents": 428,
        "balance_cents": 3557,
        "status": "scheduled",
        "id": "ls_6d1c5f3137f1",
        "created_at": "2022-12-30T20:50:32.171651",
        "updated_at": "2022-12-30T20:50:32.171654"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 17,
        "due": "2024-05-01",
        "amount_cents": 461,
        "interest_cents": 30,
        "principal_cents": 432,
        "balance_cents": 3125,
        "status": "scheduled",
        "id": "ls_76cea173362e",
        "created_at": "2022-12-30T20:50:32.173941",
        "updated_at": "2022-12-30T20:50:32.173944"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 18,
        "due": "2024-06-01",
        "amount_cents": 461,
        "interest_cents": 26,
        "principal_cents": 435,
        "balance_cents": 2690,
        "status": "scheduled",
        "id": "ls_689ca9cee02e",
        "created_at": "2022-12-30T20:50:32.176227",
        "updated_at": "2022-12-30T20:50:32.176230"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 19,
        "due": "2024-07-01",
        "amount_cents": 461,
        "interest_cents": 22,
        "principal_cents": 439,
        "balance_cents": 2251,
        "status": "scheduled",
        "id": "ls_085d58fda3d5",
        "created_at": "2022-12-30T20:50:32.178411",
        "updated_at": "2022-12-30T20:50:32.178413"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 20,
        "due": "2024-08-01",
        "amount_cents": 461,
        "interest_cents": 19,
        "principal_cents": 443,
        "balance_cents": 1808,
        "status": "scheduled",
        "id": "ls_594294b13044",
        "created_at": "2022-12-30T20:50:32.180627",
        "updated_at": "2022-12-30T20:50:32.180630"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 21,
        "due": "2024-09-01",
        "amount_cents": 461,
        "interest_cents": 15,
        "principal_cents": 446,
        "balance_cents": 1362,
        "status": "scheduled",
        "id": "ls_513eee827c1d",
        "created_at": "2022-12-30T20:50:32.182834",
        "updated_at": "2022-12-30T20:50:32.182837"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 22,
        "due": "2024-10-01",
        "amount_cents": 461,
        "interest_cents": 11,
        "principal_cents": 450,
        "balance_cents": 911,
        "status": "scheduled",
        "id": "ls_c93d2a840c51",
        "created_at": "2022-12-30T20:50:32.185134",
        "updated_at": "2022-12-30T20:50:32.185137"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 23,
        "due": "2024-11-01",
        "amount_cents": 461,
        "interest_cents": 8,
        "principal_cents": 454,
        "balance_cents": 458,
        "status": "scheduled",
        "id": "ls_e02c8d72a47d",
        "created_at": "2022-12-30T20:50:32.187384",
        "updated_at": "2022-12-30T20:50:32.187387"
    },
    {
        "loan_id": "l_68281fc97a6c",
        "month": 24,
        "due": "2024-12-01",
        "amount_cents": 461,
        "interest_cents": 4,
        "principal_cents": 458,
        "balance_cents": 0,
        "status": "scheduled",
        "id": "ls_603299ac9dff",
        "created_at": "2022-12-30T20:50:32.189858",
        "updated_at": "2022-12-30T20:50:32.189861"
    }
]
```






