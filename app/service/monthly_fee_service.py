from app.database import MonthlyFee, MonthlyFees
from app.exception import MonthlyFeeNotFound
from app.schema import MonthlyFeeSchema


def create(data: MonthlyFeeSchema) -> MonthlyFee:
    monthly_fee = MonthlyFee(**data)
    MonthlyFee.save(monthly_fee)
    return monthly_fee


def get_all() -> MonthlyFees:
    return MonthlyFee.find_all()


def get_all_by_name(name: str) -> MonthlyFees:
    return MonthlyFee.find_all_by_name(name)


def get_one_by_id(id: int) -> MonthlyFee:
    monthly_fee = MonthlyFee.find_first_by_id(id)
    if not monthly_fee: raise MonthlyFeeNotFound()
    return monthly_fee


def update(id: int, data: MonthlyFeeSchema) -> MonthlyFee:
    monthly_fee = get_one_by_id(id)
    monthly_fee.update(**data)
    MonthlyFee.save(monthly_fee)
    return monthly_fee


def delete(id: int) -> None:
    monthly_fee = get_one_by_id(id)
    MonthlyFee.delete(monthly_fee)
