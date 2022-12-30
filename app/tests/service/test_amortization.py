import decimal

import pytest

from app.service.amortization import amortization_schedule


def test_amortization_schedule() -> None:
    principal: int = 150000
    period: int = 36
    annual_interest_rage: decimal = 0.1

    expected = (
        # period, amount, interest, principal, balance
        (1, 4840.08, 1250.00, 3590.08, 146409.92),
        (2, 4840.08, 1220.08, 3620.00, 142789.92),
        (3, 4840.08, 1189.92, 3650.16, 139139.76),
        (4, 4840.08, 1159.50, 3680.58, 135459.18),
        (5, 4840.08, 1128.83, 3711.25, 131747.93),
        (6, 4840.08, 1097.90, 3742.18, 128005.75),
        (7, 4840.08, 1066.71, 3773.37, 124232.38),
        (8, 4840.08, 1035.27, 3804.81, 120427.57),
        (9, 4840.08, 1003.56, 3836.52, 116591.05),
        (10, 4840.08, 971.59, 3868.49, 112722.56),
        (11, 4840.08, 939.35, 3900.73, 108821.83),
        (12, 4840.08, 906.85, 3933.23, 104888.60),
        (13, 4840.08, 874.07, 3966.01, 100922.59),
        (14, 4840.08, 841.02, 3999.06, 96923.53),
        (15, 4840.08, 807.70, 4032.38, 92891.15),
        (16, 4840.08, 774.09, 4065.99, 88825.16),
        (17, 4840.08, 740.21, 4099.87, 84725.29),
        (18, 4840.08, 706.04, 4134.04, 80591.25),
        (19, 4840.08, 671.59, 4168.49, 76422.76),
        (20, 4840.08, 636.86, 4203.22, 72219.54),
        (21, 4840.08, 601.83, 4238.25, 67981.29),
        (22, 4840.08, 566.51, 4273.57, 63707.72),
        (23, 4840.08, 530.90, 4309.18, 59398.54),
        (24, 4840.08, 494.99, 4345.09, 55053.45),
        (25, 4840.08, 458.78, 4381.30, 50672.15),
        (26, 4840.08, 422.27, 4417.81, 46254.34),
        (27, 4840.08, 385.45, 4454.63, 41799.71),
        (28, 4840.08, 348.33, 4491.75, 37307.96),
        (29, 4840.08, 310.90, 4529.18, 32778.78),
        (30, 4840.08, 273.16, 4566.92, 28211.86),
        (31, 4840.08, 235.10, 4604.98, 23606.88),
        (32, 4840.08, 196.72, 4643.36, 18963.52),
        (33, 4840.08, 158.03, 4682.05, 14281.47),
        (34, 4840.08, 119.01, 4721.07, 9560.40),
        (35, 4840.08, 79.67, 4760.41, 4799.99),
        (36, 4839.99, 40.00, 4799.99, 0.00),
    )

    result = amortization_schedule(
        principal=principal, annual_interest_rate=annual_interest_rage, period=period
    )
    for e, r in zip(expected, result):
        assert pytest.approx(e) == r


def test_amortization_schedule_zero_interest() -> None:
    principal: int = 3_000_00
    period: int = 3
    annual_interest_rage: decimal = 0.0

    expected = (
        # period, amount, interest, principal, balance
        (1, 1_000_00, 0, 1_000_00, 2_000_00),
        (2, 1_000_00, 0, 1_000_00, 1_000_00),
        (3, 1_000_00, 0, 1_000_00, 0),
    )

    result = amortization_schedule(
        principal=principal, annual_interest_rate=annual_interest_rage, period=period
    )

    for e, r in zip(expected, result):
        assert pytest.approx(e) == r
